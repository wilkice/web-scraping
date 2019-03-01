'''
This is a demo to scrape baidu tieba.
Author: darcy
Date:2019/3/1
https://www.amazon.cn/b?ie=UTF8&node=1875254071, 3.1日打折电子书链接
'''

import requests

class Douban(object):
    def __init__(self):
        self.base_url = 'https://book.douban.com/top250?icn=index-book250-all'
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Referer': 'https://book.douban.com/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        }


    def send_request(self):
        try:
             r = requests.get(self.url, headers = self.headers, timeout = 3)
        except:
            print('This is wrong during connecting this site! Pls try again.')
        else:
            return r

    def parse_response(self):
        pass

    def save_data(self,response):
        with open('douban.html','wb') as f:
            f.write(response.content)
            print('Writting Success.')

    def main(self):
        channel = input('Pls input the channel you want to check: ')
        self.url = self.base_url + channel
        response = self.send_request()
        self.save_data(response)
        

if __name__ == "__main__":
    douban = Douban()
    douban.main()