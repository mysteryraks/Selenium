from selenium.common.exceptions import TimeoutException
import time
import os


class Helpers(object):

    @staticmethod
    def _switch_to_new_window(driver):
        old_window = driver.window_handles[0]
        new_window = driver.window_handles[1]
        try:
            driver.switch_to_window(new_window)
            print("switch to new window")
            time.sleep(2)
        except TimeoutException:
            print("invalid window-->could not switch")

    @staticmethod
    def __switch_to_parent_window(driver):
        old_window = driver.window_handles[0]
        new_window = driver.window_handles[1]
        try:
            driver.switch_to_window(old_window)
            print("switched to parent window")
            time.sleep(2)
        except TimeoutException:
            print("invalid window-->could not switch")


    @staticmethod
    def _get_screenshot(driver, testName):
        time_here = time.localtime()
        time_list = [str(time_here[1]), str(time_here[2]), str(time_here[3]), str(time_here[4])]
        time_list = '.'.join(time_list)
        fileName = testName + time_list + '.png'
        screenshotDirectory = "/Users/AshaRakesh/PycharmProjects/Programs/"

        try:
            if os.path.exists(screenshotDirectory):
                driver.save_screenshot(screenshotDirectory+fileName)
                print("screenshot obtained with filename: " +fileName)
        except:
            print("some error while taking screenshot...")


