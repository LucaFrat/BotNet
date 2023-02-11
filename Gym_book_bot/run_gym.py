import time
import gym_book.constants as const
from gym_book.booking import Booking
import gym_book.helpers as help


def main():
    debug_mode = False
    show_web_page, session, time_slot, sure_to_book = help.define_variables(debug_mode)
    with Booking(teardown=True) as bot:
        bot.open_url(show_web_page)
        bot.init_actions()
        bot.go_to_login()
        bot.login()
        bot.change_focus_date()
        bot.search_sport(session)
        bot.click_book(time_slot, sure_to_book)

if __name__ == '__main__':
    main()
