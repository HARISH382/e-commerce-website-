from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
from database import get_connection
from ml.recommender import recommend_products
from ml.sentiment import analyze_sentiment

app = Flask(__name__)
app.secret_key = "change-this-secret-key-before-deployment"

SAMPLE_PRODUCTS = [
    {"id": 1, "name": "Nova Wireless Headphones", "category": "Electronics", "price": 1499.00, "description": "Comfortable wireless headphones with deep bass for study, travel and daily use.", "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=700"},
    {"id": 2, "name": "Everyday Running Shoes", "category": "Fashion", "price": 1899.00, "description": "Lightweight running shoes with cushioned support for walking, college and workouts.", "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=700"},
    {"id": 3, "name": "Minimal Smart Watch", "category": "Electronics", "price": 2499.00, "description": "Modern smartwatch with activity tracking and a clean everyday design.", "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=700"},
    {"id": 4, "name": "Urban Travel Backpack", "category": "Accessories", "price": 999.00, "description": "Durable backpack with laptop storage for college, office and weekend travel.", "image": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=700"},
    {"id": 5, "name": "Studio Bluetooth Speaker", "category": "Electronics", "price": 1299.00, "description": "Portable Bluetooth speaker for music at home, outdoors and small gatherings.", "image": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=700"},
    {"id": 6, "name": "Classic Everyday T-Shirt", "category": "Fashion", "price": 499.00, "description": "Soft cotton basic t-shirt designed for comfortable everyday wear.", "image": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=700"},
]

def load_products():
    """Use MySQL products when configured; otherwise show demo products."""
    try:
        conn = get_connection()
        if conn is None:
            return SAMPLE_PRODUCTS
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, name, category, price, description, image FROM products ORDER BY id DESC")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows or SAMPLE_PRODUCTS
    except Exception:
        # Keeps the demo usable before MySQL has been configured.
        return SAMPLE_PRODUCTS

@app.route("/")
def index():
    products = load_products()
    return render_template("index.html", products=products[:6], recommendations=products[:4])

@app.route("/products")
def products():
    all_products = load_products()
    q = request.args.get("q", "").strip()
    category = request.args.get("category", "").strip()
    if q:
        all_products = recommend_products(q, all_products, limit=len(all_products))
    if category:
        all_products = [p for p in all_products if p["category"].lower() == category.lower()]
    categories = sorted({p["category"] for p in load_products()})
    return render_template("products.html", products=all_products, categories=categories, q=q, selected_category=category)

@app.route("/product/<int:product_id>")
def product_detail(product_id):
    product = next((p for p in load_products() if int(p["id"]) == product_id), None)
    if not product:
        return "Product not found", 404
    related = recommend_products(product["description"], [p for p in load_products() if int(p["id"]) != product_id], limit=3)
    return render_template("product_detail.html", product=product, recommendations=related)

@app.route("/cart")
def cart():
    cart_items = session.get("cart", {})
    products = load_products()
    items, total = [], 0
    for product in products:
        quantity = int(cart_items.get(str(product["id"]), 0))
        if quantity:
            line_total = float(product["price"]) * quantity
            items.append({"product": product, "quantity": quantity, "line_total": line_total})
            total += line_total
    return render_template("cart.html", items=items, total=total)

@app.post("/cart/add/<int:product_id>")
def add_to_cart(product_id):
    valid_ids = {int(p["id"]) for p in load_products()}
    if product_id in valid_ids:
        cart_items = session.get("cart", {})
        key = str(product_id)
        cart_items[key] = int(cart_items.get(key, 0)) + 1
        session["cart"] = cart_items
        flash("Added to your cart.")
    return redirect(request.referrer or url_for("products"))

@app.post("/cart/remove/<int:product_id>")
def remove_from_cart(product_id):
    cart_items = session.get("cart", {})
    cart_items.pop(str(product_id), None)
    session["cart"] = cart_items
    return redirect(url_for("cart"))

@app.route("/assistant", methods=["GET", "POST"])
def assistant():
    answer = None
    if request.method == "POST":
        query = request.form.get("message", "").strip()
        found = recommend_products(query, load_products(), limit=3)
        if found:
            names = ", ".join(p["name"] for p in found)
            answer = f"Based on your request, you may like: {names}. Compare the prices and descriptions before choosing."
        else:
            answer = "I couldn't find a close match. Try a category such as electronics, fashion, shoes or backpacks."
    return render_template("chatbot.html", answer=answer)

@app.route("/review-analysis", methods=["GET", "POST"])
def review_analysis():
    review = ""
    result = None
    if request.method == "POST":
        review = request.form.get("review", "").strip()
        if review:
            result = analyze_sentiment(review)
    return render_template("review_analysis.html", review=review, result=result)

if __name__ == "__main__":
    app.run(debug=True)
