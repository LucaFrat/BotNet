import os
import time
import show_courses.constants as const
import show_courses.course_filtration as filtr

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Courses(webdriver.Chrome):
    def __init__(self, driver_path=const.CHROME_PATH, 
                 teardown=False
                 ) -> None:
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += const.CHROME_PATH
        super(Courses, self).__init__()
        self.implicitly_wait(15)

    def __exit__(self, *args) -> None:
        if self.teardown:
            self.quit()

    def open_url(self) -> None:
        self.get(const.URL)
        self.input_visualization()
        
    def input_visualization(self) -> None:
        self.minimize_window()
        while True:
            show_web_page = str(input('\nDo you wanna show the Web page? [y/n]: '))
            if show_web_page == "y":
                self.show_web_page = True
                self.maximize_window()
                break
            elif show_web_page == "n":
                self.show_web_page = False
                break

    def select_english(self) -> None:
        self.find_element_by_class_name(
            'icon-languageSwitch'
            ).click()

    def check_cookie(self) -> None:
        try:
            self.find_element_by_class_name(
                'agree'
                ).click()
        except:
            print('No cookie appeared ...')
            WebDriverWait(self, 5).until(
                EC.text_to_be_present_in_element(
                    (By.XPATH, '/html/body/nav[1]/div/div/div/ul/li[1]/a'),
                    'Education'
                )
            )

    def go_to_page_to_make_choice(self) -> None:
        self.find_element_by_css_selector(
            'a[href$="/education"]'
            ).click()
        self.find_element_by_css_selector(
            'img[title="Programmes"]'
            ).click()

    def input_course_choice(self) -> None:
        time.sleep(1)
        self.minimize_window() 
        string_courses = ', '.join(const.COURSE_OPTIONS).capitalize()
        print('Page minimized, make your choice:')
        while True:
            course_choice = input(f"{string_courses}?\n").casefold()
            if isinstance(course_choice,str) and course_choice in const.COURSE_OPTIONS:
                print('Okay!\n')
                break
            else:
                print(f'\033[41mInput failed\033[00m : \"{course_choice}\" \
                       is not a possible choice.')
                print('Choose among: ["Bachelors" - "Masters" - "PHD"]\n')
        self.course_choice = course_choice

    def make_choice(self) -> None:
        self.find_element_by_css_selector(
            f'a[href$="/{self.course_choice}"]'
            ).click()

    def apply_filtration(self) -> None:
        filter = filtr.CourseFiltration(driver=self, choice=self.course_choice)
        filter.apply_filter()
        if self.show_web_page:
            self.maximize_window()
            time.sleep(2)
    