(SELECT 'book', 'price', 'rating' FROM books)
UNION
SELECT * FROM books
INTO OUTFILE 'books_sql.csv' 
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
