-- Setup the books database
CREATE DATABASE IF NOT EXISTS books;
USE books
CREATE TABLE books (
    book VARCHAR(255),
    price VARCHAR(255),
    rating VARCHAR(255),
)
