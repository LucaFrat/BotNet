import os
import Bots.constants as const
import Bots.intern_helpers as help

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Internship(webdriver.Chrome):
    def __init__(self, driver_path=const.CHROME_PATH, 
                 teardown=True
                 ) -> None:
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += const.CHROME_PATH
        super(Internship, self).__init__()
        self.implicitly_wait(15)

    def run(self, debug_mode: bool) -> None:
        """ Main function needed to run the bot """
        pass

    def __exit__(self, *args) -> None:
        """ Closes the web page """
        if self.teardown:
            self.quit()

    def open_url(self) -> None:
        pass
    

