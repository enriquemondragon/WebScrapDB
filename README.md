# WebScrapDB

**Web scraping and SQL database management workflow.**

## Workflow
- Download the webpage(s) locally with the [scripts](https://github.com/enriquemondragon/WebScrapDB/tree/main/HTML). e.g:
```
    $ chmod +x getHTMLone.sh
    $ ./getHTMLone.sh
```

- Create the virtual environment with the corresponding requirements and a [Scrapy](https://scrapy.org/) project along with a spider:
```
    $ chmod +x ScrapyProjSetup.sh
    $ ./ScrapyProjSetup.sh
```
In this project the spider [book](bookstore/bookstore/spiders/book.py) extracts name, price and rating of books provided in a bookstore's webpage.

- Extract relevant information using XPath with the spider and saves it in a (.csv) file:
```
    $ chmod +x RunSpider.sh
    $ ./RunSpider.sh
```
- Once with the relevant information saved in a (.csv) file we can load it with MySQL and manipulate it. Here are some sample [queries]
(https://github.com/enriquemondragon/WebScrapDB/tree/main/sql_scripts).

--------
## Author
Name: Enrique Mondragon Estrada

Mail: emondra99@gmail.com

--------
## Sources
This project was inspired by the course:

- Deza, A., Gift, N. B., Behrman, K. (n.d.). *Scripting with Python and SQL for Data Engineering*. Coursera. https://www.coursera.org/learn/scripting-with-python-sql-for-data-engineering-duke
