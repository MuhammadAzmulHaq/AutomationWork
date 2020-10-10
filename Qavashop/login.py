from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Order:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome('C:/Users/Azmul/PycharmProjects/Qavashop/driver/chromedriver.exe')
        self.username = username
        self.driver.get("https://staging.qavashop.com/en/my-account")
        self.driver.find_element_by_xpath("//input[@name=\"email\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        self.driver.get('https://staging.qavashop.com/en/merchandise/')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('/html/body/main/section/div[2]/div/div[1]/section/section/div[3]/div[2]/div[1]/div[3]/article/div[2]/div[6]/form/div/button')\
            .click()
        sleep(4)
        self.driver.get('https://staging.qavashop.com/en/order')
        sleep(4)
        # Address
        self.driver.find_element_by_xpath('/html/body/main/section/div[2]/div/section/div/div[1]/section[2]/div/div/form/div[2]/button')\
            .click()
        sleep(4)
        # Shipping_method
        self.driver.find_element_by_id('delivery_message').send_keys("test order")
        sleep(4)
        self.driver.find_element_by_xpath('/html/body/main/section/div[2]/div/section/div/div[1]/section[3]/div/div[2]/form/button').click()
        sleep(5)
        # Payment Selection
        wait = WebDriverWait(self.driver, 10)
        self.driver.switch_to.frame("singleIframe")
        wait.until(EC.element_to_be_clickable((By.ID, "checkout-frames-card-number"))).click()
        sleep(4)
        self.driver.find_element_by_id('checkout-frames-card-number').send_keys("4242424242424242")
        sleep(1)
        self.driver.find_element_by_id('checkout-frames-expiry-date').send_keys("0222")
        sleep(1)
        self.driver.find_element_by_id('checkout-frames-cvv').send_keys("100")
        sleep(4)
        # Checkout_Button
        self.driver.find_element_by_xpath('/html/body/main/section/div[2]/div/section/div/div[1]/section[4]/div/div[3]/div[1]').click()

        ## 3D secure
        self.driver.get('https://3ds2-sandbox.ckotech.co/interceptor/3ds_snbk27qxl5fe3dsgmvl6lpxirq/device-information')
        self.driver.implicitly_wait(30)
        # #hint
        self.driver.find_element_by_id('password').send_keys("Checkout1!")
        sleep(2)
        self.driver.find_element_by_id('txtButton').click()
        sleep(5)
        self.driver.close()


my_bot = Order('taha@bargoventures.com', 'incorrect')
