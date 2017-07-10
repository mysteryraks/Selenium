import time
from Programs.helpers import Helpers
import os
from selenium import webdriver


class Screenshot:

    def __init__(self):
        driver_location = "/Users/AshaRakesh/PycharmProjects/Selenium/configfiles/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driver_location
        self.driver = webdriver.Chrome()

    def test(self):

        self.driver.get("https://facebook.com")
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(40)
        self.driver.implicitly_wait(15)
        Helpers._get_screenshot(self.driver, 'rakesh')
        time.sleep(5)

scr = Screenshot()
scr.test()


