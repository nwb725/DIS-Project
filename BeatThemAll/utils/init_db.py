import psycopg2
import os
import csv

from dotenv import load_dotenv

# from choices import df

load_dotenv()

if __name__ == "__main__":
    conn = psycopg2.connect(
        host="localhost",
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
    )
    with conn.cursor() as cur:
        # Run pokemons.sql
        with open("pokemons.sql") as db_file:
            cur.execute(db_file.read())

        # Run sports.sql
        with open("sports.sql") as db_file:
            cur.execute(db_file.read())

        # Read pokemon_data.csv
        with open("pokemon_data.csv", newline="") as csvfile:
            pokemon_data = csv.DictReader(csvfile)

        # Read toughestsport.csv
        with open("sport_data.csv", newline="") as csvfile:
            sport_data = csv.DictReader(csvfile)

        for pokemon in pokemon_data:
            cur.execute(
                """
                INSERT INTO Pokemon (pokemon_name, type1, pokemon_hp, pokemon_attack, pokemon_defence, pokemon_speed)
                VALUES (%s, %s, %s, %s, %s, %s);
                """,
                (
                    pokemon["pokemon_name"],
                    pokemon["type1"],
                    float(pokemon["pokemon_hp"]),
                    float(pokemon["pokemon_attack"]),
                    float(pokemon["pokemon_defence"]),
                    float(pokemon["pokemon_speed"]),
                ),
            )

        for value in sport_data:
            cur.execute(
                """
                INSERT INTO Sports (sport_name, strength, speed, durability)
                VALUES (%s, %s, %s, %s);
                """,
                (
                    value["sport_name"],
                    float(value["strength"]),
                    float(value["speed"]),
                    float(value["durability"]),
                ),
            )
