from selenium.webdriver.common.by import By

from desired_capabilities import SetupDriver


class CalculatorTest(SetupDriver):
    def __init__(self):
        super().__init__()

    def openningCalculator(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.ID, 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_02').click()
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Multiplication"]').click()
        self.driver.find_element(By.ID, 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_06').click()
        self.driver.find_element(By.ID, 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_equal').click()
