from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Firefox()
driver.get("http://10.154.10.38/")
driver.find_element_by_id("cui-focusable").send_keys("root")
driver.find_element_by_name("cuiPassword").send_keys("123")
time.sleep(10)
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(10)
driver.find_element_by_link_text("Users").click()
driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
driver.find_element_by_id("contAddTICUser").click()
driver.find_element_by_id("popICUserUserName").send_keys("t_user")
driver.find_element_by_id("popICUserFullName").send_keys("test user")
driver.find_element_by_id("popICUserEmail").send_keys("t_user@mail.com")
driver.find_element_by_id("popICUserPassword").send_keys("123")
driver.find_element_by_id("popICUserConfPassword").send_keys("123")
driver.find_element_by_id("popICUserCreate").click()
time.sleep(5)
text=driver.find_element_by_id("contUserListt_user").text
print(text)
if text == "t_user (test user)":
	print("PASS,create user successful!")
else:
	print("FAIL,create user fail!")
driver.find_element_by_xpath("//li[4]/cui-navigation-list-item/div/ul/li/cui-navigation-list-item/a/span").click()
time.sleep(10)
driver.find_element_by_xpath("//li[@id='contUserListt_user']/div/div/div/span").click()
time.sleep(10)
driver.find_element_by_id("contRemoveUser").click()
driver.find_element_by_xpath("(//button[@type='button'])[10]").click()



