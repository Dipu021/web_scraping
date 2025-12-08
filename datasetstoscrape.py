import requests
# from parsel import Selector
import json

url = 'https://opendatanepal.com/api/trpc/dataset.search,organization.list,group.list,dataset.search?batch=1&input={"0":{"json":{"query":"","sort":"score desc, metadata_modified desc","rows":10,"start":0,"groups":[],"orgs":[],"tags":[],"resFormat":[],"facetsFields":["organization","tags","groups","res_format"]}'
def main():
    r = requests.get(url,timeout=8)
    r.raise_for_status()
    text = r.text
    with open('json_data.json',"w",encoding='utf-8') as f:
     f.write(r.text)
    data = json.loads(text)
    items = (
        data[1]
        .get("result", {})
        .get("data", {})
        .get("json", [])
    )
    return items

    # print(data)

if __name__ == '__main__':
    items = main()

for item in items:
   title = item.get('display_name')
   print(title)

   

# import requests
# import json

# new_url = 'https://opendatanepal.com/api/trpc/dataset.search,organization.list,group.list,dataset.search?batch=1&input={"0":{"json":{"query":"","sort":"score desc, metadata_modified desc","rows":10,"start":0,"groups":[],"orgs":[],"tags":[],"resFormat":[],"facetsFields":["organization","tags","groups","res_format"]}}'

# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0"
# }

# r = requests.get(new_url, headers=headers, timeout=5)
# r.raise_for_status()

# text = r.text


# with open('open.json', 'w', encoding='utf-8') as f:
#     f.write(text)

# data = json.loads(text)


# policies =data[1].get("result").get("data").get("json")

# for project in policies :
#     title = project.get("title")
#     print("title:", title)