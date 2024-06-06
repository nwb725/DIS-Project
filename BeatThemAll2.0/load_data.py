import pandas as pd
import psycopg2

# Database connection parameters
DB_HOST = "localhost"
DB_NAME = "BeatThemAll"
DB_USER = "postgres"
DB_PASS = "postgres"

# Load CSV file
sport_data = pd.read_csv("data/sport_data.csv")
pokemon_data = pd.read_csv("data/pokemon_data.csv")

# Create a connection to the database
conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)

# Create a cursor object
cursor = conn.cursor()

# Create sports table
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
# Create pokemons table
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


# Insert data into the table
for _, row in sport_data.iterrows():
    cursor.execute(
        """
    INSERT INTO sports (SPORT, s_Speed, Strength, Durability) VALUES (%s, %s, %s, %s)
    ON CONFLICT (SPORT) DO NOTHING
    """,
        (row["SPORT"], row["Speed"], row["Strength"], row["Durability"]),
    )

# Insert data into the table
for _, row in pokemon_data.iterrows():
    cursor.execute(
        """
    INSERT INTO pokemons (POKEMON, attack, defense, p_speed) VALUES (%s, %s, %s, %s)
    ON CONFLICT (POKEMON) DO NOTHING
    """,
        (row["name"], row["attack"], row["defense"], row["speed"]),
    )

# Commit the transaction and close the connection
conn.commit()
cursor.close()
conn.close()
