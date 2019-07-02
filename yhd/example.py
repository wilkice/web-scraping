import time
import json
import re

import requests
from urllib.parse import urlencode

base_url = 'https://search.yhd.com/searchPage/c0-0/mbnameApple-b/a-s1-v4-p5-price-d0-f0b-m1-rt0-pid-mid0-color-size-kmacbook/?'
params = {
    "isGetMoreProducts": "1",
    "moreProductsDefaultTemplate": "0",
    "isLargeImg": "0",
    "moreProductsFashionCateType": "2",
    "nextAdIndex": "0",
    "nextImageAdIndex": "0",
    "adProductIdListStr": "",
    "fashionCateType": "2",
    "firstPgAdSize": "0",
    "needMispellKw": "",
    "onlySearchKeyword": "1",
    "_": int(time.time() * 1000),
}
params_flash = {
    'isLargeImg': 0,
    'fashionCateType': 2,
    'onlySearchKeyword': 1,
    '_': int(time.time() * 1000),
}
url = base_url + urlencode(params)
url_flash = base_url + urlencode(params_flash)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3818.0 Safari/537.36 Edg/77.0.189.3',
    'Referer': 'https://www.yhd.com/',
}
headers_flash = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3818.0 Safari/537.36 Edg/77.0.189.3',
    'Referer': 'https://search.yhd.com/c0-0/kmacbook/',
}

response = requests.get(url, headers=headers)
# response = requests.get(url_flash, headers=headers_flash)
content = response.json().get('value')
pattern = re.compile(
    '<b>¥</b>(.*?)\n\t</em>.*?title=(.*?) singleFreeFlag', re.S)
items = re.findall(pattern, content)
for item in items:
    print(item)  # price + details

print('finished')
