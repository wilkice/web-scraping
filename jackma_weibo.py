"""requests with ajax
site: https://m.weibo.cn/u/2145291155
"""

import time
import json
from urllib.parse import urlencode

import requests
from pyquery import PyQuery as pq


base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
}


def get_page(page):
    """get content for every page"""
    params = {
        'type': 'uid',
        'value': '2145291155',
        'containerid': '1076032145291155',
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, timeout=5, headers=headers)
    except requests.ConnectionError as e:
        print(e)
    else:
        if response.status_code == 200:
            return response.json()


def parse_json(content):
    """parse data"""
    for item in content['data']['cards']:
        time = item['mblog']['created_at']
        text = pq(item['mblog']['text']).text()
        like = item['mblog']['attitudes_count']
        one_weibo = {
            'time': time,
            'like': like,
            'text': text,
        }
        weibo_list.append(one_weibo)


def get_total_pages():
    """get total weibo counts"""
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=2145291155&containerid=1005052145291155'
    try:
        response = requests.get(url, timeout=5, headers=headers)
    except requests.ConnectionError as e:
        print(e)
    else:
        if response.status_code == 200:
            total_items = response.json()['data']['userInfo']['statuses_count']
            return total_items


if __name__ == "__main__":
    weibo_list = []
    total_items = get_total_pages()
    pages = (total_items // 10) + 1
    for page in range(pages):
        content = get_page(page)
        parse_json(content)
        time.sleep(3)
    with open('jackma_weibo.json', 'w', encoding='utf-8') as f:
        json.dump(weibo_list, f, indent=2, ensure_ascii=False)
    print('Saved')
