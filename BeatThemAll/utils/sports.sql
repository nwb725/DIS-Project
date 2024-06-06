BEGIN;

DROP TABLE IF EXISTS Sports CASCADE;

CREATE TABLE IF NOT EXISTS Sports(
    SPORT VARCHAR(50) PRIMARY KEY,
    strength FLOAT,
    speed FLOAT,
    durability FLOAT
);

COMMIT;