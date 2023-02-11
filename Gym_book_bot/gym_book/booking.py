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

    def init_actions(self) -> None:
        self.actions = ActionChains(self)

    def __exit__(self, *args) -> None:
        if self.teardown:
            self.quit()
    
    
    def open_url(self, show_web_page: bool) -> None:
        self.get(const.URL)
        self.minimize_window()
        if show_web_page:
            self.maximize_window()

    def go_to_login(self) -> None:
        self.find_elements_by_class_name(
            'btn-primary'
            )[0].click()
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

    def search_sport(self, session: str) -> None:
        self.find_element_by_id(
            'tag-searchfield'
            ).send_keys(session)
        self.actions.send_keys(Keys.ENTER).perform()
        
    def click_book(self, time_slot: str, sure_to_book: bool=False) -> None:
        self.sure_to_book = sure_to_book
        slots = self.find_elements_by_class_name('d-inline-block')
        if time_slot == None:
            self.book_slot(slots[0])
        else:
            for slot in slots:
                slot_time = slot.find_element_by_tag_name(
                    'strong'
                    ).get_attribute('innerHTML')
                if slot_time.strip() == time_slot:
                    try:
                        self.book_slot(slot)
                    except:
                        help.print_fail("Failed to book!")
                    break

    def book_slot(self, slot) -> None:
        spots_elements = slot.find_elements_by_tag_name('small')   
        spot_inner_str = spots_elements[-1].get_attribute('innerHTML')
        spots_left = spot_inner_str.strip().split()[-2]
        if int(spots_left) > 0:
            self.book_or_availability(slot)
        else:
            help.print_fail("this slot has no spots available!")

    def book_or_availability(self, slot) -> None:
        if self.sure_to_book:
            slot.find_element_by_class_name(
                'btn-primary'
                ).click()
            try:    
                buttons = self.find_elements_by_tag_name('button')
                buttons[-1].click()
                help.print_success("Booked! You should receive an email of confirmation.")
            except:
                help.print_fail("Failed to book!")
        else:
            help.print_success("You could book this slot!")
    