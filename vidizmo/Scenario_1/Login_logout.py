from selenium import webdriver

# open chrome browser
app = webdriver.Chrome(executable_path="C:/Users/pc/PycharmProjects/vidizmo/drivers/chromedriver.exe")

# set implicit time to 20 seconds
app.implicitly_wait(20)
app.maximize_window()

# navigate to the url
app.get("http://automation-test.beta.vidizmo.com/home")
app.find_element_by_class_name("text-white").click()

# login
app.find_element_by_id("EmailAddress").send_keys("automation-tester@sharklasers.com")
app.find_element_by_id("Password").send_keys("Test@123")
app.find_element_by_id("Signin").click()

#logout
app.find_element_by_xpath("//*[@id='page-wrapper']/topbar-navigation/nav/div/div/ul[2]/li[4]/a/span").click()
app.find_element_by_xpath("//a[contains(text(),'Sign Out')]").click()

app.close()
app.quit()