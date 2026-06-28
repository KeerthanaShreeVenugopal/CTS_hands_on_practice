-- Drop tables if they already exist
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS users;

-- Create Users table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Create Orders table
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    product_name VARCHAR(100) NOT NULL,
    amount DECIMAL(10,2) NOT NULL
);

-- Insert data into Users
INSERT INTO users (name, email)
VALUES
('Alice', 'alice@gmail.com'),
('Bob', 'bob@gmail.com'),
('Charlie', 'charlie@gmail.com'),
('David', 'david@gmail.com');

-- Insert data into Orders
INSERT INTO orders (user_id, product_name, amount)
VALUES
(1, 'Laptop', 1200.00),
(1, 'Mouse', 25.00),
(2, 'Keyboard', 75.00),
(NULL, 'Guest Book', 15.00);

----------------------------------------------------
-- INNER JOIN
-- Returns only matching records from both tables.
----------------------------------------------------

SELECT
    u.user_id,
    u.name,
    o.product_name,
    o.amount
FROM users AS u
INNER JOIN orders AS o
ON u.user_id = o.user_id;

----------------------------------------------------
-- LEFT JOIN
-- Returns all users and their orders (if any).
----------------------------------------------------

SELECT
    u.user_id,
    u.name,
    u.email,
    o.product_name,
    o.amount
FROM users AS u
LEFT JOIN orders AS o
ON u.user_id = o.user_id;

----------------------------------------------------
-- RIGHT JOIN
-- Returns all orders and their users (if any).
----------------------------------------------------

SELECT
    u.name,
    o.product_name,
    o.amount
FROM users AS u
RIGHT JOIN orders AS o
ON u.user_id = o.user_id;

----------------------------------------------------
-- FULL OUTER JOIN
-- Returns all users and all orders.
----------------------------------------------------

SELECT
    u.user_id,
    u.name,
    u.email,
    o.order_id,
    o.product_name,
    o.amount
FROM users AS u
FULL OUTER JOIN orders AS o
ON u.user_id = o.user_id;