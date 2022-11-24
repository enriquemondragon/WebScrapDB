# WebScrapDB

**Web scraping and SQL database management workflow..**

## Workflow
- Download the webpage(s) locally with the ![scripts](https://github.com/enriquemondragon/WebScrapDB/tree/main/HTML). e.g:
```
    $ chmod +x getHTMLone.sh
    $ ./getHTMLone.sh
```

- Create the virtual environment with the corresponding requirements and a ![Scrapy](https://scrapy.org/) project along with a spider:
```
    $ chmod +x ScrapyProjSetup.sh
    $ ./ScrapyProjSetup.sh
```
In this project the spider ![book](bookstore/bookstore/spiders/book.py) extracts name, price and rating of books provided in a bookstore's webpage.

- Extract relevant information using XPath with the spider:
```
    $ chmod +x RunSpider.sh
    $ ./RunSpider.sh
```