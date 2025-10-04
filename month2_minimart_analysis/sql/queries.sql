-- SQL queries for retrieving insights

-- 1. Retrieve all customers
SELECT * FROM customers;

-- 2. Retrieve all products
SELECT * FROM products;

-- 3. Filter products by category (e.g., Drinks)
SELECT * FROM products
WHERE category = 'Drinks';

-- 4. List all orders sorted by date (most recent first)
SELECT * FROM orders
ORDER BY order_date DESC;

-- 5. Find customers who joined after March 1, 2024
SELECT * FROM customers
WHERE join_date > '2024-03-01';

-- 6. Count total number of orders
SELECT COUNT(*) AS total_orders
FROM orders;

-- 7. Calculate revenue per product (price × quantity)
SELECT p.product_name,
       SUM(p.price * o.quantity) AS revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name;

-- 8. Find the average product price
SELECT AVG(price) AS average_price
FROM products;

-- 9. Find the most expensive product
SELECT product_name, price
FROM products
ORDER BY price DESC
LIMIT 1;

-- 10. Count how many customers have placed orders
SELECT COUNT(DISTINCT customer_id) AS active_customers
FROM orders;

-- 11. Get detailed order info (customer + product + quantity + date)
SELECT o.order_id, c.name AS customer, p.product_name, 
       o.quantity, o.order_date
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN products p ON o.product_id = p.product_id;

-- 12. List all customers and their orders (include customers with no orders)
SELECT c.name, o.order_id, o.order_date
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;

-- 13. Show all products, even if they haven’t been ordered
SELECT p.product_name, o.order_id
FROM products p
LEFT JOIN orders o ON p.product_id = o.product_id;

-- 14. Find total revenue per customer
SELECT c.name,
       SUM(p.price * o.quantity) AS total_spent
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
LEFT JOIN products p ON o.product_id = p.product_id
GROUP BY c.name;

-- 15. Find the most popular product (highest quantity sold)
SELECT p.product_name,
       SUM(o.quantity) AS total_sold
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC
LIMIT 1;
