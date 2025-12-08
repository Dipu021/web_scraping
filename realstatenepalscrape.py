import requests
from parsel import Selector
import json

data = []

for i in range(1,2):
    url = f'https://www.realestateinnepal.com/category/top-listing/page/{i}/'
    r = requests.get(url)
    response = Selector(r.text)


    for list in response.xpath('//div/article'):
        title = list.xpath('.//span/h4[@class="mb-0"]/a/text()').get()
        img_url = list.xpath('.//a/figure/img/@data-src').get()
        if not img_url:
            img_url = list.xpath('.//a/figure/img/@src').get()
        location = list.xpath('.//span[@class="locationko text-white"]/text()').getall()
        location =location[2].strip() if len(location) > 2 else ''
        land = list.xpath('.//ul/li[1]/text()').get()
        if land:
            land = " ".join(land.split())
        bed = list.xpath('.//ul/li[2]/text()').get()
        car_park = list.xpath('.//ul/li[3]/text()').get()
        detailed_url = list.xpath('.//a/@href').get()
        price  = list.xpath('.//div/h4/text()').get()

        raw_data ={
            "Title:":title,
            "Price:":price,
            "Img_Url:":img_url,
            "Location:":location,
            "Land_Area:":land,
            "Avaiable_Beds:":bed,
            "Car_Park:":car_park,
            "Detailed_Url:":detailed_url
        }
        data.append(raw_data)

    print(f'page {i} complete')
    print(r.status_code)

with open("realestate_data_dipu.json","w",encoding="utf-8") as f: 
       json.dump(data,f,indent=4,ensure_ascii=False)

