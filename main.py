from Bots.gym_bot import Gym
from Bots.courses_bot import Courses
from Bots.intern_bot import Internship
import Bots.constants as const
from typing import Callable
from datetime import datetime
import os
import sys


def email_bot_ran() -> None:
    bot_exec_path = os.path.dirname(sys.executable)
    now = datetime.now()
    dd_mm_year = now.strftime("%d%m%Y")
    phrase = f'Code ran on {dd_mm_year}'
    # send_email(phrase)

Bots_classes = {
    'intern': Internship,
    'gym': Gym,
    'courses': Courses
    }

def which_bot_to_run() -> Callable:
    while True:
        choice = str(input(
            "\nWhich bot to run? [intern/gym/courses] > "
            )).strip()
        if choice in const.BOTS:
            Bot = Bots_classes[choice]
            return Bot


def main(Bot: Callable) -> None:
    debug_mode = True
    
    with Bot() as bot:
        bot.run(debug_mode)


if __name__ == "__main__":
    Bot_to_run = which_bot_to_run() 
    main(Bot_to_run)