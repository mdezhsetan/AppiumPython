import os
import time


class ScreenshotHelper():
    def __init__(self, driver):
        self.driver = driver

    def takeScreenshot(self):
        current_time = time.strftime("%Y_%m_%d_%H%M%S")
        print(current_time)
        activity = self.driver.current_activity
        print(activity)
        self.driver.save_screenshot("{0}\screenshots\{1}.png".format(os.getcwd(),current_time))