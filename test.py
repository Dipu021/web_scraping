import requests
import json
import time

data =[]


# url = "https://www.myntra.com/gateway/v1/reviews/product/25756776?size=12&sort=0&rating=0&page=5&includeMetaData=true"
base_url = "https://www.myntra.com/gateway/v1/reviews/product/25756776"

cookies=''
for key,value in response.cookies.get_dict().items():
    cookies+=f'{key}:{value}; '

headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:145.0) Gecko/20100101 Firefox/145.0',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjMwNjIwNzEiLCJhcCI6IjcxODQwNzY0MyIsImlkIjoiNzBlNzM5NzUxNjY0N2EyZCIsInRyIjoiOTc3MjI0ODE1YzQ1MWNiZTRjNTVkMTFiZGIwYzg0NTkiLCJ0aSI6MTc2Mzc0MDAzMDk4NywidGsiOiI2Mjk1Mjg2In19',
        'traceparent': '00-977224815c451cbe4c55d11bdb0c8459-70e7397516647a2d-01',
        'tracestate': '6295286@nr=0-1-3062071-718407643-70e7397516647a2d----1763740030987',
        'X-myntraweb': 'Yes',
        'X-Requested-With': 'browser',
        'x-meta-app': 'deviceId=94708384-d26e-4e8c-bae6-e9ff5af6dd06;appFamily=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:145.0) Gecko/20100101 Firefox/145.0;reqChannel=web;channel=web;',
        'deviceId': '94708384-d26e-4e8c-bae6-e9ff5af6dd06',
        'Content-Type': 'application/json',
        'Connection': 'keep-alive',
        'Referer': 'https://www.myntra.com/reviews/25756776',
        'Cookie': 'mxab=; Domain=.myntra.com; Path=/; Expires=Sun, 23 Nov 2025 16:43:25 GMT;_pv=default; Domain=.myntra.com; Path=/; Expires=Sun, 23 Nov 2025 16:18:25 GMT; HttpOnly;dp=d; Domain=.myntra.com; Path=/; Expires=Sun, 23 Nov 2025 16:19:25 GMT; HttpOnly;at=ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pTlRabE9EVmlORFV0WXpnNE55MHhNV1l3TFRnNE9UQXRZall4WVRjeE5XRXhPRFV5SWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUzTnprME5qWTBNRFVzSW1semN5STZJa2xFUlVFaWZRLmd0eVFVaDVWV0ZwNmVfQW9yMlpWTWFyX1ZtSzNTNDVWOGt4ZXlIOVFTUGc=; Domain=.myntra.com; Path=/; Expires=Thu, 28 May 2026 16:13:25 GMT; HttpOnly;bc=true; Domain=.myntra.com; Path=/;utm_track_v1=%7B%22utm_source%22%3A%22direct%22%2C%22utm_medium%22%3A%22direct%22%2C%22trackstart%22%3A1763914405%2C%22trackend%22%3A1763914465%7D; Domain=.myntra.com; Path=/; Expires=Sun, 23 Nov 2025 16:14:25 GMT; HttpOnly;lt_session=1; Domain=.myntra.com; Path=/; Expires=Sun, 23 Nov 2025 16:43:25 GMT; HttpOnly;utrid=XQUQVRp%2FCwIYGBpddVlAMCM0MDgxMTc3MDE2JDI%3D.effcd940d044c2f3d00e06002582a678; Domain=.myntra.com; Path=/; Expires=Fri, 22 May 2026 16:13:25 GMT; HttpOnly;_d_id=0e0fd546-5881-4b1d-8ee5-c225cfead6aa; Domain=.myntra.com; Path=/; Expires=Sat, 19 Aug 2028 16:13:25 GMT;_abck=4B5E6715F4F9FDF3924CB1FBA7485F64~-1~YAAQlJbTZ53F2qKaAQAAItZ9sQ5db/4D03svAPlKyZ6XGQAGPQkUThBkugbx6GqzixfFVgk9rPLMv6fVL0aqXmoq9JtLhGAglR+Qmpqnlf5+YR1GquXPNEuJWCAmPkxwv/rGGMToy5/+K30YHJ80zFpwUHPD+SAEqk2hQrTRNG1u4YJsQnUlyWnthFl1Cw5o7nSfLOYIRJ1JECweaTpdSMWnWKWgKc44Nhm7hVjRkt4aN/pYMLrNb8GpoNtpX+7iM2M9EMQ4GdUPx1V/JdwOYYvQpHGdJ1ZemCuj4oUmfUJx3YkIflcyCpkxNHubNt2G6e8uHcQTwkyYQuiWt+jOcC38LlOaxwAoAt8QkoiRYA0dnhE71QAxh0Fowv0GLNGWXIhKLdNbdjF1c3VL7PIEEVTCN8N3eeFIoz0YBpRVKcqvXvC3Jbj4US1YJ5QTFUoMOlpOqwvxsuzF5tsEbgb0x18qI4dm/aoLAS1N6UCQc8zd6Tr3MGn1HxBf546CA2RRQbEi5mbKWKBKSdalVCmFW2k0olY+hIBDgSLlCpgIByiwBooma9rE1Q1pOA3sDrDCIvF5H+HJiHHwSA1jEchJ4SsPjZLO2gYWbBUOKIFrFh3XbOiNDWvdYyt6bJ6qXuxgQCn79ot06zdAiIVbZFQ=-1-1~-1~AAQAAAAE%2f%2f%2f%2f%2f87CYDezlJIxWA7xNkGxA7rXch+guiMFO1bFYrB41bXtJJGQlVvKPNwtKAhpiwW3GUiGEl8Nh4D55OFXGoyAhIdrwKtqa50+OYDL~-1; Domain=.myntra.com; Path=/; Expires=Mon, 23 Nov 2026 16:13:25 GMT; Max-Age=31536000; Secure;bm_sz=800686D73C0EBBCEB6A878F933CD02D0~YAAQlJbTZ6DF2qKaAQAAItZ9sR1idQYmLR8pwcHhxJhZBYBe1ZsZK62uZnQBcdfjFoJqcA/1fcvcG2Tt4EPMB1n+YiDf8DM0VEQBdpUOh3jec8SXHvEujRyx5TZscXacFnMkaT1/KueGHmwT0zObcA0O7c0rBlt/jUQIDuk+EMLLqyk0SdqphSB+vjJ8lZP2WRhRKJ2TjDTtF+/hIbXEM24Hfku6fvl0gKZOM8LQQjG3ai1Tzv42X1kK972nxHirWe/NaHFxv0odk6BWVrl5QiM7S3Ay9ahrtCgkXdzqPgWocD5YALI8jwJLSHBXyAMvKmK4s3iVVPhX0LR95xREFwoPE2JPio7FffXT6FTSrjdm8C0/7f4f0D4CBxckU5nwXtydTIGuwYs=~3290681~4473670; Domain=.myntra.com; Path=/; Expires=Sun, 23 Nov 2025 20:13:25 GMT; Max-Age=14400;',        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'TE': 'trailers'
    }
page = 1
while True:
    url = f"{base_url}?size=12&sort=0&rating=0&page={page}&includeMetaData=true"
    headers['Cookie']=cookies

    response = requests.get(url, headers=headers)
    
    json_data = response.json()
    json_items = json_data.get('reviews', [])

    if not json_items:
        break

    for item in json_items:
        rew = {
            "Id": item.get("style").get("id"),
            "user": item.get("userName"),
            "rating": item.get("userRating"),
            "review_text": item.get("review").strip(),
            "created_on": item.get("updatedAt"),
            # "User_Image_url":item.get("images")[0].get("url",''),
        }
        data.append(rew)

    page += 1
    time.sleep(1)
    print(response.status_code)



with open("outrew.json","w",encoding="utf-8") as f:
    json.dump(data,f,indent=4,ensure_ascii=False)