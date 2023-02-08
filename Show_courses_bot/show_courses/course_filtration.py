# this file contains the class used to filtrate the courses
# given some keywords

from selenium.webdriver.remote.webdriver import WebDriver
import show_courses.constants as const
from dataclasses import dataclass


@dataclass(frozen=True)
class CourseFiltration:
    driver: WebDriver
    choice: str

    def apply_filter(self):
        if self.choice == const.course_possibilities[0]: 
            self.get_bachelor_courses()
        elif self.choice == const.course_possibilities[1]: 
            self.get_master_courses()
        else: 
            self.get_phd_info()

    def get_bachelor_courses(self) -> None:
        self.driver.find_elements_by_tag_name
        whole_backround = self.driver.find_element_by_xpath('//*[@id="c472535"]/div/div/div')
        boxxes = whole_backround.find_elements_by_tag_name('h3')
        print('Here are the available Bachelor courses:')
        self.pprint(boxxes)
    
    def get_master_courses(self):
        check_column = self.driver.find_element_by_css_selector(
                'ul[class="lookup-facet--hierarchicalFacet"]'
            )
        # check_column
        # check with a loop each element and click the one
        # that the user entered (check if valid)
    
    def get_phd_info(self):
        pass

    def pprint(self, input_list: list) -> None:
        for i, input in enumerate(input_list):
            input_text = input.get_attribute("innerHTML")
            print(f'{i+1}: {input_text}')

