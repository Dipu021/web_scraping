import scrapy
import json


class MyntraProductSpider(scrapy.Spider):
    name = "myntra_product"
    allowed_domains = ["myntra.com"]
    start_urls = ["https://myntra.com"]

    def start_requests(self):
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'if-none-match': 'W/"6d92d-iF4QIKHXXWotnIlxjQuJAoaRSfU"',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Not_A Brand";v="99", "Chromium";v="142"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
        }
        
        yield scrapy.Request('https://www.myntra.com/jeans/levis/levis-men-511-slim-fit-stretchable-jeans/25756776/buy', callback=self.parse, headers=headers)

    def parse(self, response):
        json_str = response.xpath('//script[@type="application/ld+json"]/text()').getall()

        for block in json_str:
            try:
                data = json.loads(block)
            except:
                continue

            if data.get("@type") == "Product":  
                product = {
                    "Title": data.get("name"),
                    "Image_url": data.get("image"),
                    "Price": data.get("offers", {}).get("price"),
                    "Availability": data.get("offers", {}).get("availability"),
                    "Brand": data.get("brand", {}).get("name")
                }
                yield product
                break    



        