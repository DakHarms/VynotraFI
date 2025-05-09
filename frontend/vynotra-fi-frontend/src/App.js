import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [ticker, setTicker] = useState('');
  const [newsArticles, setNewsArticles] = useState([]);
  const [error, setError] = useState('');

  const fetchNews = async () => {
    try {
      // Replace with your FastAPI backend URL if different (e.g., if deployed)
      const response = await axios.get(`http://localhost:8000/news/${ticker}`);
      const articles = response.data.news;
      if (articles.length === 0) {
        setNewsArticles([]);
        setError('No news found for this ticker.');
      } else {
        setNewsArticles(articles);
        setError('');
      }
    } catch (err) {
      setNewsArticles([]);
      setError('Error fetching news. Please try again.');
      console.error(err);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (ticker.trim()) {
      fetchNews();
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Vynotra FI - Global Financial Intelligence</h1>
        <p>Stay informed with real-time financial news and insights.</p>
      </header>
      <main>
        <form onSubmit={handleSubmit} className="ticker-form">
          <label htmlFor="ticker">Enter Stock Ticker (e.g., AAPL):</label>
          <input
            type="text"
            id="ticker"
            value={ticker}
            onChange={(e) => setTicker(e.target.value.toUpperCase())}
            placeholder="AAPL"
          />
          <button type="submit">Fetch News</button>
        </form>
        {error && <p className="error">{error}</p>}
        <div className="news-list">
          {newsArticles.map((article, index) => (
            <div key={index} className="news-article">
              <h3>{article.title}</h3>
              <p className="article-meta">
                {article.source} - {new Date(article.published_date).toLocaleDateString()}
              </p>
              <p>{article.content.slice(0, 100)}...</p>
              <p className="sentiment">
                Sentiment: {article.sentiment_score > 0 ? 'Positive' : 'Negative'}: {Math.abs(article.sentiment_score).toFixed(2)}
              </p>
            </div>
          ))}
        </div>
      </main>
      <footer>
        <p>© 2025 Vynotra Inc. All rights reserved.</p>
        <p><a href="mailto:info@vynotrafi.com">Contact Us</a></p>
      </footer>
    </div>
  );
}

export default App;
