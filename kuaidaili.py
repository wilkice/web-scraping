'''
This is a demo used to get free ip-proxy from kuaidaili.com
'''

import requests
from lxml import html

class Kuaidaili():
    def __init__(self):
        self.buffer_list = []
    
    def send_request(self,url):
        try:
            r = requests.get(url, timeout = 3).content
        except:
            return False
        else:
            return r


    def parse(self, r):
        sel = html.fromstring(r)
        for i in sel.xpath('//*[@id="list"]/table/tbody/tr'):
            ip = i.xpath('td[1]/text()')[0]
            port = i.xpath('td[2]/text()')[0]
            finnal =  ip + ':' + port
            self.buffer_list.append(finnal)


    def save_ip(self):
        # save "ip: port" to txt file
        with open('ip.txt','w') as f:
            f.write('Total: '+ str(len(self.buffer_list)) +' ip\n')
            for i in self.buffer_list:
                f.write(i+'\n')


    def main(self):
        page = input('Pls tell me how many pages you want to get(each page has 15 ip): ')
        
        for i in range(1,int(page)+1):
            url = 'http://www.kuaidaili.com/free/inha/' + str(i)
            r = self.send_request(url)
            if not r:
                print('Connect to kuaidaili failed. ')
                break
            else:
                self.parse(r)
                self.save_ip()


if __name__ == "__main__":
    daili = Kuaidaili()
    daili.main()
    
