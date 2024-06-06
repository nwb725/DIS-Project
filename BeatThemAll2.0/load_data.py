import pandas as pd
import psycopg2

# Database connection parameters
DB_HOST = "localhost"
DB_NAME = "BeatThemAll"
DB_USER = "postgres"
DB_PASS = "postgres"

# Load CSV file
data = pd.read_csv("data/sport_data.csv")
print(data.columns)


# Create a connection to the database
conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)

# Create a cursor object
cursor = conn.cursor()

# Create table
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS sports (
    SPORT VARCHAR(50) PRIMARY KEY,
    speed INTEGER,
    strength INTEGER,
    durability INTEGER
)
"""
)

# Insert data into the table
for _, row in data.iterrows():
    cursor.execute(
        """
    INSERT INTO sports (SPORT, Speed, Strength, Durability) VALUES (%s, %s, %s, %s)
    ON CONFLICT (SPORT) DO NOTHING
    """,
        (row["SPORT"], row["Speed"], row["Strength"], row["Durability"]),
    )

# Commit the transaction and close the connection
conn.commit()
cursor.close()
conn.close()
