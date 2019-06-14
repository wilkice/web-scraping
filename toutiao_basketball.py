"""requests with ajax, save imgs to disk
site: https://www.toutiao.com/search/?keyword=%E7%94%B5%E8%84%91
"""

import time
import json
from urllib.parse import urlencode
import time
import os

import requests


base_url = 'https://www.toutiao.com/api/search/content/?'

headers = {
    'Host': 'www.toutiao.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Referer': 'https://www.toutiao.com/search/?keyword=%E7%94%B5%E8%84%91',
    # Cookie is must needed
    'Cookie': 'tt_webid=6701920522718725645; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6701920522718725645; csrftoken=f48c81795caf910eb16cfe8c3141e9e7; s_v_web_id=9a5f44e3ffacdf73721fb92b01265513; __tasessionId=wu0hwpd4y1560419148351TE: Trailers'
}


def get_page(offset):
    """get content for every page"""
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '电脑',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
        'timestamp': int(time.time()*1000),
    }
    url = base_url + urlencode(params)
    print(url)
    try:
        response = requests.get(url, timeout=5, headers=headers)
    except requests.ConnectionError as e:
        print(e)
    else:
        if response.status_code == 200:
            return response.json()


def parse_json(content):
    """parse data"""
    for item in content.get('data'):
        img_list = []
        if item.get('image_list'):
            for img in item.get('image_list'):
                img_list.append(img.get('url'))
            title = item.get('title')
            toutiao_list.append({'title': title,
                                 'img_list': img_list})


def save_json():
    with open('toutiao.txt', 'w', encoding='utf-8') as f:
        json.dump(toutiao_list, f, indent=2, ensure_ascii=False)


def save_image():
    for one_topic in toutiao_list:
        title = one_topic['title']
        url_list = one_topic['img_list']
        if not os.path.exists('img/' + title):
            os.makedirs('img/' + title)
        for index, url in enumerate(url_list):
            img = requests.get(url)
            with open('img/' + title + '/' + str(index) + '.jpg', 'wb') as f:
                f.write(img.content)


if __name__ == "__main__":
    toutiao_list = []
    response = get_page(20)
    parse_json(response)
    save_json()
    save_image()
