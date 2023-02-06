# this file contains the class used to filtrate the courses
# given some keywords

from selenium.webdriver.remote.webdriver import WebDriver
import show_courses.constants as const

class CourseFiltration:
    def __init__(self, driver: WebDriver, choice: str) -> None:
        self.driver = driver
        self.choice = choice

    def apply_filter(self):
        if self.choice == const.course_possibilities[0]:
            pass
        elif self.choice == const.course_possibilities[1]:
            check_column = self.driver.find_element_by_css_selector(
                'ul[class="lookup-facet--hierarchicalFacet"]'
                )
        else:
            pass
    
    def pprint(self):
        pass
            
        

