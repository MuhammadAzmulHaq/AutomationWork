from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_option = Options()
chrome_option.add_argument("__disable-user-media-security=true")
# open chrome browser
app = webdriver.Chrome(executable_path="C:/Users/pc/PycharmProjects/vidizmo/drivers/chromedriver.exe", chrome_options=chrome_option)

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


#uploading_video_icon
app.find_element_by_xpath("//*[@id='small-chat']/a/span/i[2]").click()
#click_
app.find_element_by_xpath("//*[@id='page-wrapper']/admin-media-manager/add-media-component/main/div/div/div[1]/a/div/div/div[2]/p").click()
app.find_element_by_id("uploadCtrl").send_keys("C:/Users/pc/PycharmProjects/vidizmo/Scenario_5/Anger_Management.mp4")
#save_close
app.find_element_by_xpath("//*[@id='page-wrapper']/admin-media-manager/mashup-upload-page/div/main/mashup-upload/section/div[3]/div[2]/div[2]/mashups-setting/section/div/div/div/form/div[2]/div/div/button[2]").click()
time.sleep(2)

#workflow
app.find_element_by_xpath("//*[@id='page-wrapper']/topbar-navigation/nav/div/div/div[1]/a").click()
app.find_element_by_xpath("//*[@id='side-menu']/li[4]/ul/li[4]/a/i").click()
app.find_element_by_xpath("//*[@id='page-wrapper']/control-panel-page/main/div/div[1]/aside/div/div[2]/div[2]/accordion/div[7]/ul/li/a/i").click()

#logout
app.find_element_by_xpath("//*[@id='page-wrapper']/topbar-navigation/nav/div/div/ul[2]/li[4]/a").click()
app.find_element_by_xpath("//a[contains(text(),'Sign Out')]").click()

app.close()
app.quit()