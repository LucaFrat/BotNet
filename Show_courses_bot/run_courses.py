"""
This Bot is useful to retreive and print in the terminal 
informations about the available Bachelor and Master 
courses, and about the PHD procedure, at the TU Delft.
"""

from show_courses.courses import Courses

def main() -> None:
    with Courses(teardown=True) as bot:
        bot.open_url()
        bot.select_english()
        bot.check_cookie()
        bot.go_to_page_to_make_choice()
        bot.input_course_choice()
        bot.make_choice()
        bot.apply_filtration()

if __name__ == "__main__":
    main()