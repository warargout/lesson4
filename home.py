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
# Home1 добавление комментария
# 1 open url
driver.get("https://practice.automationtesting.in/")  # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# wait
driver.implicitly_wait(6)

# 2 to Win
driver.execute_script("window.scrollBy(0, 600);") # проскроллитm страницу на 600 пикселей вниз

# 3 click READ MORE
driver.find_element_by_css_selector('a[data-product_id="163"]').click()
time.sleep(2)  # ставим ожидание

# 4 click REVIEWV
driver.find_element_by_css_selector('a[href="#tab-reviews"]').click()
time.sleep(2)  # ставим ожидание

# 5 rate 5*
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(2)  # ставим ожидание
driver.find_element_by_css_selector('.stars > span > a:nth-child(5)').click()
time.sleep(2)  # ставим ожидание

# 6 write nice book
driver.find_element_by_id("comment").send_keys("Nice Book!")
time.sleep(2)  # ставим ожидание

# 7 fill name
driver.find_element_by_id("author").send_keys("Yurec")
time.sleep(2)  # ставим ожидание

# 8 fill email
driver.find_element_by_id("email").send_keys("warargout@gmail.com")
time.sleep(2)  # ставим ожидание

# 9 click SUBMIT
driver.find_element_by_id("submit").click()
time.sleep(5)  # ставим ожидание

######################################################################################################################

# driver.quit()