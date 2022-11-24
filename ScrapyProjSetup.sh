#!/bin/bash

source venv_webscrap/bin/activate;
scrapy startproject bookstore;
cd bookstore;
scrapy genspider book http://books.toscrape.com/;
