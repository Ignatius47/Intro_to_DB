import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Red!Fox27#explos",
            database="library_db"
        )
        if connection.is_connected():
            print("Connected to the database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def Books(title, author_id, price, publication_date):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            book_query = "INSERT INTO Books (title, author_id, price, publication_date) VALUES (%s, %s, %s, %s)"
            values = (title, author_id, price, publication_date)
            cursor.execute(book_query, values)
            connection.commit()
            print("Book inserted successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

def Authors(author_id, author_name):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            author_query = "INSERT INTO Authors (author_id, author_name) VALUES (%s, %s)"
            values = (author_id, author_name)
            cursor.execute(author_query, values)
            connection.commit()
            print("Author inserted successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

def Customers(customer_id, customer_name, email, address):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            customer_query = "INSERT INTO Customers (customer_id, customer_name, email, address) VALUES (%s, %s, %s, %s)"
            values = (customer_id, customer_name, email, address)
            cursor.execute(customer_query, values)
            connection.commit()
            print("Customer inserted successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

def Orders(order_id, customer_id, order_date):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            order_query = "INSERT INTO Orders (order_id, customer_id, order_date) VALUES (%s, %s, %s)"
            values = (order_id, customer_id, order_date)
            cursor.execute(order_query, values)
            connection.commit()
            print("Order inserted successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

def Order_details(order_detail_id, order_id, book_id, quantity):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            details_query = "INSERT INTO Order_details (order_detail_id, order_id, book_id, quantity) VALUES (%s, %s, %s, %s)"
            values = (order_detail_id, order_id, book_id, quantity)
            cursor.execute(details_query, values)
            connection.commit()
            print("Order details inserted successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()
