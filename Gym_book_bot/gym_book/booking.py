import os
import time
import gym_book.constants as const
import gym_book.private as priv

from selenium import webdriver


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=const.CHROME_PATH, 
                 teardown=False
                 ) -> None:
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += const.CHROME_PATH
        super(Booking, self).__init__()
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
            show_web_page = "y" #str(input('\nDo you wanna show the Web page? [y/n]: '))
            if show_web_page == "y":
                self.show_web_page = True
                self.maximize_window()
                break
            elif show_web_page == "n":
                self.show_web_page = False
                break

    def go_to_login(self):
        self.find_element_by_xpath(
            '//*[@id="content"]/div/div[2]/div/login-page/div[2]/div/div[2]/button[1]'
            ).click()
        self.find_element_by_id(
            'idp__titleremaining1'
        ).click()

    def login(self):
        self.find_element_by_id(
            'username'
            ).send_keys(priv.USERNAME)
        self.find_element_by_id(
            'password'
            ).send_keys(priv.PASSWORD)
        self.find_element_by_id(
            'submit_button'
            ).click()

    def change_focus_date(self):
        days_element = self.find_element_by_css_selector('day-selector[class="mb-4"]')
        available_days = days_element.find_elements_by_tag_name('a')
        available_days[2].click()

    def search_sports(self):
        search_box = self.find_element_by_id('tag-searchfield')
        for session in const.SESSIONS:
            pass




    