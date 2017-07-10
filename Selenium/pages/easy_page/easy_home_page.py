import time
from selenium.webdriver.common.by import By
from Selenium.pages.easy_page.timesheet_page import TimeSheet
from Selenium.utilities.helpers import Helpers
import Selenium.utilities.custom_logger as cl
import logging


class EasyPage(Helpers):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

#   locators
    _username_field = "txtLanId"
    _password_field = "txtPassword"
    _login_btn = "btnlogin"
    _my_time_link = "a#lnkFav1"

    def getusername(self):
        return self.get_element(self._username_field, "name")

    def getpassword(self):
        return self.driver.find_element(By.NAME, self._password_field)

    def getloginbtn(self):
        return self.driver.find_element(By.NAME, self._login_btn)

    def setusername(self):
        self.send_text(self._username_field, "rr0023714", locatorType="name")

    def setpassword(self):
        self.send_text(self._password_field, "Trinity@062017")

    def getmytimelink(self):
        return self.driver.find_element_by_css_selector(self._my_time_link)

    def login(self):
        self.log.info('In method EasyPage.login()')
        if self.verify_title("EASY - Login"):
            self.log.info("Login page title was verified correctly as 'EASY - Login'")
            self.setusername()
            self.setpassword()
            self.getloginbtn().click()
        else:
            self.log.error("login failed because the title of login page was not correct and expected title was 'EASY - Login'...")
            return False
        if self.verify_title("EASY - Easy Access System For You"):
            self.log.info("Easy Login Successful")
            return True
        else:
            self.log.error("Login failed")
            return False

    def click_my_time_link(self):
        self.log.info('In method EasyPage.click_my_time_link()')
        self.wait_for_element("//p[contains(text(), 'My Time')]", 30, "xpath")
        self.click_element("//p[contains(text(), 'My Time')]", "xpath")
        time.sleep(5)
        self.switch_to_new_window()
        return TimeSheet(self.driver)

