import scrapy
import os
import pandas as pd

dir = os.environ['BOOKS']
url =[]
print('Searching webpages in: ', dir)
for root, dirs, files in os.walk(dir):
    for file in files:
        if file.endswith('.html'):
            url.append(dir + '/' + file)
print('Webpages are: ', url)

class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['books.toscrape.com']
    #start_urls = ['http://books.toscrape.com/catalogue/category/books_1/index.html']
    
    start_urls = [f'file://{url[0]}']

    def parse(self, response):
        # Find book names
        names = []
        books=response.xpath('//article').xpath('div')
        for item in range(len(books.xpath('a').extract())):
            b=books.xpath('a')[item].extract()
            start=b.find('alt="')
            end=b.find(' class')
            print(books.xpath('a')[item].extract()[start+5:end-1])
            names.append(books.xpath('a')[item].extract()[start+5:end-1])

        # Find prices
        price = []
        prices=response.xpath('//article').xpath('div')
        len(prices.xpath('p').extract()) # len is (2*number of books) prices are in even indeces
        for item in range(0,len(prices.xpath('p').extract()),2):
            p=prices.xpath('p')[item].extract()
            start=p.find('£')+1
            end=start+5
            print(prices.xpath('p').extract()[item][start:end])
            price.append(prices.xpath('p').extract()[item][start:end])
        
        # Find ratings
        rate = []
        ratings=response.xpath('//article')
        len(ratings.xpath('p'))
        for item in range(len(ratings.xpath('p'))):
            r=ratings.xpath('p')[item].extract()
            start=r.find('star-rating ')+12
            end=r.find('>\n')-1
            print(ratings.xpath('p').extract()[item][start:end])
            rate.append(ratings.xpath('p').extract()[item][start:end])
        
        info = {'book_names' : names,
                    'price' : price,
                    'rating' : rate}

        df = pd.DataFrame(info)
        print('df is: ', df)

        parent = os.path.split(dir)
        path = parent[0] + '/sql_scripts/' + 'books.csv'
        df.to_csv (path, index = False, header=True)
        print('saved!')