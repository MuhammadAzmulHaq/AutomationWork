from selenium import webdriver
import time


# open chrome browser
app = webdriver.Chrome(executable_path="C:/Users/pc/PycharmProjects/vidizmo/drivers/chromedriver.exe")


# set implicit time to 20 seconds
app.implicitly_wait(10)


# navigate to the url
app.get("http://automation-test.beta.vidizmo.com/home")
app.find_element_by_class_name("text-white").click()


# login
app.find_element_by_id("EmailAddress").send_keys("automation-tester@sharklasers.com")
app.find_element_by_id("Password").send_keys("Test@123")
app.find_element_by_id("Signin").click()
time.sleep(1)

#search by title
app.find_element_by_name("top-search").send_keys("Video")
app.find_element_by_xpath("//*[@id='page-wrapper']/topbar-navigation/nav/div/div/div[2]/form/div/span/button").click()
app.find_element_by_xpath("//*[@id='mashupId-139650']/div/div/div/div[2]/div[1]/div[1]/va/a").click()
time.sleep(10)

#commnet_post
app.find_element_by_xpath("(//textarea[@name='newComment'])[2]").send_keys("azmul")
#post_button
app.find_element_by_xpath("//*[@id='page-wrapper']/playback-page/div/div/div/div/main/div[3]/div[2]/div/comment-add-edit/div/div[2]/div/div[1]/div/form/div/button[1]").click()
#eidt
app.find_element_by_xpath("//*[@id='page-wrapper']/playback-page/div/div/div/div/main/div[3]/div[2]/div/comment-add-edit/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/a[2]/i").click()
app.find_element_by_xpath("(//textarea[@name='newComment'])[2]").send_keys("azmul haq")
#update
app.find_element_by_xpath("//*[@id='page-wrapper']/playback-page/div/div/div/div/main/div[3]/div[2]/div/comment-add-edit/div/div[2]/div/div[2]/div[1]/form/div/button[1]").click()
#delete
app.find_element_by_xpath("//*[@id='page-wrapper']/playback-page/div/div/div/div/main/div[3]/div[2]/div/comment-add-edit/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/a[1]/i").click()

#logout
app.find_element_by_xpath("//*[@id='page-wrapper']/topbar-navigation/nav/div/div/ul[1]/li[4]/a/span").click()
app.find_element_by_xpath("//a[contains(text(),'Sign Out')]").click()


#close browser
app.close()
app.quit()