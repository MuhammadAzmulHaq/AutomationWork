import unittest
from appium import webdriver


class AppiumTest(unittest.TestCase):
    dc = {}
    driver = None

    def setUp(self):
        # This is the Application and ‘app’ desired capability to specify a path to Appium.
        self.dc['app'] = "F:\\Appium\\eribank.apk"
        # appPackage and appActivity desired capability specify app details to Appium
        self.dc['appPackage'] = "com.experitest.ExperiBank"
        self.dc['appActivity'] = ".LoginActivity"
        # platformName desired capability specify platform detail to Appium
        self.dc['platformName'] = 'Android'
        # device id is got from running adb devices command in PC
        self.dc['deviceName'] = 'a3ae1c63'
        # Creating the Driver by passing Desired Capabilities.
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.dc)

    def testFirstAutomationTest(self):
        if len(self.driver.find_elements_by_xpath("//*[@ text=’OK’]")) > 0:
            self.driver.find_element_by_xpath("//*[ @ text =’OK’]").click()
            # Find location of Elements and perform actions.
            self.driver.find_element_by_xpath("//*[ @ text =’Username’]").send_keys('company')
            self.driver.find_element_by_xpath("//*[ @ text =’Password’]").send_keys('company')
            self.driver.find_element_by_xpath("//*[ @ text =’Login’]").click()

    # Function to Release the driver
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
