from flask import Flask, request, render_template
import psycopg2
import pandas as pd

app = Flask(__name__)

# Database connection parameters
DB_HOST = "localhost"
DB_NAME = "BeatThemAll"
DB_USER = "postgres"
DB_PASS = "postgres"


@app.route("/", methods=["GET", "POST"])
def index():
    sport_stats = None
    pokemons_you_can_beat = []
    if request.method == "POST":
        sport = request.form["sport"]
        print(f"Searching for sport: {sport}")
        sport_stats = get_sport_stats(sport)
        if sport_stats:
            print(f"Found stats: {sport_stats}")
            pokemons_you_can_beat = get_pokemons_you_can_beat(sport_stats)
        else:
            print("No stats found.")
    return render_template(
        "index.html",
        sport_stats=sport_stats,
        pokemons_you_can_beat=pokemons_you_can_beat,
    )


def get_sport_stats(sport):
    try:
        connection = psycopg2.connect(
            host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS
        )
        cursor = connection.cursor()
        query = "SELECT s_speed, strength, durability FROM sports WHERE SPORT = %s"
        cursor.execute(query, (sport,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result:
            return {"speed": result[0], "strength": result[1], "durability": result[2]}
        else:
            return None
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None


def get_pokemons_you_can_beat(sport_stats):
    try:
        connection = psycopg2.connect(
            host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS
        )
        cursor = connection.cursor()
        query = "SELECT p_speed, attack, defense, POKEMON FROM pokemons"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        connection.close()

        pokemons_you_can_beat = []
        for result in results:
            p_speed, attack, defense, pokemon_name = result
            conditions_met = sum(
                [
                    sport_stats["speed"] > p_speed,
                    sport_stats["strength"] > attack,
                    sport_stats["durability"] > defense,
                ]
            )
            if conditions_met >= 2:
                pokemons_you_can_beat.append(pokemon_name)
        for p in pokemons_you_can_beat:
            print(p)
        return pokemons_you_can_beat
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []


if __name__ == "__main__":
    app.run(debug=True)
