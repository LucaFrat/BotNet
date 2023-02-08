import os
import time
import gym_book.constants as const

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
            show_web_page = str(input('\nDo you wanna show the Web page? [y/n]: '))
            if show_web_page == "y":
                self.show_web_page = True
                self.maximize_window()
                break
            elif show_web_page == "n":
                self.show_web_page = False
                break

    def choose_login_method(self):
        pass
        
    