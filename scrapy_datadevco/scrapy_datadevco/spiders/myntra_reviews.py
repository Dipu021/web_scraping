# # import scrapy
# # import json
# # import re


# # class MyntrareviewsSpider(scrapy.Spider):
# #     name = "myntra_reviews"
# #     allowed_domains = ["myntra.com"]
# #     start_urls = ["https://myntra.com"]

# #     def __init__(self, urls:list =["https://www.myntra.com/jeans/levis/levis-men-511-slim-fit-stretchable-jeans/25756776/buy"]):
# #         self.urls = urls
# #         self.page = 1
# #     def start_requests(self):
# #         for url in self.urls:
# #             match = re.search(r'/(\d+)/buy', url)
# #             product_id = match.group(1)
             
# #             headers = {
# #                     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0',
# #                     'Accept': 'application/json',
# #                     'Accept-Language': 'en-US,en;q=0.5',
# #                     # 'Accept-Encoding': 'gzip, deflate, br, zstd',
# #                     'Referer': 'https://www.myntra.com/reviews/25756776',
# #                     'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjMwNjIwNzEiLCJhcCI6IjcxODQwNzY0MyIsImlkIjoiZGMxYzYwYWEwMjdkZDYzOCIsInRyIjoiMzg3ZjdhZTcxOTM4ZTI5MTk3NDI3YTNmZWU4ZWMzYzAiLCJ0aSI6MTc2Mzc0MDM0MjI0OSwidGsiOiI2Mjk1Mjg2In19',
# #                     'traceparent': '00-387f7ae71938e29197427a3fee8ec3c0-dc1c60aa027dd638-01',
# #                     'tracestate': '6295286@nr=0-1-3062071-718407643-dc1c60aa027dd638----1763740342249',
# #                     'X-myntraweb': 'Yes',
# #                     'X-Requested-With': 'browser',
# #                     'x-meta-app': 'deviceId=0c3a5531-a0e8-46e3-a976-09527c3c56c0;appFamily=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0;reqChannel=web;channel=web;',
# #                     'deviceId': '0c3a5531-a0e8-46e3-a976-09527c3c56c0',
# #                     'Content-Type': 'application/json',
# #                     'Sec-Fetch-Dest': 'empty',
# #                     'Sec-Fetch-Mode': 'cors',
# #                     'Sec-Fetch-Site': 'same-origin',
# #                     'Connection': 'keep-alive',
# #                     'Cookie': '_mxab_=config.bucket%3Dregular%3Bcoupon.cart.channelAware%3DchannelAware_Enabled%3Bcart.cartfiller.personalised%3Denabled; _pv=default; dp=d; at=ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pWmpReE9HSm1PVFF0WXpabU1TMHhNV1l3TFdJNVpHRXRNbUV6TXpoa09HWmxOVGRsSWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUzTnpreU9USXlPVE1zSW1semN5STZJa2xFUlVFaWZRLjBPU3dMcGdaTFNZVk9qVWNJQkZwd0pjT0U2NFJQZ0NqUUx0cTFjVGQweDQ=; microsessid=452; lt_timeout=1; lt_session=1; utrid=XxpuChZ9W3cTbWFCZ01AMCMxNzcxMjAxNjI4JDI%3D.880cc6b879317b30c9330094d0802e24; _d_id=0c3a5531-a0e8-46e3-a976-09527c3c56c0; user_session=mrs8m_Kq18AIcLaxzyus6A.E5uvaYFSBiGl_148E6GFK-3q41ogoRR5MxrVbUdRGVn_KvK6Wlbz5j_QeMMCVJ_mcCav568WSP9f8NOpEFIGFKRVSsgW1xsZasT2RznaQe6PodMc8bmNhxYLQG8676CB5iIoRO4I8bhSHQyt_ssoig.1763740293322.86400000.dOAm02OQLu8zig2O49WwhgPTzl4hI8mbJyWYb1bCrHE; _abck=F0737706841DDF8900746E7A4A80E1E7~0~YAAQ9MIRYBHbTaCaAQAAsikdpw5SxMtMgSi1hA+qd/gMd63yi1AwgMY9OnYqfBdf8jD6QSwykYvMJWsnTwBM2UBLZ6YMVH7gSDTaDRitk6jv+GqaerNTOiH2tE+j1K2TcD8RX6fBddsT2MfooepDSU42kownBbF4fgICOzQ3LiVOko8dVeKGc6kbPeya6wH4/rPVPO9aS2KP77Sk7d5KL+3NDMPD3BGVeRy/SWPHGaslLQ2EZue7POY2/Kax96cpSZELYEUKSR0q9wL8keXQXQpDPRTbhzEVt9HQENM3s9u/e1H3wyh+52oPx9D4KYrev4PVH/K8nWfSHM/t4aDAZAsnZ/EiOL3E2cavGjC4s5yWRhXw/tv8HO77gHz44OWoPLEfaKoPD7vv07J2Ict8z6D5i5HC3wdA06IVxkynNLfd6ce76vnUcFkkHgmyJygL/dZ/ifZyqMID7N/xaq5GCy5OualysGbrHd8yKpBOAb1y4i/mshISkJASq0uYX2xA468iBXxNRiGi5ugxwliMmHDUymN3dA+NJikfrHNUy27gz1nSfoRyjh3zDMq9467UmNo+kzEZOjP28iV5V7W5wEFRZEgJqBNAm6UZIQFntUE/oJjgwrgJy2a00m8gSZdV8gxs+Jdt5JqXsmmN2gs=~-1~-1~-1~AAQAAAAE%2f%2f%2f%2f%2f54S%2f7E0rTDcnp92QAMlrDuvxZS4XL2tFr8TtMt96TpsfXKFgZbxNjj0dC0htZAoltm%2fGOAHYphaaitCBBi3upE9IKfJyH3HMZ7K~-1; ak_bmsc=05F8AE1FC49980685C1B4F2BDF0211A0~000000000000000000000000000000~YAAQ9MIRYCICTqCaAQAAF6Mdpx3MrCIhSmuiWkDlPQJAYuWHnEP6YsbruaSdrpAEeWc8+oCh9aPdQ9uQzwa2r4hmsAcXV9zIP0uoK16UdTyfzWMbhZfzRBbANWk3FhBQOxyoyN5+1ly75f0tAU8b5RD0qp/KC864LWve0+8pxL2GGm6asj/oFclfAQ6pAokB9KkBjwwcB7Rb/SlHEdYwjkZs1ajTepPzc0nYS3R8tkPBJVepwY9Woz1aSshAa/fNMZHYbaGW5UKCcbj7xVImTdosVxas8mobX68EgLOAgn1rhqFN7XFk7Z/sa2497sErHEuGbz7jwF4K/x30W+4Yr3pTFwfwdtV4LXnXu04l9s31URll6x0t2vv3/s/OujmkaHrPiwTqjA4+CGq0llGynfTU2TUhxhFcJci7oI3Meief8s2/5fA5UuCa45jc8Y5qR3OMDDpNRetjCGnzkB1Pb6BWobuW8C/PmMiWo3XWsJ0spw1IPMB/Js0TXHNR2W0DEEu4O7nXUNNDejX28ZDq77e42V04Jp6Idw==; bm_sz=92FAA655BC2D2D5A9B3CD5A01BC450BC~YAAQ9MIRYPoOTqCaAQAADtcdpx0i1VYrSPjqZbPcYYnVJZ+N8FYhJbNsBqlxpLy8xDu6zXSSXZbBmO01o/4/22sc1vADzNoLxnwqgwkunDLCK8cxz14iL8tWSDJ26lHGJ8LuAKYXJj/6R2RG8iiGt7WRc1WsEtafJDtPudoR0Q2D0Adv4DPQI6txZDovuhARkETh+i8mC2wDyuFzSTxW8atx4oisWKi6boptOBU1vPdrTNH8CdWWpcfC9arjBRm1gXJBgCbqLjRiAPzOCUVXPyNUeNffzOF969///wt5rx/5gAiVE5tNIWjHAYz1aPE4V3RZBV/xeCnavwzsBegjXrWvKJa5RK35sVFgEbIdHN7zRmtWVez9XomzqSdn23CAiIYiMIa0otVuwa1kk5TiqJnWZye3R9PIklfd8DzTrdfiMjMlU2JBTrp3mPN/NxNNRONRS0yNEw0R2m+lSg==~3682374~3425592; mynt-eupv=1; _ma_session=%7B%22id%22%3A%2244a1061f-618c-462f-b073-bc31a902d9a9-0c3a5531-a0e8-46e3-a976-09527c3c56c0%22%2C%22referrer_url%22%3A%22%22%2C%22utm_medium%22%3A%22%22%2C%22utm_source%22%3A%22%22%2C%22utm_channel%22%3A%22direct%22%7D; _xsrf=QbnqUjTDFmrAxim9gmaYSkiU3vb2CpKf; bm_sv=0DA3D8CAAA6315FE30760A84180804A6~YAAQ9MIRYPkOTqCaAQAADtcdpx1sIYgN3QKtZuY774i4RsM13YyHHA0K1HSVMmIsHhEqU7Kx69LK8du3lu2GaTdKz2fiH/IAxnHL3jHjYKTXvHLum18k1TaTEbnm4sRoYrGpO83YIJWtS7FX6YNTJb3MXUA8YUDA1eVX1nIT5HxsbEen8Ape8OeajujKZyeR59WU2lEaZy9/tr7DFZM3AwOQRAXPRHWMDia5ECbSw3iEHCT1IvHo7T1CqvlHP7nZ4g==~1; x-mynt-pca=ilavX6XD2pe0VzPQHz5b2SuyladI59HBO12rejjvTT-fRFIgWaFp8ZVTLQbrmVfGZhnqmAhiGf3mCFYh0j_KQhHOS3UqVRqaAet-kmXfc_xYx4s7djk%3D; bm_mi=DBB41E66C05B61618173C62F90A312EA~YAAQ9MIRYNAATqCaAQAAdp4dpx2CZAN93pmV8synJMkzrwAXNi65pHJrg/WrEkGXquJFg7NJF4XBr3ARrvZCADiTRCF8KgkxfXwsZ4c7vY6Z59/aD/ot1bTCz5+lyQydXW1Z3yObIlcS14t/FDMkS/KnWfWKF6q5eeDfFpRNC+2R8Y/ZesABu/c/h1TfEpX+r+V0vpkHdvKSURqEu5eXYkFtH+1XAZAO6Y/xjJc+eJb7ZdRb0/k4VJLQYaTmnsF5H6zrIY4+ZhsEUByU53FE+kHBc8ZfC/9yNHhqoSVG6l0ELZWdiyxTqcjKiMxylcMRw8Indgj8a5QKphdC+Q==~1; _gcl_au=1.1.1062702089.1763740328; ak_RT="z=1&dm=myntra.com&si=27c961b2-0b55-47f7-bb06-6970c205fbfb&ss=mi91g9v9&sl=1&tt=23r&rl=1"; tvc_VID=1; _cs_ex=1; _cs_c=1; _fbp=fb.1.1763740329231.937948024260807897; _scid=7_szmJu5R1x2euN_zsPhxOEA_xpPBD9Z; _scid_r=7_szmJu5R1x2euN_zsPhxOEA_xpPBD9Z; _sctr=1%7C1763662500000',
# #                 }
            


# #             # params = {
# #             #             'size': '12',
# #             #             'sort': '0',
# #             #             'rating': '0',
# #             #             'page': self.page,
# #             #             'includeMetaData': 'true',
# #             # }
        

# #             yield scrapy.Request(f'https://www.myntra.com/gateway/v1/reviews/product/{product_id}', callback=self.parse,headers=headers)

# #     def parse(self, response):
# #         data = json.loads(response.text)

# #         reviews = data.get("data", {}).get("reviews", [])
# #         for review in reviews:
# #             yield {
# #                 "Id": review.get("style").get("id"),
# #                 "user": review.get("userName"),
# #                 "rating": review.get("style").get("userRating"),
# #                 "review_text": review.get("style").get("review"),
# #                 "created_on": review.get("updatedAt"),
# #                 "User_Image_url":review.get("images").get("url"),
# #             }


# import requests
# from parsel import Selector
# import json
# import re

# urls = ["https://www.myntra.com/gateway/v1/reviews/product/25756776"]
# reviews_data = []

# for url in urls:
#     headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0',
#             'Accept': 'application/json',
#             'Accept-Language': 'en-US,en;q=0.5',
#             'Referer': 'https://www.myntra.com/reviews/25756776',
#             'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjMwNjIwNzEiLCJhcCI6IjcxODQwNzY0MyIsImlkIjoiZGMxYzYwYWEwMjdkZDYzOCIsInRyIjoiMzg3ZjdhZTcxOTM4ZTI5MTk3NDI3YTNmZWU4ZWMzYzAiLCJ0aSI6MTc2Mzc0MDM0MjI0OSwidGsiOiI2Mjk1Mjg2In19',
#             'traceparent': '00-387f7ae71938e29197427a3fee8ec3c0-dc1c60aa027dd638-01',
#             'tracestate': '6295286@nr=0-1-3062071-718407643-dc1c60aa027dd638----1763740342249',
#             'X-myntraweb': 'Yes',
#             'X-Requested-With': 'browser',
#             'x-meta-app': 'deviceId=0c3a5531-a0e8-46e3-a976-09527c3c56c0;appFamily=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0;reqChannel=web;channel=web;',
#             'deviceId': '0c3a5531-a0e8-46e3-a976-09527c3c56c0',
#             'Content-Type': 'application/json',
#             'Sec-Fetch-Dest': 'empty',
#             'Sec-Fetch-Mode': 'cors',
#             'Sec-Fetch-Site': 'same-origin',
#             'Connection': 'keep-alive',
#     }

#     response = requests.get(url,headers=headers)
 

#     data = json.loads(response.text)
#     breakpoint()
#     reviews = data.get("data", {}).get("reviews", [])
#     for review in reviews:
#         rew = {
#             "Id": review.get("style").get("id"),
#             "user": review.get("userName"),
#             "rating": review.get("style").get("userRating"),
#             "review_text": review.get("style").get("review"),
#             "created_on": review.get("updatedAt"),
#             "User_Image_url":review.get("images").get("url"),
#         }
#         reviews_data.append(rew)


            
