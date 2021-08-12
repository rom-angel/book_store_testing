# слайд 94
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")

driver.execute_script("window.scrollBy(0, 600);")
selenium_ruby = driver.find_element_by_css_selector(".product_tag-ruby h3")
selenium_ruby.click()
reviews = driver.find_element_by_css_selector(".tabs.wc-tabs > .reviews_tab")
time.sleep(3)
reviews.click()
stars = driver.find_element_by_css_selector(".stars .star-5")
time.sleep(3)
stars.click()
textarea = driver.find_element_by_id("comment")
textarea.send_keys("Nice book!")
name = driver.find_element_by_id("author")
name.send_keys("Name")
email = driver.find_element_by_id("email")
email.send_keys("11@gmail.com")
submit = driver.find_element_by_id("submit")
submit.click()
driver.quit()