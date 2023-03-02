from Bots.gym_bot import Gym


def main() -> None:
    my_booking = True
    with Gym() as bot:
        bot.run(my_booking)


if __name__ == "__main__":
    main()