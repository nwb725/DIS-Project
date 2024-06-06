import pandas as pd
import psycopg2

DB_HOST = "localhost"
DB_NAME = "BeatThemAll"
DB_USER = "postgres"
DB_PASS = "postgres"

sport_data = pd.read_csv("data/sport_data.csv")
pokemon_data = pd.read_csv("data/pokemon_data.csv")

conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)

cursor = conn.cursor()

cursor.execute(
    """
DROP TABLE IF EXISTS sports CASCADE;
    
CREATE TABLE IF NOT EXISTS sports (
    SPORT VARCHAR(50) PRIMARY KEY,
    s_speed INTEGER,
    strength INTEGER,
    durability INTEGER
)
"""
)

cursor.execute(
    """
DROP TABLE IF EXISTS pokemons CASCADE;
    
CREATE TABLE IF NOT EXISTS pokemons (
    POKEMON VARCHAR(50) PRIMARY KEY,
    attack INTEGER,
    defense INTEGER,
    p_speed INTEGER
)
"""
)


for _, row in sport_data.iterrows():
    cursor.execute(
        """
    INSERT INTO sports (SPORT, s_Speed, Strength, Durability) VALUES (%s, %s, %s, %s)
    ON CONFLICT (SPORT) DO NOTHING
    """,
        (row["SPORT"], row["Speed"], row["Strength"], row["Durability"]),
    )

for _, row in pokemon_data.iterrows():
    cursor.execute(
        """
    INSERT INTO pokemons (POKEMON, attack, defense, p_speed) VALUES (%s, %s, %s, %s)
    ON CONFLICT (POKEMON) DO NOTHING
    """,
        (row["name"], row["attack"], row["defense"], row["speed"]),
    )

conn.commit()
cursor.close()
conn.close()
