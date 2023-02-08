from show_courses.courses import Courses

with Courses(teardown=True) as bot:
    bot.open_url()
    bot.select_english()
    bot.check_cookie()
    bot.go_to_page_to_make_choice()
    bot.input_course_choice()
    bot.make_choice()
    bot.apply_filtration()
