'''
This is a demo used to get pic from samsungclub
'''
import requests
from lxml import html

class SamsungClub():
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
        }
        # self.proxies = {
        #     'http': 'http://45.125.32.181:3128'
        # }

    def send_request(self, url):
        r = requests.get(url, headers = self.headers, timeout =3)
        return r

    @staticmethod
    def get_img_page(response):
        sel = html.fromstring(response.content)
        page_url_list = sel.xpath("//h1[@class='Intercept']/a/@href")
        return page_url_list

    @staticmethod
    def get_img_url(response):
        sel = html.fromstring(response.content)
        img_url_list = sel.xpath("//img[@class='ueditor_img']/@src")
        return img_url_list

    @staticmethod
    def save_img(response, filename):
        with open(filename,'wb') as f:
            f.write(response.content)
        
        

    def main(self):
        homepage_url = 'http://www.galaxyclub.cn/photo'
        response = self.send_request(homepage_url)
        page_url_list = SamsungClub.get_img_page(response)
        print('get page')
        for page in page_url_list:
            url = 'http://www.galaxyclub.cn' + page
            print('url: ' + url)
            response = self.send_request(url)
            img_url_list = SamsungClub.get_img_url(response)
            print('img_url_list')
            for img in img_url_list:
                print('进来了')
                filename = img[-10:]
                print(filename)
                response = self.send_request(img)
                SamsungClub.save_img(response, filename)
                print('save')




homepage = SamsungClub()
homepage.main()
