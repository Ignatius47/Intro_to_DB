SELECT Books 
FROM information_schema.tables 
WHERE table_schema = 'alx_book_store';

SELECT Authors
FROM information_schema.tables
WHERE table_schema = 'alx_book_store';

SELECT Customers
FROM information_schema.tables
WHERE table_schema = 'alx_book_store';

SELECT Orders
FROM information_schema.tables
WHERE table_schema = 'alx_book_store';

SELECT Order_Details
FROM information_schema.tables
WHERE table_schema = 'alx_book_store';