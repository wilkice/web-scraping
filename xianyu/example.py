from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

server = 'http://localhost:4723/wd/hub'

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'SM-N9500',
    'appPackage': 'com.taobao.idlefish',
    'appActivity': 'com.taobao.fleamarket.home.activity.MainActivity',
    # 'appPackage': 'com.dealmoon.android',
    # 'appActivity': 'com.north.expressnews.main.MainActivity'
    'unicodeKeyboard': True,
    'resetKeyboard': True,

}

driver = webdriver.Remote(server, desired_caps)

wait = WebDriverWait(driver, 30)

permission_1 = wait.until(EC.presence_of_element_located((By.ID, "com.android.packageinstaller:id/permission_deny_button")))
permission_1.click()
permission_2 = wait.until(EC.presence_of_element_located((By.ID, "com.android.packageinstaller:id/permission_deny_button")))
permission_2.click()
permission_3 = wait.until(EC.presence_of_element_located((By.ID, "com.android.packageinstaller:id/permission_deny_button")))
permission_3.click()
ignore = wait.until(EC.presence_of_element_located((By.ID, "com.taobao.idlefish:id/left_btn")))
ignore.click()
# tap search box
search_box = driver.find_element_by_id("com.taobao.idlefish:id/search_bar_text")
search_box.click()
search_text = wait.until(EC.presence_of_element_located((By.ID, "com.taobao.idlefish:id/search_term")))
search_text.send_keys('Macbook')
search_button = driver.find_element_by_id("com.taobao.idlefish:id/search_button")
search_button.click()



