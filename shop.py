import time
from selenium import webdriver  # импортируем webdriver
from selenium.webdriver.support.select import Select  # импортируем класс Select или библиотеки webdriver element =
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(executable_path='C:/chromedriver')
driver.maximize_window()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

####################################################################################################################
# Shop1 отображение страницы товара
# 1 open url
driver.get("https://practice.automationtesting.in/")  # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# wait
driver.implicitly_wait(6)

# 2 login
driver.find_element_by_css_selector('#menu-item-50 > a').click()
driver.find_element_by_id("username").send_keys("warargout@gmail.com")
driver.find_element_by_id("password").send_keys("ghjnfkbyf")
time.sleep(2)  # ставим ожидание

# 3 click shop
driver.find_element_by_css_selector('#menu-item-40 > a').click()
time.sleep(2)  # ставим ожидание

# 4 click html5
driver.find_element_by_css_selector('a[data-product_id="181"]').click()
time.sleep(2)  # ставим ожидание

# 5 print header
header = driver.find_element_by_css_selector('#content > div > div:nth-child(2) > h1').text
print("\n", "Заголовок книги: ", header)

######################################################################################################################
# Shop2 количество товаров кв категории
# 1 open url
driver.get("https://practice.automationtesting.in/")  # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# wait
driver.implicitly_wait(6)

# 2 login
driver.find_element_by_css_selector('#menu-item-50 > a').click()
driver.find_element_by_id("username").send_keys("warargout@gmail.com")
driver.find_element_by_id("password").send_keys("ghjnfkbyf")
time.sleep(2)  # ставим ожидание

# 3 click shop
driver.find_element_by_css_selector('#menu-item-40 > a').click()
time.sleep(2)  # ставим ожидание

# 4 select html
driver.find_element_by_css_selector('.cat-item-19 > a').click()
time.sleep(2)  # ставим ожидание

# 5 print count
bks = len(driver.find_elements_by_class_name('status-publish'))
print('\n', "Книг найдено: ", bks)

#######################################################################################################################
# Shop3 сортировка товаров
# 1 open url
driver.get("https://practice.automationtesting.in/")  # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# wait
driver.implicitly_wait(6)

# 2 login
driver.find_element_by_css_selector('#menu-item-50 > a').click()
driver.find_element_by_id("username").send_keys("warargout@gmail.com")
driver.find_element_by_id("password").send_keys("ghjnfkbyf")
time.sleep(2)  # ставим ожидание

# 3 click shop
driver.find_element_by_css_selector('#menu-item-40 > a').click()
time.sleep(2)  # ставим ожидание

# 4 def order ?
SortType = driver.find_element_by_css_selector('option[selected="selected"]').get_attribute("value")

print("\n", "text ", SortType)
# print("\n", "text ", str(SortType))
assert EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.orderby > option[selected = "selected"]'), 'Default sorting')

# assert driver.find_element_by_css_selector('.orderby').value_of_css_property('value') == "menu_order"

# 5 sort by price down
SortOrd = driver.find_element_by_class_name('orderby')
Select(SortOrd).select_by_value("price-desc")
time.sleep(2)  # ставим ожидание

# 6 new old SortOrder
SortOrder = driver.find_element_by_css_selector('option[selected="selected"]')

# 7 order by price down?
SortType = SortOrder.get_attribute("value")
print("\n", "новая сортировка ", SortType)

#######################################################################################################################
# Shop4 отображение, скидка товара
driver.get("https://practice.automationtesting.in/")  # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# wait
driver.implicitly_wait(6)

# 2 login
driver.find_element_by_css_selector('#menu-item-50 > a').click()
driver.find_element_by_id("username").send_keys("warargout@gmail.com")
driver.find_element_by_id("password").send_keys("ghjnfkbyf")
time.sleep(2)  # ставим ожидание

# 3 click shop
driver.find_element_by_css_selector('#menu-item-40 > a').click()
time.sleep(2)  # ставим ожидание

# 4 select Android
driver.find_element_by_css_selector('img[title="Android Quick Start Guide"]').click()
time.sleep(2)  # ставим ожидание

# 5 old price 600
OldPr = driver.find_element_by_css_selector('.price > del > span').text
print("\n", "старая цена ", OldPr)
assert OldPr == "₹600.00"

# 6 new price 450
NewPr = driver.find_element_by_css_selector('.price > ins > span').text
print(" новая цена   ", OldPr)
assert NewPr == "₹450.00"

# 7 bookcase
WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[title="Android Quick Start Guide"]'))).click()
time.sleep(2)  # ставим ожидание, что б посмотреть

# 8 close bookcase
WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.pp_close'))).click()
time.sleep(2)  # ставим ожидание, что б посмотреть

######################################################################################################################
# Shop5 проверка цены в магазине
driver.get("https://practice.automationtesting.in/")  # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# wait
driver.implicitly_wait(6)

# 2 click shop
driver.find_element_by_css_selector('#menu-item-40 > a').click()
time.sleep(2)  # ставим ожидание

# 3 add html5 WA D to basket
driver.find_element_by_css_selector('a[data-product_id="182"]').click()
time.sleep(2)  # ставим ожидание

# 4 book 1? price 180?
BaskIt = driver.find_element_by_class_name('cartcontents').text
print("\n", "книг в корзине ", BaskIt)
assert BaskIt == "1 Item"

BaskPr = driver.find_element_by_css_selector('#wpmenucartli > a > span[class="amount"]').text
print(" стоимость кв корзине ", BaskPr)
assert BaskPr == "₹180.00"

# 5 to basket
driver.find_element_by_id('wpmenucartli').click()
time.sleep(2)  # ставим ожидание, что б посмотреть

# 6 subtotal
WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'td[data-title="Subtotal"] > span'))  )
time.sleep(2)  # ставим ожидание, что б посмотреть

# 7 total
WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'td[data-title="Total"] > strong > span'))  )
time.sleep(2)  # ставим ожидание, что б посмотреть

######################################################################################################################
# Shop6 работа в корзине
driver.get("https://practice.automationtesting.in/")  # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# wait
driver.implicitly_wait(6)

# 2 click shop
driver.find_element_by_css_selector('#menu-item-40 > a').click()
time.sleep(2)  # ставим ожидание, что б посмотреть

# 3 add html5 WA D and JS D S a A to basket
driver.find_element_by_css_selector('a[data-product_id="182"]').click() #html5 WA D to basket
time.sleep(2)  # ставим ожидание
driver.find_element_by_css_selector('a[data-product_id="180"]').click() #JS D S a A to basket
time.sleep(2)  # ставим ожидание

# 4 to basket
driver.find_element_by_id('wpmenucartli').click()
time.sleep(2)  # ставим ожидание, что б посмотреть

# 5 del html5
driver.find_element_by_css_selector('a[data-product_id="182"]').click()
time.sleep(2)  # ставим ожидание, что б посмотреть

# 6 undo del
driver.find_element_by_link_text('Undo?').click()
time.sleep(2)  # ставим ожидание, что б посмотреть

# 7 JS count -> 3
CountJS = driver.find_element_by_css_selector('.cart > tbody > tr:nth-child(2) > td:nth-child(5) > div > input')
CountJS.clear()
CountJS.send_keys(3)
time.sleep(2)  # ставим ожидание, что б посмотреть

# 8 update basket
driver.find_element_by_css_selector('[value="Update Basket"]').click()
time.sleep(2)  # ставим ожидание, что б посмотреть

# 9 JS 3?
# NumberJS = CountJS.value_of_css_property("value")
CountJS = driver.find_element_by_css_selector('.cart > tbody > tr:nth-child(2) > td:nth-child(5) > div > input')
NumberJS = CountJS.get_attribute('value')
print("\n", "количество книг JS ", NumberJS)
assert  NumberJS == "3"

# 10 Applay coupon
time.sleep(2)  # ставим ожидание, на этот раз по заданию
driver.find_element_by_css_selector('[name="apply_coupon"]').click()

# 11 Please enter ?
ErrTx = driver.find_element_by_css_selector('.woocommerce-error > li').text
print("\n", "Текст ошибки ", "\n", ErrTx)
assert ErrTx == "Please enter a coupon code."

################################################################################################################
# Shop7 покупка товара
driver.get("https://practice.automationtesting.in/")  # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# wait
driver.implicitly_wait(6)

# 2 click shop
driver.find_element_by_css_selector('#menu-item-40 > a').click()
driver.execute_script("window.scrollBy(0, 300);") # проскроллитm страницу на 300 пикселей вниз

# 3 add html5 WA D to basket
driver.find_element_by_css_selector('a[data-product_id="182"]').click() #html5 WA D to basket
time.sleep(1)  # ставим ожидание, тут надо

# 4 to basket
driver.find_element_by_id('wpmenucartli').click()

# 5 proceed
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.checkout-button'))).click()

# 6 fill *
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'billing_first_name'))).send_keys("Yurec")
driver.find_element_by_id('billing_last_name').send_keys('Tkachev')
driver.find_element_by_id('billing_email').send_keys('warargout@gmail.com')
driver.find_element_by_id('billing_phone').send_keys('5500 8800')

driver.find_element_by_id('s2id_billing_country').click() #нажать селектор страны
driver.find_element_by_id('s2id_autogen1_search').send_keys('rus') #поиск по имени
driver.find_element_by_css_selector('#select2-results-1 > li:nth-last-child(1)').click() #выбрали результат

driver.find_element_by_id('billing_address_1').send_keys('1st square, 1')
driver.find_element_by_id('billing_city').send_keys('Krasnodar')
driver.find_element_by_id('billing_state').send_keys('Krasnodarskiy kray')
driver.find_element_by_id('billing_postcode').send_keys('350000')

# 7 payment
driver.execute_script("window.scrollBy(0, 600);") # проскроллитm страницу на 300 пикселей вниз
time.sleep(2)  # ставим ожидание, по заданию
driver.find_element_by_id('payment_method_cheque').click()

# 8 place order
driver.find_element_by_id('place_order').click()

# 9 thanks ?
ThTx = driver.find_element_by_css_selector('#page-35 > div > div > p').text
print(ThTx)
assert ThTx == "Thank you. Your order has been received."

# 10 Check Payments ?
PMTx = driver.find_element_by_css_selector('.order_details > tfoot > tr:nth-child(3) > td').text
print(PMTx)
assert PMTx == "Check Payments"
time.sleep(3)  # ставим ожидание, что б посмотреть

driver.quit()