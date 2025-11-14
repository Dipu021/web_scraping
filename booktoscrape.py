import requests
from parsel import Selector
import json

def title(response):
    # for list in response.xpath('//li/article'):
         title=response.xpath('.//h3/a/text()').get()
         return title
        

def price(response):
    # for list in response.xpath('//li/article'):
         price = response.xpath('.//p[@class="price_color"]/text()').get()
         return price
      
        

def check_avaiablity(response):
    # for list in response.xpath('//li/article'):
        raw = response.xpath('.//p[@class="instock availability"]/text()').getall()
        clean =''.join(x.strip() for x in raw if x.strip())
        return clean


def image_url(response):
    # for list in response.xpath('//li/article'):
        url = response.xpath('.//img/@src').get()
        complete_url = "https://books.toscrape.com/" + url
        return complete_url


def rating(response):
    # for list in response.xpath('//li/article'):
        rate = response.xpath('.//p/@class').get().split(' ')[1]
        return rate
        

books = []

for i in range(1,51):
    r=requests.get(f'https://books.toscrape.com/catalogue/page-{i}.html')

    response=Selector(r.text)

    for item in response.xpath('//li/article'):
            books_element = {
                    'Title':title(item),
                    'Price':price(item),
                    'Availabilty':check_avaiablity(item),
                    'Rating':rating(item),
                    'URL':image_url(item)
            }
            books.append(books_element)


    print(f'page {i} complete')
    print(r.status_code)

with open("books.json","w",encoding="utf-8") as f: 
       json.dump(books,f,indent=4,ensure_ascii=False)