import requests

from lxml import etree


class MeiZiSpider(object):
    def __init__(self):
        self.url = "https://www.mzitu.com/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
            "referer": "https://www.mzitu.com/",    
        }
        self.page = 1

    def send_request(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def parse_response(self, html):
        html_str = etree.HTML(html)
        div_list = html_str.xpath("//*[@id='pins']/li/a/@href")
        return div_list

    def get_page(self, single_page_response):
        html_str = etree.HTML(single_page_response)
        max_page = html_str.xpath("//div[@class='pagenavi']//span/text()")[-2]
        return max_page

    def img_link(self, final_page_response):
        html_str = etree.HTML(final_page_response)
        final_img = html_str.xpath("//div[@class='main-image']//img/@src")[0]
        return final_img

    def send_img_request(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content



    def save_img(self, response, img_name):
        with open(img_name, "wb") as f:
            f.write(response)



    def main(self):
        url = self.url.format(self.page)

        html = self.send_request(url)
        item_list = self.parse_response(html)
        for single_page in item_list:
            single_page_response = self.send_request(single_page)
            max_page = self.get_page(single_page_response)
            for page in range(1, int(max_page) + 1):
                page_url = single_page + "/" + str(page)
                final_page_response = self.send_request(page_url)
                img_url = self.img_link(final_page_response)
                # print(img_url)
                img_name = img_url[-9:]
                response = self.send_img_request(img_url)
                self.save_img(response, img_name)

                


if __name__ == '__main__':
    meizispider = MeiZiSpider()
    meizispider.main()