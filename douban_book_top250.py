"""Get books info from https://book.douban.com/top250
Download title, rating, sentense to json file and upload them to MongoDB
You need to change the MongoClient address to your server address(ip:port)
"""

import json

import requests
from lxml import etree
import pymongo
from tqdm import tqdm

# connect to mongodb
# Here I am using database scrape and collection douban
client = pymongo.MongoClient(host, port)
collection = client.scrape.douban

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
}


def get_one_page(url):
    """Send request to url"""
    response = requests.get(url, headers=headers, timeout=5)
    if response.status_code == 200:
        return response.text
    else:
        print('Connection Error!')
        exit()


def get_page_books(content):
    """Get 25 books info of every single page"""
    html = etree.HTML(content)
    # this is where one book info stores
    books = html.xpath('//div[@class="pl2"]/..')
    for book in books:
        title = book.xpath('div[1]/a[1]/text()')[0].strip()
        rating = book.xpath('div/span[@class="rating_nums"]/text()')[0].strip()
        try:
            sentense = book.xpath('p/span[@class="inq"]/text()')[0].strip()
        except IndexError:
            sentense = ''
        book = {
            'title': title,
            'rating': rating,
            'sentense': sentense,
        }
        book_list.append(book)


def write_to_json(content):
    with open('douban_book_top250.txt', 'w', encoding='utf-8') as f:
        # ensure_ascii=False to show chinese characters correctly
        f.write(json.dumps(content, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    book_list = []
    # use tdqm to show progress bar
    for page_num in tqdm(range(10)):
        url = 'https://book.douban.com/top250?start=' + str(page_num*25)
        sourcepage = get_one_page(url)
        get_page_books(sourcepage)
    write_to_json(book_list)
    collection.insert_many(book_list)
