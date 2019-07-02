"""This program can get items from xianyu(2.taobao.com) and save it to mongodb
TODO: add city, likes and images
TODO: mondo primary key and index
"""


import time

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import pymongo


server = 'http://localhost:4723/wd/hub'
TIMEOUT = 300
MONGO_URI = 'localhost'
MONGO_DB = 'scrape'
MONGO_COLLECTION = 'xianyu'


class Xianyu(object):
    """This is a spider to scrape item info from xianyu(2.taobao.com)"""

    def __init__(self, item_name):
        """Connect to mongodb and appium"""
        self.desired_caps = {
            'platformName': 'Android',
            'deviceName': 'SM-N9500',
            'appPackage': 'com.taobao.idlefish',
            'appActivity': 'com.taobao.fleamarket.home.activity.MainActivity',
            # 'unicodeKeyboard': True,
            # 'resetKeyboard': True,
        }
        self.item_name = item_name
        self.driver = webdriver.Remote(server, self.desired_caps)
        self.wait = WebDriverWait(self.driver, TIMEOUT)
        self.client = pymongo.MongoClient(host=MONGO_URI)
        self.collection = self.client[MONGO_DB][MONGO_COLLECTION]

    def open(self):
        """dont give permission to xianyu"""
        time.sleep(10)
        TouchAction(self.driver).tap(x=890, y=2822).perform()
        time.sleep(1)
        TouchAction(self.driver).tap(x=883, y=2829).perform()
        time.sleep(1)
        TouchAction(self.driver).tap(x=858, y=2822).perform()
        time.sleep(1)
        TouchAction(self.driver).tap(x=461, y=1734).perform()

    def search(self):
        """search items"""
        TouchAction(self.driver).tap(x=749, y=179).perform()
        el1 = self.driver.find_element_by_id(
            "com.taobao.idlefish:id/search_term")
        el1.send_keys(self.item_name)
        TouchAction(self.driver).tap(x=1299, y=192).perform()

    def scroll(self):
        self.driver.swipe(607, 2273, 625, 900)

    def save_onepage(self):
        # items = self.wait.until(EC.presence_of_all_elements_located((By.ID, "com.taobao.idlefish:id/card_root")))
        items = self.wait.until(EC.presence_of_all_elements_located(
            (By.ID, "com.taobao.idlefish:id/btm_card")))
        for item in items:
            try:
                title = item.find_element_by_id(
                    "com.taobao.idlefish:id/result_item_title").get_attribute('text')
                print(title)
                price = item.find_element_by_id(
                    "com.taobao.idlefish:id/integer_price").get_attribute('text')
                print(price)
                # city = item.find_element_by_id("com.taobao.idlefish:id/com.taobao.idlefish:id/city").get_attribute('text')
                # print(city)
                # like = item.find_element_by_id("com.taobao.idlefish:id/search_item_flowlayout").get_attribute('text')
                # print(like)
            except NoSuchElementException:
                pass
            else:
                item_info = {
                    "title": title,
                    "price": price,
                    # "city": city
                }
                # self.collection.insert_one(item_info)


mac = Xianyu('macbook')
mac.open()
mac.search()
mac.save_onepage()
for i in range(4):
    mac.scroll()
    mac.save_onepage()

# permission_1 = wait.until(EC.presence_of_element_located((By.ID, "com.android.packageinstaller:id/permission_deny_button")))
# permission_1.click()
# permission_2 = wait.until(EC.presence_of_element_located((By.ID, "com.android.packageinstaller:id/permission_deny_button")))
# permission_2.click()
# permission_3 = wait.until(EC.presence_of_element_located((By.ID, "com.android.packageinstaller:id/permission_deny_button")))
# permission_3.click()
# ignore = wait.until(EC.presence_of_element_located((By.ID, "com.taobao.idlefish:id/left_btn")))
# ignore.click()
