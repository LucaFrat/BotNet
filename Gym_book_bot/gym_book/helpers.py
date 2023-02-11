import gym_book.constants as const


def define_variables(debug_mode: bool) -> list[bool,str,str,bool]:
    if debug_mode:
        show_web_page = True
        session = const.TEST_SESSION
        time_slot = const.TEST_TIME_SLOT
        sure_to_book = False
        return [show_web_page, session, time_slot, sure_to_book]
    else:
        return input_info_booking()

def input_info_booking() -> list[bool,str,str,bool]:
    show = input_visualization()
    sure_to_book = are_you_sure()
    session = input_session()
    if session == 'fitn':
        time_slot = input_time_slot()
    else:
        time_slot = None
    return [show, session, time_slot, sure_to_book]


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
        sure = str(input(
            'Do you wanna Book or just check for the Availability? [b/a] > '
            )).strip()
        if sure in ["B","b","book"]:
            sure = True
            break
        elif sure in ["A","a","availability"]:
            sure = False
            break
    return sure

def input_session() -> str:
    while True:
        session = str(input("""
Insert session to be booked.
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
        time_slot = str(input("What time? > ")).strip()
        if len(time_slot) == 1 and int(time_slot) in range(7,10):
            time_slot = f'0{time_slot}:00'
            break
        elif len(time_slot) == 2 and int(time_slot) in range(10,23):
            time_slot = f'{time_slot}:00'
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

def print_success(text: str) -> None:
    print(green("\n+------------------------------------+"))
    print(green(f'{text}\n'))

def print_fail(text: str) -> None:
    print("\n+--------------------------------------------+")
    print(f'{red("ERROR")}: {text} \n')