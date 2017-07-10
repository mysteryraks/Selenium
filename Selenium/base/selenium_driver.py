from selenium import webdriver
import os


class Driver():

    def __init__(self, browser):
        self.browser = browser

    def start_driver(self):
        if self.browser == 'firefox':
            driver_location = "/Users/AshaRakesh/PycharmProjects/Selenium/configfiles/geckodriver.exe"
            os.environ["webriver.gecko.driver"]=driver_location
            driver = webdriver.Firefox()
        elif self.browser=='chrome':
            driver_location = "/Users/AshaRakesh/PycharmProjects/Selenium/configfiles/chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = driver_location
            driver = webdriver.Chrome()
        else:
            driver_location = "/Users/AshaRakesh/PycharmProjects/Selenium/configfiles/chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = driver_location
            driver = webdriver.Chrome()
        driver.maximize_window()
        driver.set_page_load_timeout(40)
        driver.implicitly_wait(15)
        return driver
