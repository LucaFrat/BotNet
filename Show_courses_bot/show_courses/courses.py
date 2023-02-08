import os
import time
import show_courses.constants as const
from show_courses.course_filtration import CourseFiltration

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Courses(webdriver.Chrome):
    def __init__(self, driver_path=const.CHROME_PATH, teardown=False) -> None:
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += const.CHROME_PATH
        super(Courses, self).__init__()
        self.implicitly_wait(15)

    def __exit__(self, *args):
        if self.teardown:
            self.quit()

    def open_url(self) -> None:
        self.implicitly_wait(15)
        self.get(const.URL)

    def select_english(self) -> None:
        english_button = self.find_element_by_class_name('icon-languageSwitch')
        english_button.click()

    def check_cookie(self) -> None:
        try:
            cookie = self.find_element_by_class_name('agree')
            cookie.click()
        except:
            print('No cookie appeared ...')
            WebDriverWait(self, 5).until(
                EC.text_to_be_present_in_element(
                    (By.XPATH, '/html/body/nav[1]/div/div/div/ul/li[1]/a'),
                    'Education'
                )
            )

    def go_to_page_to_make_choice(self):
        education_element = self.find_element_by_css_selector('a[href$="/education"]')
        education_element.click()
        programmes_element = self.find_element_by_css_selector('img[title="Programmes"]')
        programmes_element.click()

    def input_course_choice(self) -> None:
        time.sleep(1)
        self.minimize_window()
        course_possibilities = const.course_possibilities 
        string_courses = ', '.join(course_possibilities).capitalize()
        print('\nPage minimized, make your choice:')
        while True:
            course_choice = input(f"{string_courses}?\n").casefold()
            if isinstance(course_choice, str) and course_choice in course_possibilities:
                print('Okay!\n')
                break
            else:
                print(f'\033[41mInput failed\033[00m : \"{course_choice}\" is not a possible choice.')
                print('Choose among: ["Bachelors" - "Masters" - "PHD"]\n')
        #self.maximize_window()
        self.course_choice = course_choice
    
    def make_choice(self) -> None:
        choice_element = self.find_element_by_css_selector(f'a[href$="/{self.course_choice}"]')
        choice_element.click()

    def apply_filtration(self) -> None:
        filter = CourseFiltration(driver=self, choice=self.course_choice)
        filter.apply_filter()