CREATE DATABASE IF NOT EXISTS shopnova_ai;
USE shopnova_ai;

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    category VARCHAR(80) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    description TEXT NOT NULL,
    image TEXT
);

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    email VARCHAR(190) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NULL,
    total DECIMAL(10,2) NOT NULL,
    status VARCHAR(40) NOT NULL DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    review_text TEXT NOT NULL,
    sentiment VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

INSERT INTO products (name, category, price, description, image)
SELECT 'Nova Wireless Headphones', 'Electronics', 1499.00, 'Comfortable wireless headphones with deep bass for study, travel and daily use.', 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=700'
WHERE NOT EXISTS (SELECT 1 FROM products WHERE name = 'Nova Wireless Headphones');
INSERT INTO products (name, category, price, description, image)
SELECT 'Everyday Running Shoes', 'Fashion', 1899.00, 'Lightweight running shoes with cushioned support for walking, college and workouts.', 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=700'
WHERE NOT EXISTS (SELECT 1 FROM products WHERE name = 'Everyday Running Shoes');
INSERT INTO products (name, category, price, description, image)
SELECT 'Minimal Smart Watch', 'Electronics', 2499.00, 'Modern smartwatch with activity tracking and a clean everyday design.', 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=700'
WHERE NOT EXISTS (SELECT 1 FROM products WHERE name = 'Minimal Smart Watch');
INSERT INTO products (name, category, price, description, image)
SELECT 'Urban Travel Backpack', 'Accessories', 999.00, 'Durable backpack with laptop storage for college, office and weekend travel.', 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=700'
WHERE NOT EXISTS (SELECT 1 FROM products WHERE name = 'Urban Travel Backpack');
INSERT INTO products (name, category, price, description, image)
SELECT 'Studio Bluetooth Speaker', 'Electronics', 1299.00, 'Portable Bluetooth speaker for music at home, outdoors and small gatherings.', 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=700'
WHERE NOT EXISTS (SELECT 1 FROM products WHERE name = 'Studio Bluetooth Speaker');
INSERT INTO products (name, category, price, description, image)
SELECT 'Classic Everyday T-Shirt', 'Fashion', 499.00, 'Soft cotton basic t-shirt designed for comfortable everyday wear.', 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=700'
WHERE NOT EXISTS (SELECT 1 FROM products WHERE name = 'Classic Everyday T-Shirt');
