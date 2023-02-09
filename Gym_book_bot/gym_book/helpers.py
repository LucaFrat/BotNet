import gym_book.constants as const

def input_info_booking():
    show = input_visualization()
    sure = are_you_sure()
    session = input_session()
    date = input_date()
    if session == 'fitn':
        time_slot = input_time_slot()
    else:
        time_slot = None
    return show, session, date, time_slot, sure


def input_visualization() -> None:
    while True:
        show = str(input('\nDo you wanna show the Web page? [y/n]: '))
        if show == "y":
            show = True
            break
        elif show == "n":
            show = False
            break
    return show

def are_you_sure() -> bool:
    while True:
        sure = str(input('Do you wanna Book (B) or just check for the Availability (A) [B/A] > '))
        if sure == ("B" or "b"):
            sure = True
            break
        elif sure == ("A" or "a"):
            sure = False
            break
    return sure

def input_session() -> str:
    while True:
        session = str(input("""
Insert session to be booked.
Choose among:
- Fitness    [fitn]
- Hatha Yoga [hat]
- Power Yoga [power y]
> """)).strip()
        if session in const.SESSIONS:
            break
        else:
            input_error()
    return session

def input_date() -> str:
    while True:
        date = int(input("When? (insert number of the day) > "))
        if date in range(1,32):
            break
        else:
            input_error()
    return date

def input_time_slot() -> str:
    while True:
        time_slot = str(input("What time? (insert [hh:mm]) > ")).strip()
        time_slot.replace(time_slot[2], ":")
        if all([len(time_slot) == 5, 
                int(time_slot[:2]) in range(24),
                int(time_slot[-2:]) in range(60)]):
            break
        else:
            input_error()
    return time_slot

def green(text: str) -> str:
    return f"\033[32m{text}\033[00m"

def red(text: str) -> str:
    return f"\033[41m{text}\033[00m"

def input_error() -> None:
    print(f'{red("Input failed")}, try again.')