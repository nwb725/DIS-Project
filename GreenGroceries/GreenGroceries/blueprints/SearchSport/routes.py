from flask import render_template, request, Blueprint
from GreenGroceries.forms import (
    SearchSportForm
)
from GreenGroceries.queries import (
    get_weaker_pokemon,
    get_pokemon_name_by_type,
    get_pokemon_stats,
    get_fastest_pokemon,
    get_sport_stats,
)
Sport = Blueprint("sport", __name__)


@Sport.route("/sport", methods=["GET", "POST"])
def searchSport():
    form = SearchSportForm()
    if request.method=="POST":
        sport = get_sport_stats(
            sport_name=request.form.get("sport")
        )
    title = f'Sports!'
    return render_template(
        "pages/produce.html", produce=sport, form=form, title=title
    )
        