import pytest
import unittest
from Selenium.pages.easy_page.easy_home_page import EasyPage
from Selenium.pages.easy_page.timesheet_page import TimeSheet
from Selenium.utilities.helpers import Helpers
import time
import Selenium.utilities.custom_logger as cl
import logging


@pytest.mark.usefixtures("one_time_setup")
class EasyTests(unittest.TestCase, EasyPage, TimeSheet, Helpers):

    log = cl.customLogger(logging.INFO)

    @pytest.fixture(autouse=True)
    def classSetup(self, one_time_setup):
        self.log.info("In easy setup")
        self.driver = one_time_setup
        self.easy = EasyPage(self.driver)
        self.myTime = TimeSheet(self.driver)
        # print(type(self.easy))
        # print(type(self.myTime))

    @pytest.mark.run(order=1)
    def test_easy_login(self):
        self.log.info("Verifying easy login")
        self.driver.get("https://easy.techmahindra.com")
        result = self.easy.login()
        self.get_screenshot("test_easy_login")
        assert result == True
        self.log.info("Completed verification of 'test_easy_login'")

    @pytest.mark.run(order=2)
    def test_myTime_link(self):
        self.log.info("Verifying 'test_myTime_link'")
        self.myTime = self.easy.click_my_time_link()
        self.myTime.click_ack()
        self.get_screenshot("test_myTime_link")
        # print(type(self.myTime))
        self.log.info("Completed verification of 'test_myTime_link'")

    @pytest.mark.run(order=2)
    def test_select_the_desired_week(self):
        # print(type(self.myTime))
        # print(type(self.easy))
        self.myTime.click_ack()
        time.sleep(2)
        self.easy.switch_to_parent_window()
        time.sleep(1)
        self.easy.verify_title("EASY - Easy Access System For You")


