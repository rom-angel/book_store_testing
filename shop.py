# слайд 97
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")

my_acc = driver.find_element_by_id("menu-item-50")
my_acc.click()
username = driver.find_element_by_id("username")
username.send_keys("miwel94127@britted.com")
password = driver.find_element_by_id("password")
password.send_keys("6fTC8@cW8sGhhyG")
login = driver.find_element_by_name("login")
login.click()
shop = driver.find_element_by_id("menu-item-40")
shop.click()
book3 = driver.find_element_by_css_selector(".products.masonry-done > li:nth-child(3)")
book3.click()
html5_forms = WebDriverWait(driver, 20).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".summary.entry-summary"), "HTML5 Forms"))
driver.quit()


# слайд 98
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")

my_acc = driver.find_element_by_id("menu-item-50")
my_acc.click()
username = driver.find_element_by_id("username")
username.send_keys("miwel94127@britted.com")
password = driver.find_element_by_id("password")
password.send_keys("6fTC8@cW8sGhhyG")
login = driver.find_element_by_name("login")
login.click()
shop = driver.find_element_by_id("menu-item-40")
shop.click()
html = driver.find_element_by_css_selector(".product-categories > li:nth-child(2)")
html.click()
items_count = (len(driver.find_elements_by_css_selector(".products.masonry-done")), 3)
if len(items_count) == 3:
    print("Отображается 3 товара")
else:
    print("Ошибка")
# выводится ошибка(
driver.quit()


# слайд 99

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")

my_acc = driver.find_element_by_id("menu-item-50")
my_acc.click()
username = driver.find_element_by_id("username")
username.send_keys("miwel94127@britted.com")
password = driver.find_element_by_id("password")
password.send_keys("6fTC8@cW8sGhhyG")
login = driver.find_element_by_name("login")
login.click()
shop = driver.find_element_by_id("menu-item-40")
shop.click()
order_selector = driver.find_element_by_class_name("orderby")
select = Select(order_selector)
order_selector_def = order_selector.get_attribute("value")
if order_selector_def == "price-desc":
    print("в селекторе выбран вариант сортировки от большего к меньшему")
else:
    print("выбран дефолтный вариант сортировки")
select.select_by_value("price-desc")
order_selector = driver.find_element_by_class_name("orderby")
select = Select(order_selector)
order_selector_hl = order_selector.get_attribute("value")
if order_selector_hl == "price-desc":
    print("выбран вариант сортировки от большего к меньшему")
else:
    print("выбран дефолтный вариант сортировки")
driver.quit()


# слайд 100

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")

my_acc = driver.find_element_by_id("menu-item-50")
my_acc.click()
username = driver.find_element_by_id("username")
username.send_keys("miwel94127@britted.com")
password = driver.find_element_by_id("password")
password.send_keys("6fTC8@cW8sGhhyG")
login = driver.find_element_by_name("login")
login.click()
shop = driver.find_element_by_id("menu-item-40")
shop.click()
aqsg = driver.find_element_by_css_selector(".products > li:nth-child(1)")
aqsg.click()
old_price = driver.find_element_by_css_selector(".price > del > span")
old_price_get_text = old_price.text
assert old_price_get_text == "₹600.00"
new_price = driver.find_element_by_css_selector("ins > span")
new_price_get_text = new_price.text
assert new_price_get_text == "₹450.00"
image = driver.find_element_by_class_name("images")
image.click()
#при добавлении time.sleep() тест падает, но проходит и без него
pp_close = driver.find_element_by_css_selector(".pp_pic_holder.pp_woocommerce > div .pp_close")
pp_close.click()
driver.quit()


# слайд 101

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")

shop = driver.find_element_by_id("menu-item-40")
shop.click()
book4_add_basket = driver.find_element_by_css_selector(".products > li:nth-child(4) > a:nth-child(2)")
book4_add_basket.click()
item = driver.find_element_by_css_selector(".wpmenucart-contents .cartcontents")
item_get_text = item.text
assert item_get_text == "1 Item"
price = driver.find_element_by_css_selector("#wpmenucartli .amount")
price_get_text = price.text
assert price_get_text == "₹180.00"
basket = driver.find_element_by_id("wpmenucartli")
basket.click()
subtotal = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "cart-subtotal"), "180.00"))
total = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "order-total"), "189.00"))
driver.quit()


# слайд 102

import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")

shop = driver.find_element_by_id("menu-item-40")
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
book4_add_basket = driver.find_element_by_css_selector(".products > li:nth-child(4) > a:nth-child(2)")
book4_add_basket.click()
time.sleep(3)
book7_add_basket = driver.find_element_by_css_selector(".products > li:nth-child(5) > a:nth-child(2)")
book7_add_basket.click()
basket = driver.find_element_by_id("wpmenucartli")
basket.click()
time.sleep(3)
#не удается удалить книгу из корзины
remove_book4 = driver.find_element_by_css_selector(".shop_table.shop_table_responsive .cart_item")
remove_book4.click()
time.sleep(10)
#кнопка ундо не появляется - тест падает
undo = driver.find_element_by_css_selector(".woocommerce > .woocommerce-message > a")
undo.click()
quantity = driver.find_element_by_css_selector(".cart_item .quantity")
quantity.clear()
driver.quit()
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://practice.automationtesting.in/")

shop = driver.find_element_by_id("menu-item-40")
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
book4_add_basket = driver.find_element_by_css_selector(".products > li:nth-child(4) > a:nth-child(2)")
book4_add_basket.click()
basket = driver.find_element_by_id("wpmenucartli")
basket.click()
proceed_to_checkout = driver.find_element_by_css_selector(".checkout-button.button.alt.wc-forward")
proceed_to_checkout.click()
first_name = driver.find_element_by_id("billing_first_name")
first_name.send_keys("Иван")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Иванов")
email_address = driver.find_element_by_id("billing_email")
email_address.send_keys("miwel94127@britted.com")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("9999999999")
#country = driver.find_element_by_id("s2id_billing_country")
#country.click()
#input_country = driver.find_element_by_id("s2id_autogen1_search")
#input_country.send_keys("Mont")
#не удается выбрать страну, ниже введенной
#displayed_country = driver.find_element_by_class_name("select2-result-label-677")
#displayed_country.click()
check_payments = driver.find_element_by_id("payment_method_cheque")
driver.execute_script("window.scrollBy(0, 600);")
check_payments.click()
place_order = driver.find_element_by_id("place_order")
place_order.click()
text1 = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
text2= WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order_details > li:nth-child(4)"), "Check Payments"))
driver.quit()

