from app import db_cursor


def search_sport(query):
    sql = """
    SELECT * FROM sports
    WHERE SPORT ILIKE %s
    LIMIT 1
    """
    db_cursor.execute(sql, ("%" + query + "%",))
    sport = db_cursor.fetchone()
    return dict(sport) if sport else None


def get_sport_details(sport_name):
    sql = """
    SELECT * FROM sports
    WHERE SPORT = %s
    LIMIT 1
    """
    db_cursor.execute(sql, (sport_name,))
    sport_details = db_cursor.fetchone()
    return dict(sport_details) if sport_details else None
