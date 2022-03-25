import sqlite3

import json


def get_movie_by_title(title):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        sqlite_query = f"SELECT title, country, release_year, listed_in, description " \
                       f"FROM netflix " \
                       f"WHERE title = '{title}' " \
                       f"ORDER BY release_year;"
        cursor.execute(sqlite_query)
        data = cursor.fetchone()
        new_format = ["title", "country", "release_year", "genre", "description"]
        new_format_data = dict(zip(new_format, data))
        return new_format_data


def get_movies_by_years_gap(from_year, to_year):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        sqlite_query = f"SELECT title, release_year " \
                       f"FROM netflix " \
                       f"WHERE release_year BETWEEN '{from_year}' AND '{to_year}'" \
                       f"ORDER BY release_year LIMIT 100"

        cursor.execute(sqlite_query)
        data = cursor.fetchall()
        new_format = ["title", "release_year"]
        new_format_data = []
        for i in range(len(data)):
            new_format_data.append(dict(zip(new_format, data[i])))
        return new_format_data


def get_movie_by_rating(rating):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        sqlite_query = f"SELECT title, rating, description " \
                       f"FROM netflix " \
                       f"WHERE rating = '{rating}'" \
                       f"ORDER BY release_year LIMIT 10"

        cursor.execute(sqlite_query)
        data = cursor.fetchall()
        new_format = ["title", "rating", "description"]
        new_format_data = []
        for i in range(len(data)):
            new_format_data.append(dict(zip(new_format, data[i])))
        return new_format_data


def get_movies_by_genre(genre):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        sqlite_query = f"SELECT title, rating " \
                       f"FROM netflix " \
                       f"WHERE listed_in LIKE '%{genre}%'" \
                       f"ORDER BY release_year DESC LIMIT 10"

        cursor.execute(sqlite_query)
        data = cursor.fetchall()
        return json.dumps(data)


def get_actors(actor1, actor2):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()

        sqlite_query = f"SELECT netflix.'cast' " \
                       f"FROM netflix " \
                       f"WHERE netflix.'cast' LIKE '%{actor1}%' " \
                       f"AND netflix.'cast' LIKE '%{actor2}%' " \
                       f"ORDER BY release_year "

        actors = []
        buddy_actors = []
        cursor.execute(sqlite_query)
        data = cursor.fetchall()
        for casting in data:
            for person in casting[0].split(','):
                actors.append(person.strip(' '))

        for buddy in actors:
            if actors.count(buddy) > 1 and buddy not in buddy_actors:
                buddy_actors.append(buddy)

        return buddy_actors


def get_movies(movie_type, year, genre):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        sqlite_query = f"SELECT title, description " \
                       f"FROM netflix " \
                       f"WHERE type LIKE '{movie_type}'" \
                       f"AND release_year = '{year}'" \
                       f"AND listed_in LIKE '%{genre}%'" \
                       f"ORDER BY release_year "

        cursor.execute(sqlite_query)
        data = cursor.fetchall()
        return json.dumps(data)
