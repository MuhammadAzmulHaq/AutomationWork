from selenium import webdriver
from time import sleep

class Wishlist:
    def __init__(self, username, paswd):
        self.driver = webdriver.Chrome('C:/Users/Azmul/PycharmProjects/Qavashop/driver/chromedriver.exe')
        self.driver.get("https://staging.qavashop.com/en/bundles/rocket-appartamento-rocket-fausto-grinder.html")
        self.driver.find_element_by_xpath('/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[3]/button').click()
        sleep(4)
        self.username = username
        self.driver.find_element_by_xpath("//input[@name=\"email\"]") \
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]") \
            .send_keys(paswd)
        self.driver.find_element_by_xpath('//button[@type="submit"]') \
            .click()
        sleep(10)
        self.driver.quit()
        self.driver.close()

wish = Wishlist('taha@bargoventures.com','incorrect')