from selenium import webdriver
from time import sleep


class Order_flow:
    def __init__(self):
        self.driver = webdriver.Chrome('C:/Users/pc/PycharmProjects/BargoVen/drivers/chromedriver.exe')
        self.driver.get("https://staging.qavashop.com/en/my-account")
        self.driver.find_element_by_xpath("//input[@name=\"email\"]")\
            .send_keys('azmulhaq+901@bargoventures.com')
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys('123456789')
        self.driver.save_screenshot('login_qava.png')
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(5)


        # Select Product form Category
        self.driver.get('https://staging.qavashop.com/en/brewing-bar/')
        self.driver.implicitly_wait(30)

        # Qavashop Product
        self.driver.find_element_by_xpath('/html/body/main/section/div[2]/div/div[1]/section/section/div[3]/div[2]/div[1]/div[3]/article/div[2]/div[6]/form/div/button')\
            .click()
        sleep(4)

        # Checkout
        self.driver.get('https://staging.qavashop.com/en/order')
        sleep(4)

        # Address
        self.driver.find_element_by_xpath('/html/body/main/section/div[2]/div/section/div/div[1]/section[2]/div/div/form/div[2]/button').click()
        sleep(4)

        # Shipping message
        self.driver.find_element_by_xpath('/html/body/main/section/div[2]/div/section/div/div[1]/section[3]/div/div[2]/form/div/div[2]/div/textarea').send_keys(" Test Order ")
        sleep(4)

        # Continue Button
        self.driver.find_element_by_xpath('/html/body/main/section/div[2]/div/section/div/div[1]/section[3]/div/div[2]/form/button').click()
        sleep(4)

        # Checkout Button
        self.driver.find_element_by_xpath('/html/body/main/section/div[2]/div/section/div/div[1]/section[4]/div/div[3]/div[1]/button').click()
        sleep(5)

        self.driver.save_screenshot('Qavashop_checkout.png')
        self.driver.close()
        self.driver.quit()


my_order = Order_flow()