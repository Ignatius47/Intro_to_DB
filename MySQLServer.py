CREATE DATABASE IF NOT EXISTS alx_book_store;

USE alx_book_store;

import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Red!Fox27#explos",
        database="library_db"
    )
    if connection.is_connected():
        print("Connected to the database")
        return connection
    
def Books(title, author_id, price, publication_date):
    connection = create_connection()
    cursor = connection.cursor()
    book_query = "INSERT INTO Books (title, author_id, price, publication_date) VALUES (%s, %s, %s, %s)"
    values = ("The ALX champ", "$20", "12/08/2024")
    print(book_query, values)
    cursor.close()
    connection.close()

def Authors(author_id, author_name):
    connection = create_connection()
    cursor = connection.cursor()
    author_query = "INSERT INTO Authors (author_id, author_name) (VALUES %s, %s)"
    values = ("Ignatius")
    print(author_query, values)
    cursor.close()
    connection.close()

def Customers(customer_id, customer_name, email, address):
    connection = create_connection()
    cursor = connection.cursor()
    customer_query = "INSERT INTO Customers (customer_id, customer_name, email, address) (VALUES %s, %s, %s, %s)"
    values = ("Dickens", "dick@gmail.com", "FC2435")
    print(customer_query, values)
    cursor.close()
    connection.close()

def Orders(order_id, customer_id, order_date):
    connection = create_connection()
    cursor = connection.cursor()
    order_query = "INSERT INTO Orders (order_id, customer_id, order_date) (VALUES %s, %s, %s)"
    values = ("12/08/2024")
    print(order_query, values)
    cursor.close()
    connection.close()

def Order_details(order_detail_id, order_id, book_id, quantity):
    connection = create_connection()
    cursor = connection.cursor()
    details_query = "INSERT INTO Order_details (order_detail_id, order_id, book_id, quantity) (VALUES %s, %s, %s, %s)"
    values = ("500kg")
    print(details_query, values)
    cursor.close()
    connection.close() 
