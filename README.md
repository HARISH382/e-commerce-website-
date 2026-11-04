# ShopNova AI — Smart E-Commerce Demo

A beginner-friendly portfolio starter combining a Flask e-commerce website with content-based product recommendations and review sentiment analysis.

## Features
- Responsive dark, neon-accented storefront
- Product catalog and category filter
- Product detail pages
- Session-based demo shopping cart
- TF-IDF + cosine-similarity product matching using scikit-learn
- Review sentiment demo using VADER
- Optional MySQL integration with sample data

## Requirements
- Python 3.10+
- VS Code
- MySQL Server (optional for the demo; sample products show without it)

## Run in VS Code (Windows)

1. Extract the ZIP and open the `shopnova-ai` folder in VS Code.
2. Open Terminal → New Terminal.
3. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, use Command Prompt:
   ```bat
   .venv\Scripts\activate.bat
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. (Optional) Configure MySQL:
   - Open MySQL Workbench or your MySQL terminal.
   - Run the contents of `schema.sql`.
   - Set your database password in the terminal before starting the app:

   PowerShell:
   ```powershell
   $env:DB_HOST="localhost"
   $env:DB_USER="root"
   $env:DB_PASSWORD="YOUR_MYSQL_PASSWORD"
   $env:DB_NAME="shopnova_ai"
   ```

   If MySQL is not configured, the app uses demo products in memory.

6. Start the Flask app:

   ```bash
   python app.py
   ```

7. Open this address in your browser: http://127.0.0.1:5000

## Test it
- Home page: `http://127.0.0.1:5000`
- Catalog: `http://127.0.0.1:5000/products`
- AI assistant: `http://127.0.0.1:5000/assistant`
- Review sentiment: `http://127.0.0.1:5000/review-analysis`
- Cart: `http://127.0.0.1:5000/cart`

## Important limitations
- This is a learning/demo project, not a production store.
- Checkout and payment processing are intentionally not implemented.
- Login, registration, persistent cart, order creation, admin management, CSRF protection and production-grade security are not implemented yet.
- Before deployment, replace `app.secret_key`, move secrets to environment variables, disable debug mode, validate inputs, and add security protections.
- The sample images load from Unsplash, so internet access is needed to see them.

## Resume description
**ShopNova AI — AI-Powered E-Commerce Recommendation Platform**  
Built a responsive e-commerce web application using Python Flask, HTML, CSS, JavaScript and MySQL. Implemented content-based product matching with TF-IDF and cosine similarity, plus customer review sentiment analysis using VADER. Developed product browsing, category filters, product detail pages and a session-based shopping cart.
