# Vynotra FI MVP Features (May 2025)

## Objective
Build a Minimum Viable Product (MVP) for Vynotra FI, a global financial intelligence app, to validate the concept with early users by November 2025 (Phase 3).

## Core Features
1. **Stock News Fetching**:
   - Fetch news articles for a given stock ticker using the NewsAPI (already implemented in main.py).
   - Display up to 5 recent articles with title, content, published date, source, and sentiment score.
2. **Sentiment Analysis**:
   - Perform sentiment analysis on news articles using the transformers library (already implemented in main.py).
   - Display a sentiment score for each article (positive/negative).
3. **Database Storage**:
   - Store fetched news articles in a PostgreSQL database (already implemented in main.py).
   - Include fields: title, content, published date, source, ticker, sentiment score.
4. **Basic API Endpoints**:
   - `/news/fetch/{ticker}`: Fetch and store news for a ticker (already implemented).
   - `/news/{ticker}`: Retrieve stored news for a ticker (already implemented).
   - `/`: Display branding message "Vynotra FI API - Global Financial Intelligence" (already implemented).
5. **User Interface (UI)**:
   - Build a simple web frontend to interact with the API.
   - Display a form to input a ticker and show fetched news articles with sentiment scores.
   - Use HTML/CSS/JavaScript (or a framework like React) for the frontend.

## Future Enhancements
- **Unique Username Feature**: As outlined in `feature_username.md`, implement personalized usernames tied to user progress and goals (target: August 2025, 100–500 users).

## Timeline
- Development Start: May 2025
- Target Completion: November 2025 (Phase 3)

## Next Steps
- Set up a frontend development environment (e.g., install Node.js, create a React app).
- Design a basic UI wireframe for the ticker input and news display.
- Connect the frontend to the existing API endpoints.