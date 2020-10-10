from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class order():
    def __init__(self):
        self.driver = webdriver.Chrome('C:/Users/pc/PycharmProjects/BargoVen/drivers/chromedriver.exe')
        self.driver.get('https://staging.ekuep.com/en/login?back=history')
        self.driver.find_element_by_name('email').send_keys('azmulhaq+901@bargoventures.com')
        self.driver.find_element_by_name('password').send_keys('123456789')
        self.driver.save_screenshot("login.png")
        self.driver.find_element_by_id('submit-login').click()
        self.driver.implicitly_wait(10)

        # self.driver.get('https://staging.ekuep.com/en/coffee-makers/consumables/')
        self.driver.get('https://staging.ekuep.com/en/cooking-equipment/toasters-and-panini-grills/panini-grills/')
        sleep(4)

        # Hybrid supplier product
        # self.driver.find_element_by_xpath('/html/body/main/section/div[2]/div[2]/div[1]/section/section/div[3]/div[2]/div/div[4]/article/div[2]/div[7]/form/div/button').click()
        # sleep(30)

        # Bargo supplier product
        # self.driver.find_element_by_xpath('/html/body/main/section/div[2]/div[2]/div[1]/section/section/div[3]/div[2]/div/div[2]/article/div[2]/div[7]/form/div/button').click()
        # sleep(5)

        # ekuep product
        # consumable category
        # self.driver.find_element_by_xpath('/html/body/main/section/div[2]/div[2]/div[1]/section/section/div[3]/div[2]/div/div[9]/article/div[2]/div[7]/form/div/button').click()
        # cooking equipment
        self.driver.find_element_by_xpath(
            '/html/body/main/section/div[2]/div[1]/div[1]/section/section/div[3]/div[2]/div/div[1]/article/div[2]/div[7]/form/div/button').click()
        sleep(5)

        # Checkout
        self.driver.get('https://staging.ekuep.com/en/order')
        self.driver.implicitly_wait(20)

        # Address
        self.driver.find_element_by_xpath(
            '/html/body/main/section/div[2]/div/section/div/div[1]/div/section[2]/div/div/form/div[2]/button').click()

        # Order text
        self.driver.find_element_by_xpath(
            '/html/body/main/section/div[2]/div/section/div/div[1]/div/section[3]/div/div[2]/form/div/div[2]/div/textarea').send_keys(
            "Test order")

        # Continue Button
        self.driver.find_element_by_xpath(
            '/html/body/main/section/div[2]/div/section/div/div[1]/div/section[3]/div/div[2]/form/button').click()

        # Payment method Cash on Delivery
        self.driver.find_element_by_xpath('/html/body/main/section/div[2]/div/section/div/div[1]/div/section[4]/div/div[1]/div[3]/div/span').click()
        sleep(5)

        # Credit card
        # self.driver.find_element_by_xpath('/html/body/main/section/div[2]/div/section/div/div[1]/div/section[4]/div/div[1]/div[4]/div/span').click()
        # self.driver.find_element_by_xpath('//*[@id="modal-wrapper"]/div/div/div/form/div[1]/input').click()
        # self.driver.find_element_by_xpath('//*[@id="modal-wrapper"]/div/div/div/form/div[1]/input').send_keys('4242424242424242')
        # sleep(7)
        # self.driver.find_element_by_xpath(
        #    '/html/body/div/div/div/div/form/div[2]/div[1]/div/div/div[1]/input').send_keys('02')
        # sleep(7)
        # self.driver.find_element_by_xpath(
        #    '/html/body/div/div/div/div/form/div[2]/div[1]/div/div/div[1]/input').send_keys('22')
        # sleep(8)
        # self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/form/div[2]/div[2]/div').send_keys('100')
        # sleep(7)

        # WebDriverWait(self.driver, 20).until(
        #     EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//label[@for='payment-option-3']")))
        # WebDriverWait(self.driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//div[@id='payment-option-3-additional-information']"))).send_keys(
        #     "4242424242424242")
        # Checkout
        # self.driver.find_element_by_xpath(
        #     '/html/body/main/section/div[2]/div/section/div/div[1]/div/section[4]/div/div[2]/div[1]/button').click()
        # sleep(10)
        #
        # # 3D Secure
        # self.driver.get('https://api.sandbox.checkout.com/gwc-simulator/simulate/3ds/acs?authenticated=Y')
        # self.driver.find_element_by_xpath('/html/body/div[2]/div/form/div[1]/input').send_keys('Checkout1!')
        # sleep(10)
        #
        # self.driver.find_element_by_xpath('/html/body/div[2]/div/form/input').click()
        # sleep(8)
        
        self.driver.save_screenshot('checkout.png')
        self.driver.close()
        self.driver.quit()


x = order()
