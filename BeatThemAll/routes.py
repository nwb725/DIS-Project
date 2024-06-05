from flask import render_template, request, jsonify
from app import app
from app.queries import search_sport, get_sport_details


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    query = data.get("query", "")
    if not isinstance(query, str):
        return jsonify({"found": False, "matched_sport": None})

    matched_sport = search_sport(query)
    found = matched_sport is not None
    return jsonify({"found": found, "matched_sport": matched_sport})


@app.route("/query_sport", methods=["POST"])
def query_sport():
    data = request.get_json()
    sport = data.get("sport", "")
    sport_details = get_sport_details(sport)
    return jsonify(sport_details)
