import requests
from parsel import Selector
import json

url = 'https://opendatanepal.com/api/trpc/dataset.search,organization.list,group.list,dataset.search?batch=1&input={"0":{"json":{"query":"","sort":"score desc, metadata_modified desc","rows":10,"start":0,"groups":[],"orgs":[],"tags":[],"resFormat":[],"facetsFields":["organization","tags","groups","res_format"]}},"1":{"json":null,"meta":{"values":["undefined"]}},"2":{"json":null,"meta":{"values":["undefined"]}},"3":{"json":{"query":"water","sort":"score desc, metadata_modified desc","rows":10,"start":0,"groups":[],"orgs":[],"tags":[],"resFormat":[],"facetsFields":["organization","tags","groups","res_format"]}}}'

headers ={
    'Accept': '*/*',
'Accept-Encoding':'gzip, deflate, br, zstd',
'Accept-Language':'en-US,en;q=0.5',
'Connection':'keep-alive',
'content-type':'application/json',
'Host':'opendatanepal.com',
'Priority':'u=4',
'Referer':'https://opendatanepal.com/datasets?q=water',
'Sec-Fetch-Dest':'empty',
'Sec-Fetch-Mode':'cors',
'Sec-Fetch-Site':'same-origin',
'trpc-accept':'application/jsonl',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0'
}

r=requests.get(url,headers=headers)
with open('abcd.json','w',encoding='utf-8') as f:
    f.write(r.text)
# response = Selector(r.text)
breakpoint()

# json_str= response.xpath('.//script[@id="__NEXT_DATA__"]/text()').get()
# joson_data = json.loads(json_str)
