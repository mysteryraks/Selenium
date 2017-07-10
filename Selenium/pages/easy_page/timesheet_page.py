import time
from Selenium.utilities.helpers import Helpers
import Selenium.utilities.custom_logger as cl
import logging


class TimeSheet(Helpers):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        self.driver = driver

    def click_ack(self):
        self.wait_for_element("input#ctl00_CPH_chkAcknow", 30, "css")
        self.verify_title("MyTime")
        self.click_element("input#ctl00_CPH_chkAcknow", "css")
        time.sleep(5)
        self.log.info("Ack button was clicked")
