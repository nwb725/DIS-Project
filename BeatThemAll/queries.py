from BeatThemAll import db_cursor, conn
from BeatThemAll.forms import SportStatsForm


def search_sport(query):
    sql = """
    SELECT * FROM Sport_data
    WHERE SPORT= %s
    LIMIT 1
    """
    db_cursor.execute(sql, ("%" + query + "%",))
    sport = db_cursor.fetchone()
    return dict(sport) if sport else None


def get_sport_details(sport_name):
    sql = """
    SELECT * FROM Sports
    WHERE SPORT = %s
    LIMIT 1
    """
    db_cursor.execute(sql, (sport_name,))
    sport_details = db_cursor.fetchone()
    return dict(sport_details) if sport_details else None


def get_weaker_pokemon(sport_pk):
    sql = """"
    SELECT pokemon_name
    FROM Pokemons
    WHERE pokemon_speed < (
        SELECT speed
        FROM Sports
        WHERE sport_name = %s
    );
    """
    db_cursor.execute(sql, (sport_pk))
    conn.commit()


def get_pokemon_name_by_type(type1):
    sql = """
    SELECT * FROM Pokemons
    WHERE type1 = %s
    """
    db_cursor.execute(sql, (type1))
    conn.commit()


def get_pokemon_stats(pokemon_pk):
    sql = """
    SELECT * FROM Pokemons
    WHERE pokemon_name = %s
    """
    db_cursor.execute(sql, (pokemon_pk))
    conn.commit()


def get_fastest_pokemon():
    sql = """
    SELECT pokemon_name, pokemon_speed
    FROM Pokemons
    WHERE pokemon_speed = (
    SELECT MAX(pokemon_speed)
    FROM Pokemons
    LIMIT 1
    ); """
    db_cursor.execute(sql)
    conn.commit()


def get_sport_stats(sports_pk):
    sql = """
    SELECT * FROM Sports
    WHERE SPORT = %s
    """
    db_cursor.execute(sql, (sports_pk,))
    sport_details = db_cursor.fetchone()
    return dict(sport_details) if sport_details else None
