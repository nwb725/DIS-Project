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
    if request.method == "POST":
        sport = request.form["sport"]
        print(f"Searching for sport: {sport}")  # Debugging line
        sport_stats = get_sport_stats(sport)
        if sport_stats:
            print(f"Found stats: {sport_stats}")  # Debugging line
        else:
            print("No stats found.")  # Debugging line
    return render_template("index.html", sport_stats=sport_stats)


def get_sport_stats(sport):
    try:
        connection = psycopg2.connect(
            host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS
        )
        cursor = connection.cursor()
        query = "SELECT speed, strength, durability FROM sports WHERE SPORT = %s"
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


if __name__ == "__main__":
    app.run(debug=True)
