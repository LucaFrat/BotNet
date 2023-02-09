import time
import gym_book.constants as const
from gym_book.booking import Booking
import gym_book.helpers as help


def define_variables(debug_mode: bool) -> list:
    if debug_mode:
        show_web_page = True
        session = const.TEST_SESSION
        date = None
        time_slot = const.TEST_TIME_SLOT
        sure = False
        return show_web_page, session, date, time_slot, sure
    else:
        return help.input_info_booking()

def main():
    debug_mode = False
    show_web_page, session, date, time_slot, sure = define_variables(debug_mode)
    with Booking(teardown=True) as bot:
        bot.open_url(show_web_page)
        bot.init_actions()
        bot.go_to_login()
        bot.login()
        bot.change_focus_date()
        bot.search_sports(session)
        bot.click_book(time_slot, sure)
        time.sleep(2)

if __name__ == '__main__':
    main()
