from flask import Flask, jsonify
from utils import get_movie_by_title, get_movies_by_years_gap, get_movie_by_rating

app = Flask(__name__)


@app.route('/movies/<title>')
def page_by_title(title):
    movie = get_movie_by_title(title)

    return jsonify(movie)


@app.route('/movies/<int:from_year>/<int:to_year>')
def page_by_years_gap(from_year, to_year):
    movie = get_movies_by_years_gap(from_year, to_year)

    return jsonify(movie)


@app.route('/movies/rating/children/<rating>')
def page_by_rating_children(rating):
    movie = get_movie_by_rating(rating)

    return jsonify(movie)


@app.route('/movies/rating/family/<rating>')
def page_by_rating_family(rating):
    movie = get_movie_by_rating(rating)

    return jsonify(movie)


@app.route('/movies/rating/adult/<rating>')
def page_by_rating_adult(rating):
    movie = get_movie_by_rating(rating)

    return jsonify(movie)


app.run()
