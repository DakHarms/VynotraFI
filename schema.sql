CREATE TABLE news (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    content TEXT,
    published_date TIMESTAMP,
    source VARCHAR(100),
    ticker VARCHAR(10),
    sentiment_score FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);