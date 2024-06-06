import psycopg2, os
from BeatThemAll2.load_data import DB_HOST, DB_NAME, DB_USER, DB_PASS

POKEMON_IMAGES_DIR = "static/pokemon_images"


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
                image_filename = pokemon_name.lower() + ".png"
                if os.path.exists(os.path.join(POKEMON_IMAGES_DIR, image_filename)):
                    pokemons_you_can_beat.append(
                        {
                            "name": pokemon_name,
                            "speed": p_speed,
                            "attack": attack,
                            "defense": defense,
                        }
                    )
        return pokemons_you_can_beat
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []
