CREATE DATABASE IF NOT EXISTS alx_book_store;

USE alx_book_store;

CREATE TABLE Books (
    book_id PRIMARY KEY,
    title VARCHAR(130),
    author_id FOREIGN KEY REFERENCING Authors TABLE,
    price DOUBLE,
    publication_date DATE
);

CREATE TABLE Authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(215)
);

CREATE TABLE Customers (
    customer_id PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT
);

CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id FOREIGN KEY REFERENCING Customers TABLE,
    order_date DATE
)

CREATE TABLE Order_Details (
    orderdetail_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id FOREIGN KEY REFERENCING Orders TABLE,
    book_id FOREIGN KEY REFERENCING Books TABLE,
    quantity DOUBLE
)
