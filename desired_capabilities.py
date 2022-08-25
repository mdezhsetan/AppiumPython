from appium import webdriver

desired_capibilities = {
    "deviceName": "Mahshad's A52",
    "udid": "RZ8T11EEMNJ",
    "platformName": "Android",
    "platformVersion": "12",
    "appPackage": "com.sec.android.app.popupcalculator",
    "appActivity": "com.sec.android.app.popupcalculator.Calculator"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capibilities)
