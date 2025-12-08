import requests
import json
import re

urls = "https://www.myntra.com/gateway/v1/reviews/product/25756776?size=12&sort=0&rating=0&page=5&includeMetaData=true"

for url in urls:
    match = re.search(r'/product/(\d+)', url)
    if match:
        product_id = match.group(1)

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
  'Cookie': '_mxab_=config.bucket%3Dregular%3Bcoupon.cart.channelAware%3DchannelAware_Enabled%3Bcart.cartfiller.personalised%3Denabled; _pv=default; dp=d; at=ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pTkdZM1lqa3habUV0WXpabU1TMHhNV1l3TFdJNVpHRXRNbUV6TXpoa09HWmxOVGRsSWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUzTnpreU9USXdNVGNzSW1semN5STZJa2xFUlVFaWZRLmszRm1fdTE4SzNGcF81Vk9JSElWY0hGYlZ6Tkt1Zklxc3lOTTRtQkVfNnM=; microsessid=273; utm_track_v1=%7B%22utm_source%22%3A%22direct%22%2C%22utm_medium%22%3A%22direct%22%2C%22trackstart%22%3A1763740017%2C%22trackend%22%3A1763740077%7D; lt_timeout=1; lt_session=1; utrid=eAleD0xOBklCBmMUGANAMCMyOTY3Njk5NTc4JDI%3D.d4c7fb0dc23e13ed661e2749b48fa953; _d_id=94708384-d26e-4e8c-bae6-e9ff5af6dd06; user_session=X_vkxIs0UERzbhK6HWOEIg.nvwsp3nwQQHA8OHHvWrC2yaNpfyHHME8lSxNqaUh_d2hc2EtK2b4XmRDF63Yr-Vv5ZQ5wL6N8Mi8k83AkViPW36G5-tnHYiiCFstrdaWmwGlS0fGY7R4kJ9lPsrnqqDNrktOEy725M5coUuoHPu1Dw.1763740017147.86400000.Y63H5QHnd0KT27_rkh-SQIn0qcQV1c-o0Swxn0MM7ko; _abck=FBECC24DA61EB8E31C1E56D56AF25E97~-1~YAAQjPQ3F4Hyv6SaAQAAW/EYpw6D20DV7VCOzGe+MoRqqQO/1v3XhoeqWL0kwvu+HYFlgz1vOg1LagIDag0GloRsv/ihzFVpnwcqpl/yRF4GX856LsuTAc+JZGXKx/cOuzaKd/6V8m3DwpK6pf/BPtkOS/dhQxpOuPkcm+Rq9vWpA1JrAc61ayq79B7a/614b3XjngJWymAgH00oATb0NoAYvj/Angc5oLyk3RK6IezojNjDsgNawqN8UGycdcxodFPj/dQvFQ3znwdn9L6HYvH7qzBN0YmPHes1VQTJT7zyvkHhSE4hhjVfpTn9r0akTQzsgRGDf8FX34+MNN1DErMXq7810sK+2OXZVdP7EQAM5EVuDVLvwted0+uLmZd8DuyHzZrR8KXhv7eMw5tWkyc2SyhITlsNTpGnHFxHg6weRHDqfHJUnK72scuAUqMFpJAG28y3+11Uvmc63Mg8JH9NzW7mZYVvwCYeJtnQ4vpnLR9st433n+1NcrMsJI40AlZg5btTtNJvbcb/b5vNhP+oWb2lLvn24sdrkd7NCGmGeFsLYa2cYTh5H210b2igJdKLhVyVUClBbQQLflDAeI/e1iAjzf5csL3+QP2fLZ8/2RsPNkGyh+Xj~-1~-1~-1~AAQAAAAE%2f%2f%2f%2f%2f2+kVSQ7uYKSy5A7F2sLUmtF05eINPe2ccInAUbIpCkG2ADjuLUKc9k4iucjeLAojJRZ8fX5mpNeO1yu4BqyEvkxbJDSTkc8nr%2fk~-1; ak_bmsc=4EEEEFEB4BBAA3A565519C5A9EE4DD62~000000000000000000000000000000~YAAQjPQ3Fwbxv6SaAQAAX+IYpx08Yo/LMOa30iy9u+8FStPPS/V/j9pROi1sjm+Kwi4oQVQQIiiee/b56/x+ia9ySKWPDfkTfluap/bkI1f1o21j19ph0940JlDUZAlW2x5QyhrB6u+1HB83zm0nG4D9eALnetgzagWICD+jGDNaGSvzkSS6ozZmkU/baWXNBz6ppElJKtgPQy1pIe700kQzjl0WetLsSyLMZKgsTnKaJ6uwRZOVJqQej0cRu+Ij2sVnTMWy97k/+6AAH7vhVVCvqnyx/JKB1nhrZobd4JPiuZZB13d5XzzGrw7nRGesNSkXMDo4Jk/8oU1QYFU6aNAayzdpzM8lVk1ZFvrF9Mx0AxhisHDtI8ckg2P/O01IPKa9jCE48KJa07LfQRl5AdZYdHLQQVD3aQO0xqBObi1oUw4=; bm_sz=850A8F3E1B1319DC8756DABD9A53A6AC~YAAQjPQ3Fwjxv6SaAQAAX+IYpx1sXbyvrHMpQcS2RJIcgBbHbSv9LtFsIds+EijPkolzzsHrnGMr604xVNxdc5YtylPfhPDtxNTXblj7HdjvjnP5KUcq4L9iMs8gnaGPDItelGUnJhLnrUabKSH1zX/8rP3yLxmzshuZu+ZEmT416kgom5gHn40gOUBpl/kRSjw1NhQJMrlqfXp1a13AQH4wiG4mPYH4mIMpnJjdKQ7mqwnUWfrm5ACUQf0apeWX3VDoOnqcXXoNAJqE8v0iUWh3XMwxPuzpkJhBIkAhg8fSI2NX57PUoEDoluaLPAs5NYl0RIlDK+/rFkfsPhTMDKrsal4AWlDYA0A90glfwMA8n+7kxoiOR4KcTGlrZT075ltXc0r9JHiVrlGlIRU7r+U62mJ3QffMJ1NZVBbq0OBrgXed~3618118~3163444; mynt-eupv=1; _ma_session=%7B%22id%22%3A%220fc008ee-aa5e-4009-b2d9-8e1e869d5b1c-94708384-d26e-4e8c-bae6-e9ff5af6dd06%22%2C%22referrer_url%22%3A%22%22%2C%22utm_medium%22%3A%22%22%2C%22utm_source%22%3A%22%22%2C%22utm_channel%22%3A%22direct%22%7D; _xsrf=HBfA6RSamrJMSVZcRasnbKlBzZsvf7Qd; bm_sv=E39C2AA15AEAF2418BC7530DCCD56D36~YAAQjPQ3Fyv1v6SaAQAAzRQZpx0NuvrTAOiJawR5kse7mN8vTfP0OVJC9cnwC/kQ8JcAc19MUCaZJrkmr03amtN0ppHeldXpk7+Ycme0xKa4lZXMZJ8Rif7HQj2WQYZKDLCRDfWoZWFWa3GgblD92VOiwPxwvLEqeofvVfyCNV9SOeif4rFB5I8uB/P/HC6B2D7I3hDZIaA7Lj2GOpKZwTEaRCuipChI0DnGews9SRr0fSnEFxzFUhzsMAR5SpMb~1; x-mynt-pca=ky9k2YX3TH08xlCaGHhUYuRpIkrG3GCpCMpaMQTTlaMXoD5_ovSIJlJTxHFglhu2d5RpWABaP1XyVvRvEr4raBTmk0OlIQccA2VgQwan3oUZ9Z-e31Q%3D',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'TE': 'trailers'
}
response = requests.get(f'https://www.myntra.com/gateway/v1/reviews/product/{product_id}',headers=headers)
print(response.text)
print(response.status_code)