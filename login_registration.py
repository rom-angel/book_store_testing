'''# слайд 95
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")

my_acc = driver.find_element_by_id("menu-item-50")
my_acc.click()
reg_email = driver.find_element_by_id("reg_email")
reg_email.send_keys("miwel94127@britted.com")
reg_password = driver.find_element_by_id("reg_password")
reg_password.send_keys("6fTC8@cW8sGhhyG")
register = driver.find_element_by_name("register")
register.click()
driver.quit()
'''

# слайд 96

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")

my_acc = driver.find_element_by_id("menu-item-50")
my_acc.click()
username = driver.find_element_by_id("username")
username.send_keys("miwel94127@britted.com")
password = driver.find_element_by_id("password")
password.send_keys("6fTC8@cW8sGhhyG")
login = driver.find_element_by_name("login")
login.click()
logout = WebDriverWait(driver, 20).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout"), "Logout"))
driver.quit()