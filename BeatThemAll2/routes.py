from BeatThemAll2 import app
from flask import render_template, request, Blueprint
from BeatThemAll2.queries import get_pokemons_you_can_beat, get_sport_stats
import re

Index = Blueprint('Index', __name__)

@Index.route("/", methods=["GET", "POST"])
def index():
    sport_stats = None
    pokemons_you_can_beat = []
    if request.method == "POST":
        sport = request.form["sport"]
        if not re.match(r"[A-Z][a-z]+(:\s[A-Z][a-z]+)*", sport):
            sport = " ".join(word.capitalize() for word in sport.split())
        print(f"Searching for sport: {sport}")
        sport_stats = get_sport_stats(sport)
        if sport_stats:
            print(f"Found stats: {sport_stats}")
            pokemons_you_can_beat = get_pokemons_you_can_beat(sport_stats)
        else:
            print("No stats found.")
    percentage_beatable = (len(pokemons_you_can_beat) / 898) * 100
    return render_template(
        "index.html",
        sport_stats=sport_stats,
        pokemons_you_can_beat=pokemons_you_can_beat,
        percentage_beatable=percentage_beatable,
    )
