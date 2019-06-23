import requests
import time

base_url = 'https://search.yhd.com/searchPage/c0-0/mbname%E5%BE%AE%E8%BD%AF%EF%BC%88Microsoft%EF%BC%89-b/a-s1-v4-p1-price-d0-f0b-m1-rt0-pid-mid0-color-size-ksurface+book/?isGetMoreProducts=1&moreProductsDefaultTemplate=0&isLargeImg=0&moreProductsFashionCateType=2&nextAdIndex=0&nextImageAdIndex=0&adProductIdListStr=&fashionCateType=2&firstPgAdSize=0&needMispellKw=&onlySearchKeyword=1&_='

timestamp = int(time.time() * 1000)
url = base_url + str(timestamp)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3818.0 Safari/537.36 Edg/77.0.189.3',
    'Referer': 'https://www.yhd.com/',

}

response = requests.get(url, headers=headers)
# with open('example.html', 'w', encoding='utf-8') as f:
#     f.write(response.content.decode('utf-8'))
print(response.content.decode('utf-8'))


# callback: jQuery111307046293252049012_1561023575257
# isGetMoreProducts: 1
# moreProductsDefaultTemplate: 0
# isLargeImg: 0
# moreProductsFashionCateType: 2
# nextAdIndex: 0
# nextImageAdIndex: 0
# adProductIdListStr: 
# fashionCateType: 2
# firstPgAdSize: 0
# needMispellKw: 
# onlySearchKeyword: 1
# _: 1561023575259

# callback: jQuery11130007428571518508065_1561023686812
# isGetMoreProducts: 1
# moreProductsDefaultTemplate: 0
# isLargeImg: 0
# moreProductsFashionCateType: 2
# nextAdIndex: 0
# nextImageAdIndex: 0
# adProductIdListStr: 
# fashionCateType: 2
# firstPgAdSize: 0
# needMispellKw: 
# onlySearchKeyword: 1
# _: 1561023686814
