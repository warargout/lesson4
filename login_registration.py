import time
from selenium import webdriver  # импортируем webdriver
from selenium.webdriver.support.select import Select  # импортируем класс Select или библиотеки webdriver element =
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(executable_path='C:/chromedriver')
driver.maximize_window()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#####################################################################################################################
# # Reg1 регистрация аккаунта
# # 1 open url
# driver.get("https://practice.automationtesting.in/")  # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# # wait
# driver.implicitly_wait(6)
#
# # 2 click MY MENU
# driver.find_element_by_css_selector('#menu-item-50 > a').click()
# time.sleep(2)  # ставим ожидание
#
# # 3 fill email
# driver.find_element_by_id("reg_email").send_keys("warargout@gmail.com")
# time.sleep(2)  # ставим ожидание
#
# # 4 fill password
# driver.find_element_by_id("reg_password").send_keys("ghjnfkbyf")
# time.sleep(2)  # ставим ожидание
#
# # 5 register
# driver.find_element_by_css_selector('input[name="register"]').click()
# time.sleep(2)  # ставим ожидание

#######################################################################################################################
# # Reg2 логин
# # 1 open url
# driver.get("https://practice.automationtesting.in/")  # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# # wait
# driver.implicitly_wait(6)
#
# # 2 click MY MENU
# driver.find_element_by_css_selector('#menu-item-50 > a').click()
# time.sleep(2)  # ставим ожидание
#
# # 3 fill email
# driver.find_element_by_id("username").send_keys("warargout@gmail.com")
# time.sleep(2)  # ставим ожидание
#
# # 4 fill password
# driver.find_element_by_id("password").send_keys("ghjnfkbyf")
# time.sleep(2)  # ставим ожидание
#
# # 5 login
# driver.find_element_by_css_selector('input[name="login"]').click()
# time.sleep(2)  # ставим ожидание
#
# # 6 logaut?
# driver.find_element_by_css_selector('#menu-item-50 > a').click()
# time.sleep(2)  # ставим ожидание
#
# assert EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'a[href="https://practice.automationtesting.in/my-account/customer-logout/"]'), 'logaut')

########################################################################################################################

driver.quit()