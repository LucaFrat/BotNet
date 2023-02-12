from Bots.gym_bot import Gym
from Bots.courses_bot import Courses
from Bots.intern_bot import Internship
import Bots.constants as const
from typing import Callable


def which_bot_to_run() -> Callable:
    Bots_classes = {
        'intern': Internship,
        'gym': Gym,
        'courses': Courses
        }
    while True:
        choice = str(input(
            "\nWhich bot would you run? [intern/gym/courses] > "
            )).strip()
        if choice in const.BOTS:
            Bot = Bots_classes[choice]
            return Bot


def main(Bot: Callable) -> None:
    debug_mode = False
    with Bot() as bot:
        bot.run(debug_mode)


if __name__ == "__main__":
    Bot_to_run = which_bot_to_run() 
    main(Bot_to_run)