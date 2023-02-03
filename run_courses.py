import os
import Show_courses.constants as c
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


os.environ['PATH'] += c.CHROME_PATH
driver = webdriver.Chrome()
driver.get("https://www.tudelft.nl")
driver.implicitly_wait(15)

english_button = driver.find_element_by_class_name('icon-languageSwitch')
english_button.click()

try:
    cookie = driver.find_element_by_class_name('agree')
    cookie.click()
except:
    print('No cookie appeared ...')

WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element(
        (By.XPATH, '/html/body/nav[1]/div/div/div/ul/li[1]/a'),
        'Education'
    )
)

education_element = driver.find_element_by_css_selector('a[href$="/education"]')
education_element.click()

programmes_element = driver.find_element_by_css_selector('img[title="Programmes"]')
programmes_element.click()

master_element = driver.find_element_by_css_selector('a[href$="/masters"]')
master_element.click()