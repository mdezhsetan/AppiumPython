from selenium.webdriver.common.by import By

from setup_desiredcaps_driver import create_driver
from screenshot import ScreenshotHelper


class CalculatorTest:
    def __init__(self):
        self.driver = create_driver(appPackage="com.sec.android.app.popupcalculator",
                                    appActivity="com.sec.android.app.popupcalculator.Calculator", port=9999)
        self.screenshot_helper = ScreenshotHelper(self.driver)

    def multiplicationTest(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.ID, 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_02').click()
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Multiplication"]').click()
        self.driver.find_element(By.ID, 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_06').click()
        equal_btn = self.driver.find_element(By.ID, 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_equal')
        equal_btn.click()
        self.createScreenshot()

    def createScreenshot(self):
        self.screenshot_helper.takeScreenshot()
