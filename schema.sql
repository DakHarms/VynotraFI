CREATE TABLE news_articles (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    published_date TIMESTAMP NOT NULL,
    source TEXT NOT NULL,
    ticker TEXT NOT NULL,
    sentiment_score FLOAT
);