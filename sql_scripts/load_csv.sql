LOAD DATA LOCAL INFILE 'books.csv' INTO TABLE books
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'
(@book_names,@price,@rating) set book=@book_names, price=@price, rating=@rating
