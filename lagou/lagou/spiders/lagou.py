import scrapy


class LagouSpider(scrapy.Spider):
    name = "lagou"

    def start_requests(self):
        base_url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false'
        formdata = {
            "first": False,
            "pn": 1,
            "kd": "爬虫",

        }
        return scrapy.FormRequest(base_url, formdata=formdata, callback=self.parse)

    def parse(self, response):
        yield response.json()
