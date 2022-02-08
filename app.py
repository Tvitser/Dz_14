from flask import Flask, render_template, request, abort
from utils import search_by_id, search_by_title, search_by_year, search_by_rating, search_by_genre

app = Flask(__name__)


@app.route("/movies/<title>")
def search_by_title_page(title):
    if title != None:
        data=search_by_title(title)
    else:abort(404)
    return render_template("movies.html", data=data)

@app.route("/movies/<year1>/to/<year2>")
def search_by_year_page(year1, year2):
    data=search_by_year(year1, year2)
    return render_template("year_search.html", data=data)


@app.route("/rating/<rating>/")
def search_by_age_page(rating):
    data=search_by_rating(rating)
    return render_template("rating_search.html", data=data)

@app.route("/genre/<genre>")
def genre_page(genre):
    data=search_by_genre(genre)
    print(data)
    return render_template("genre_search.html", data=data)
app.run(debug=True)