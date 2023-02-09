import os
import time
import gym_book.constants as const
import gym_book.private as priv
import gym_book.helpers as help

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


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

    def init_actions(self) -> None:
        self.actions = ActionChains(self)
    
    def open_url(self, show_web_page: bool) -> None:
        self.get(const.URL)
        self.minimize_window()
        if show_web_page:
            self.maximize_window()

    def go_to_login(self) -> None:
        #TODO look for a better way to find the next element 
        self.find_element_by_xpath(
            '//*[@id="content"]/div/div[2]/div/login-page/div[2]/div/div[2]/button[1]'
            ).click()
        self.find_element_by_id(
            'idp__titleremaining1'
        ).click()

    def login(self) -> None:
        self.find_element_by_id(
            'username'
            ).send_keys(priv.USERNAME)
        self.find_element_by_id(
            'password'
            ).send_keys(priv.PASSWORD)
        self.find_element_by_id(
            'submit_button'
            ).click()

    def change_focus_date(self) -> None:
        days_element = self.find_element_by_css_selector(
            'day-selector[class="mb-4"]')
        available_days = days_element.find_elements_by_tag_name('a')
        available_days[2].click()

    def search_sports(self, session: str) -> None:
        search_box = self.find_element_by_id('tag-searchfield')
        search_box.send_keys(session)
        self.actions.send_keys(Keys.ENTER).perform()
        
    def click_book(self, time_slot: str, sure: bool=False) -> None:
        self.sure = sure
        slots = self.find_elements_by_class_name('d-inline-block')
        for slot in slots:
            slot_time = slot.find_element_by_tag_name(
                'strong'
                ).get_attribute('innerHTML')
            if slot_time.strip() == time_slot:
                self.book_slot(slot=slot)
                break

    def book_slot(self, slot) -> None:
        spots_elements = slot.find_elements_by_tag_name('small')   
        spots_element_str = spots_elements[-1].get_attribute('innerHTML')
        spots_left = spots_element_str.strip().split()[-2]
        if int(spots_left) > 0:
            self.sure_to_book()
        else:
            print(f'{help.red("ERROR:")} this slot has no spots available! \n')

    def sure_to_book(self) -> None:
        if self.sure:
            self.find_element_by_css_selector(
                'button[class="btn-primary"]'
                ).click()
            print("")
            print(help.green("+----------------------------------------------------+"))
            print(help.green("Booked! You should receive an email of confirmation."))
        else:
            print("")
            print(help.green("+------------------------------------+"))
            print(help.green("It works, you could book this slot!\n"))
    