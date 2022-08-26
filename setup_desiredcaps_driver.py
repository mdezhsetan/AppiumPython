from appium import webdriver

def create_driver(appPackage, appActivity,port):
    desired_capabilities = {
        "deviceName": "Mahshad's A52",
        "udid": "RZ8T11EEMNJ",
        "platformName": "Android",
        "platformVersion": "12",
        "appPackage":  appPackage,
        "appActivity": appActivity
    }
    return webdriver.Remote('http://localhost:{0}/wd/hub'.format(port), desired_capabilities)
