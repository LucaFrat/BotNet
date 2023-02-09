from gym_book.booking import Booking
from gym_book.helpers import input_info_booking

def main():
    #session, date, time_slot = input_info_booking()
    with Booking(teardown=True) as bot:
        bot.open_url()
        bot.go_to_login()
        bot.login()
        bot.change_focus_date()

if __name__ == '__main__':
    main()
