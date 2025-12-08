import scrapy
import json

class HariSpider(scrapy.Spider):
    name = "hari"
    allowed_domains = ["jbhifi.com.au", "vtvkm5urpx-1.algolianet.com"]
    start_urls = ["https://jbhifi.com.au"]

    def start_requests(self):
         

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0',
                'Accept': 'application/json',
                'Accept-Language': 'en-US,en;q=0.5',
                # 'Accept-Encoding': 'gzip, deflate, br, zstd',
                'content-type': 'application/json',
                'Origin': 'https://www.jbhifi.com.au',
                'Connection': 'keep-alive',
                'Referer': 'https://www.jbhifi.com.au/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'cross-site',
            }
            data = '{"requests":[{"indexName":"shopify_products_families","analyticsTags":["Desktop","Firefox","Windows","Asia","Kathmandu","perks_no","search"],"clickAnalytics":true,"distinct":true,"facets":["banner_tags.label","facets.Artist","facets.Brand","facets.Category","facets.Price","facets.Sold by","isMarketplace","onPromotion"],"filters":"(price > 0 AND product_published = 1 AND availability.displayProduct = 1)","highlightPostTag":"__/ais-highlight__","highlightPreTag":"__ais-highlight__","hitsPerPage":36,"maxValuesPerFacet":100,"page":0,"query":"laptop","userToken":"anonymous-3ff60f75-8436-4f85-b3c2-13da4a2d5ed3"},{"indexName":"shopify_products_families","analyticsTags":["Desktop","Firefox","Windows","Asia","Kathmandu","perks_no","search"],"clickAnalytics":true,"distinct":true,"facets":["banner_tags.label","facets.Artist","facets.Brand","facets.Category","facets.Price","facets.Sold by","isMarketplace","onPromotion"],"filters":"onPromotion:true AND (price > 0 AND product_published = 1 AND availability.displayProduct = 1)","highlightPostTag":"__/ais-highlight__","highlightPreTag":"__ais-highlight__","hitsPerPage":36,"maxValuesPerFacet":100,"page":0,"query":"laptop","userToken":"anonymous-3ff60f75-8436-4f85-b3c2-13da4a2d5ed3"},{"indexName":"shopify_products_families","analyticsTags":["Desktop","Firefox","Windows","Asia","Kathmandu","perks_no","search"],"clickAnalytics":true,"distinct":true,"facets":["banner_tags.label","facets.Artist","facets.Brand","facets.Category","facets.Price","facets.Sold by","isMarketplace","onPromotion"],"filters":"banner_tags.label:Clearance AND (price > 0 AND product_published = 1 AND availability.displayProduct = 1)","highlightPostTag":"__/ais-highlight__","highlightPreTag":"__ais-highlight__","hitsPerPage":36,"maxValuesPerFacet":100,"page":0,"query":"laptop","userToken":"anonymous-3ff60f75-8436-4f85-b3c2-13da4a2d5ed3"}]}'

            yield scrapy.Request('https://vtvkm5urpx-1.algolianet.com/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(5.41.0)%3B%20Lite%20(5.41.0)%3B%20Browser%3B%20instantsearch.js%20(4.80.0)%3B%20react%20(18.3.1)%3B%20react-instantsearch%20(7.16.3)%3B%20react-instantsearch-core%20(7.16.3)%3B%20JS%20Helper%20(3.26.0)&x-algolia-api-key=1d989f0839a992bbece9099e1b091f07&x-algolia-application-id=VTVKM5URPX',method="POST", callback=self.parse,headers=headers,body=json.dumps(data))


    def parse(self, response):
        data = response.json()  # Parse the JSON response
        
        # Ensure that 'results' is accessed properly
        results = data.get("results", [])
        if not results:
            self.log("No results found.")
            return
        
        # Access 'hits' from each result
        for result in results:
            hits = result.get("hits", [])
            for text in hits:
                title = text.get("title")
                if title:  # Only yield if title exists
                    yield {
                        "Title": title
                    }
