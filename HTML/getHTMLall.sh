#!/bin/bash

pages=5; # Select number of pages

for ((page=1; page<=$pages; page++))
do
    echo $page
    wget http://books.toscrape.com/catalogue/category/books_1/page-"$page".html;
done

BOOKS=`pwd`;
export BOOKS;
