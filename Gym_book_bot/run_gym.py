from gym_book.booking import Booking

def main():
    with Booking(teardown=True) as bot:
        bot.open_url()
        bot.choose_login_method()

if __name__ == '__main__':
    main()
