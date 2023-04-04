CREATE TABLE IF NOT EXISTS tweets(
    datetime DATE NOT NULL,
    username VARCHAR(200) NOT NULL,
    text TEXT,
    source VARCHAR(200),
    location VARCHAR(200)
);
