import unittest
from selenium import webdriver
from time import sleep


class Test(unittest.TestCase):
    def test(self):
        self.driver = webdriver.Chrome('C:/Users/pc/PycharmProjects/BargoVen/drivers/chromedriver.exe')
        self.driver.get("https://www.google.com/")
        self.driver.implicitly_wait(30)
        titleofwebpage = self.driver.title

        # Assert Equal
        # self.assertEqual("Google", titleofwebpage, 'Web page title is same')
        # sleep(5)

        # Assert Not Equal
        self.assertNotEqual("Google336", titleofwebpage, 'Web page title is not same')

if __name__ == "__main__":
    unittest.main()
