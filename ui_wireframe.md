# Vynotra FI UI Wireframe (May 2025)

## Objective
Design a simple web interface for the Vynotra FI MVP, allowing users to input a stock ticker and view news articles with sentiment scores.

## Layout
### Header
- **Title**: "Vynotra FI - Global Financial Intelligence"
- **Description**: A short tagline (e.g., "Stay informed with real-time financial news and insights.")

### Main Section
- **Ticker Input Form**:
  - A text input field labeled "Enter Stock Ticker (e.g., AAPL)".
  - A "Fetch News" button to submit the ticker.
- **News Display Area**:
  - A list of up to 5 news articles (fetched via the `/news/{ticker}` API endpoint).
  - For each article:
    - Title (bold)
    - Source and Published Date (e.g., "CNN - 2025-05-08")
    - Content (short snippet, e.g., first 100 characters)
    - Sentiment Score (e.g., "Positive: 0.85" or "Negative: -0.72")
  - If no articles are found, display a message: "No news found for this ticker."

### Footer
- **Copyright**: "© 2025 Vynotra Inc. All rights reserved."
- **Contact Link**: A link to "mailto:info@vynotrafi.com" (to be updated once email is set up in Phase 3).

## Next Steps
- Implement the UI in React by modifying `src/App.js` and `src/App.css`.
- Add API calls to fetch news using the `/news/{ticker}` endpoint.
- Style the UI with basic CSS for a clean, professional look.