# this file contains the class used to filtrate the courses
# given some keywords

from selenium.webdriver.remote.webdriver import WebDriver
import show_courses.constants as const
from dataclasses import dataclass


@dataclass(frozen=True)
class CourseFiltration:
    driver: WebDriver
    choice: str
    
    def apply_filter(self) -> None:
        if self.choice == const.COURSE_OPTIONS[0]:
            self.get_bachelor_courses()
        elif self.choice == const.COURSE_OPTIONS[1]: 
            self.get_master_courses()
        else: 
            self.get_phd_info()

    def get_bachelor_courses(self) -> None:
        whole_background = self.driver.find_element_by_xpath(
            '//*[@id="c472535"]/div/div/div'
            )
        boxxes = whole_background.find_elements_by_tag_name('h3')
        self.pprint(boxxes, index=0)
    
    def get_master_courses(self) -> None:
        self.driver.find_element_by_css_selector(
            'input[name="lookup[99822][filter][25][88]"]'
            ).click()
        agenda_element = self.driver.find_element_by_id('c99822')
        title_courses = agenda_element.find_elements_by_class_name('h3')
        self.pprint(title_courses, index=1)

    def get_phd_info(self) -> None:
        self.driver.find_element_by_css_selector(
            'a[href$="finding-a-position"]'
            ).click()
        phd_text_paragraph = self.driver.find_element_by_xpath('//*[@id="c35332"]/div/div/p')
        phd_text = phd_text_paragraph.get_attribute('innerHTML')
        print(f'{self.green("PHD availability")}:\n{phd_text}\n')
        

    def pprint(self, input_list: list, index: int) -> None:
        course_print = str(const.COURSE_OPTIONS[index][:-1]).capitalize()
        print(f'Here are the available {course_print} courses:')
        for i, input in enumerate(input_list):
            input_text = input.get_attribute("innerHTML")
            print(f'{self.green(str(i+1))}: {input_text}')
    
    def green(self, text: str) -> str:
        return f"\033[32m{text}\033[00m"

