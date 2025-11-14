import requests
from parsel import Selector
import json

quotes_array = []

base_url = "https://quotes.toscrape.com/"
page = 1
while True:
    url = f'{base_url}/page/{page}/'

    r= requests.get(url)
    response = Selector(r.text)

    quotes = response.xpath('//div[@class="quote"]')

    if not quotes:
        print("No more pages left.")
        break


    for quote in quotes:
        text = quote.xpath('.//span[@class="text"]/text()').get()
        author = quote.xpath('.//span/small[@class="author"]/text()').get()
        unorder_tags = quote.xpath('.//div/a[@class="tag"]/text()').getall()
        order_tags = unorder_tags.sort()
        author_links = quote.xpath('.//span/a/@href').get()
        author_details = "https://quotes.toscrape.com/"+author_links


        qou = {
             'Quotes':text,
             'Author':author,
             'Tags':order_tags,
             'Author Details':author_details
        }
        quotes_array.append(qou)
        

    print(f"{page} Completed")
    page+=1
    print(r.status_code)

with open("quotes.json","w",encoding="utf-8") as f:
       json.dump(quotes_array,f,indent=4,ensure_ascii=False)