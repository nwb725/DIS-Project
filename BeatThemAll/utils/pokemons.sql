BEGIN;

DROP TABLE IF EXISTS Pokemon CASCADE;

CREATE TABLE IF NOT EXISTS Pokemon(
    pokemon_name varchar(50) PRIMARY KEY,
    type1 varchar(50),
    pokemon_attack float,
    pokemon_defence float,
    pokemon_speed float
);

COMMIT;

