DROP TABLE IF EXISTS Sports CASCADE;
Create TABLE IF NOT EXISTS Sports(
    sport_name varchar(50) PRIMARY KEY,
    strength float,
    speed float,
    durabilit float
)