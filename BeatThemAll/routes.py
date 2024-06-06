from flask import flash, render_template, request, jsonify
from BeatThemAll.forms import SportStatsForm
from app import app
from queries import get_sport_stats, search_sport, get_sport_details


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/temp")
def index():
    return render_template("index.html")


@app.route('/sport-stats', methods=['GET', 'POST'])
def sport_stats():
    # Hvor får man dataen fra?!?!
    form = SportStatsForm()
    #if form.validate_on_submit():
    sport_name = form.sport_name.data
    print(sport_name)
        
    sport_details = get_sport_stats(sport_name)
    print("now")
    print(sport_details)
    return render_template('sport_stats.html', form=form, sport_details=None)


@app.route("/query_sport", methods=["POST"])
def query_sport():
    data = request.get_json()
    sport = data.get("sport", "")
    sport_details = get_sport_details(sport)
    return jsonify(sport_details)
