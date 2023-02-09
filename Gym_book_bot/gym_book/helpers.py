import gym_book.constants as const

def input_info_booking():
    while True:
        session = str(input("""
            Insert session to be booked.
            Choose among:
            - Fitness    [fitn]
            - Hatha Yoga [hat]
            - Power Yoga [power y]
            """)).strip()
        if session in const.SESSIONS:
            break
        else:
            input_error()
    while True:
        date = int(input("""
        When? (insert number of the day) 
        """))
        if date in range(1,32):
            break
        else:
            input_error()
    time_slot = None
    if session == 'f':
        while True:
            time_slot = str(input("""
            What time? (insert [hh:mm])
            """)).strip()
            time_slot.replace(time_slot[2], ":")
            if all(len(time_slot) == 5, 
                   int(time_slot[:2]) in range(24),
                   int(time_slot[-2:]) in range(60)):
                break
            else:
                input_error()
    return [session, date, time_slot]

def green(text: str) -> str:
    return f"\033[32m{text}\033[00m"

def red(text: str) -> str:
    return f"\033[41m{text}\033[00m"

def input_error() -> None:
    print(f'{red("Input failed")}, try again.')