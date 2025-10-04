-- SQL script to insert sample data

-- Customers Table
INSERT INTO customers (customer_id, name, email, join_date)
VALUES
(1, 'Alice Johnson', 'alice@example.com', '2024-01-15'),
(2, 'Bob Smith', 'bob@example.com', '2024-02-10'),
(3, 'Charlie Brown', 'charlie@example.com', '2024-02-28'),
(4, 'Diana Prince', 'diana@example.com', '2024-03-05'),
(5, 'Ethan Hunt', 'ethan@example.com', '2024-03-20'),
(6, 'Fiona Adams', 'fiona@example.com', '2024-04-01'),
(7, 'George Miller', 'george@example.com', '2024-04-10');

-- Products Table
INSERT INTO products (product_id, product_name, category, price)
VALUES
(1, 'Coca-Cola', 'Drinks', 1.50),
(2, 'Bread', 'Bakery', 2.00),
(3, 'Milk', 'Dairy', 1.20),
(4, 'Eggs (Dozen)', 'Dairy', 2.50),
(5, 'Chocolate Bar', 'Snacks', 1.00);

-- Orders Table
INSERT INTO orders (order_id, customer_id, product_id, quantity, order_date)
VALUES
(1, 1, 1, 2, '2024-04-12'),  
(2, 3, 4, 1, '2024-04-13'),  
(3, 5, 2, 3, '2024-04-14');  


