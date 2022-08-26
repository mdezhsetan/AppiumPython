from appium import webdriver


class SetupDriver:
    def __init__(self):
        self.desired_capabilities = {
            "deviceName": "Mahshad's A52",
            "udid": "RZ8T11EEMNJ",
            "platformName": "Android",
            "platformVersion": "12",
            "appPackage": "com.sec.android.app.popupcalculator",
            "appActivity": "com.sec.android.app.popupcalculator.Calculator"
        }
        self.driver = webdriver.Remote('http://localhost:9999/wd/hub', self.desired_capabilities)
        print("setup")
