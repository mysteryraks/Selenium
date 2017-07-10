import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as ec
from traceback import print_stack
import Selenium.utilities.custom_logger as cl
import logging

class Helpers:

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
        self.log.info("In method 'INIT OF HELPERS CLASS'")

    def get_screenshot(self, testName):
        self.log.info("In method 'get_screenshot'")
        time_here = time.localtime()
        time_list = [str(time_here[1]), str(time_here[2]), str(time_here[3]), str(time_here[4])]
        time_list = '.'.join(time_list)
        fileName = testName + time_list + '.png'
        screenshotDirectory = "/Users/AshaRakesh/PycharmProjects/Selenium/"

        try:
            if os.path.exists(screenshotDirectory):
                self.driver.save_screenshot(screenshotDirectory+fileName)
                self.log.info("screenshot obtained with filename: " +fileName)
        except:
            self.log.info("some error while taking screenshot...")

    def switch_to_new_window(self):
        self.log.info("In method 'switch_to_new_window'")
        old_window = self.driver.window_handles[0]
        self.log.info(old_window)
        time.sleep(3)
        new_window = self.driver.window_handles[1]
        self.log.info(new_window)
        try:
            self.driver.switch_to_window(new_window)
            time.sleep(2)
            self.log.info("switched to the new window...")
        except TimeoutException:
            self.log.info("invalid window-->could not switch and probably timedout")

    def switch_to_parent_window(self):
        self.log.info("In method 'switch_to_parent_window'")
        old_window = self.driver.window_handles[0]
        new_window = self.driver.window_handles[1]
        try:
            self.driver.switch_to_window(old_window)
            time.sleep(2)
            self.log.info("switched to the parent window...")
        except TimeoutException:
            self.log.info("invalid window-->could not switch")

    def get_title(self):
        self.log.info("In method 'get_title'")
        return self.driver.title

    def verify_title(self, txt):
        self.log.info("In method 'verify_title'")
        if self.get_title() == txt:
            self.log.info("Title asserted correctly: " +txt)
            return True
        else:
            self.log.error("Title obtained was {0} while expected title was {1}".format(self.get_title(), txt))
            return False

    def get_by_type(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "name":
            print("Found By Type for locator type name...")
            return By.NAME
        elif locatorType == "id":
            return By.ID
        elif locatorType == "className":
            return By.CLASS_NAME
        elif locatorType == "linkText":
            return By.LINK_TEXT
        else:
            print("locator is not supported: " + locatorType)
            return False

    def get_element(self, locator, locatorType = "id"):
        element = None
        try:
            byType = self.get_by_type(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Found element with locator" + locator + " and locator type: " + locatorType)
            return element
        except:
            print("The combination of locator: " + locator +" and locator type: " +locatorType +" did not work")
        return element

    def click_element(self, locator, locatorType = "id"):
        try:
            element = self.get_element(locator, locatorType)
            element.click()
            print("Element with locator: " +locator + " locator type: " +locatorType + " was found a clicked")

        except:
            print("Element with locator: " + locator + " locator type: " + locatorType + " was not found, so, not clicked")
            print_stack()

    def send_text(self, locator, txt, locatorType = "id"):
        try:
            element = self.get_element(locator, locatorType)
            element.send_keys(txt);
            print("Element with locator: " + locator + "locator type: " + locatorType + " was found and text was sent")
        except:
            print("Element with locator: " + locator + " locator type: " + locatorType + " was not found so, no data was sent to element")
            print_stack()

    def wait_for_element(self, locator, timeout =10, locatorType="id"):
        element = None
        try:
            byType = self.get_by_type(locatorType)
            print("waiting for maximum :" +str(timeout) + " seconds for the element")
            wait = WebDriverWait(self.driver, timeout, 0.5, ignored_exceptions=[TimeoutException, ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])
            element = wait.until(ec.presence_of_element_located((byType, locator)))
            print("Element was located on the webpage")
        except:
            print("Element was not located on the webpage")

        return element







