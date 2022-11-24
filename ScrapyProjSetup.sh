#!/bin/bash

python3 -m venv venv_webscrap
source venv_webscrap/bin/activate;
pip install requirements.txt;
scrapy startproject bookstore;
cd bookstore;
scrapy genspider book http://books.toscrape.com/;
