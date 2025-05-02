from fastapi import FastAPI, HTTPException
import psycopg2
from psycopg2 import Error
from transformers import pipeline
import requests
from datetime import datetime

app = FastAPI()

# Database connection
def get_db_connection():
    return psycopg2.connect(
        dbname="stocknews",
        user="postgres",
        password="Hockeystar44!",  # Your PostgreSQL password
        host="localhost",
        port="5432"
    )

# Sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

@app.get("/")
def read_root():
    return {"message": "Stock News App API"}

@app.get("/test-db")
def test_db():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1;")
        result = cursor.fetchone()
        conn.close()
        return {"status": "Database connected", "result": result[0]}
    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/news/fetch/{ticker}")
def fetch_news(ticker: str):
    api_key = "aef4aff009124d4b8839fdd55655eb7d"  # Your NewsAPI key
    url = f"https://newsapi.org/v2/everything?q={ticker}&apiKey={api_key}&language=en&sortBy=publishedAt"
    try:
        response = requests.get(url)
        response.raise_for_status()
        articles = response.json().get("articles", [])[:5]  # Limit to 5 articles

        conn = get_db_connection()
        cursor = conn.cursor()
        for article in articles:
            title = article.get("title", "")
            content = article.get("description", "") or article.get("content", "")[:500]
            published_date = article.get("publishedAt")
            source = article.get("source", {}).get("name", "Unknown")
            # Sentiment analysis
            sentiment = sentiment_analyzer(content)[0]
            sentiment_score = sentiment["score"] if sentiment["label"] == "POSITIVE" else -sentiment["score"]

            cursor.execute(
                """
                INSERT INTO news (title, content, published_date, source, ticker, sentiment_score)
                VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;
                """,
                (title, content, published_date, source, ticker.upper(), sentiment_score)
            )
        conn.commit()
        conn.close()
        return {"status": "News fetched and analyzed", "ticker": ticker, "articles": len(articles)}
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"News API error: {str(e)}")
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.get("/news/{ticker}")
def get_news(ticker: str):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT title, content, published_date, source, sentiment_score FROM news WHERE ticker = %s ORDER BY published_date DESC LIMIT 5;",
            (ticker.upper(),)
        )
        news = cursor.fetchall()
        conn.close()
        return {
            "ticker": ticker,
            "news": [
                {
                    "title": n[0],
                    "content": n[1],
                    "published_date": n[2],
                    "source": n[3],
                    "sentiment_score": n[4]
                } for n in news
            ]
        }
    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    