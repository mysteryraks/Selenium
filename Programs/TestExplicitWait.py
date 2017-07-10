from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
from Programs.helpers import Helpers


class Test(Helpers):

    def __init__(self):
        driver_location = "/Users/AshaRakesh/PycharmProjects/Selenium/configfiles/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driver_location
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(30)

    def login(self):
        self.driver.get("https://easy.techmahindra.com")
        try:
            wait = WebDriverWait(self.driver, 30, 1, ignored_exceptions=[NoSuchElementException])
            wait.until(EC.presence_of_element_located((By.NAME, "txtLanId")))
            self.driver.find_element(By.NAME, "txtLanId").send_keys("rr0023714")
            self.driver.find_element(By.NAME, "txtPassword").send_keys("Trinity@062017")
            self.driver.find_element(By.NAME, "btnlogin").click()
            wait.until(EC.title_contains, "EASY - Easy Access System For You")
            parent = self.driver.current_window_handle
            wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'My Time')]")))
            self.driver.find_element_by_xpath("//p[contains(text(), 'My Time')]").click()
            time.sleep(5)
            #handles = self.driver.window_handles
            #print(handles)
            #for handle in handles:
            #    if handle not in parent:
            #        self.driver.switch_to_window(handle)
            #        print("switched to time window")
            Helpers._switch_to_new_window(self.driver)

            # old_handle = self.driver.window_handles[0]
            # new_handle = self.driver.window_handles[1]
            # print(old_handle)
            # print(new_handle)
            # self.driver.switch_to_window(new_handle)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#ctl00_CPH_chkAcknow")))
            assert "MyTime" in self.driver.title
            self.driver.find_element_by_css_selector("input#ctl00_CPH_chkAcknow").click()
            time.sleep(5)
            print("Test Passed")
        except TimeoutException:
            print("waited for too long...")
        finally:
            self.driver.quit()


    def screentest(self):

        self.driver.get("https://facebook.com")
        time.sleep(5)


if __name__ == '__main__':
    test = Test()
    test.login()
    test.screentest()



