import random
import sys


def load_highs():
    infile = open('high_royal.txt', 'r')
    highs = infile.readlines()
    infile.close()
    return highs


def load_lows():
    infile = open('low_royal.txt', 'r')
    lows = infile.readlines()
    infile.close()
    return lows


def build_lists() -> (list, list):
    """
    Build lists to be used per election cycle \n
    :return: Highs, Lows for both sets of houses
    """
    highs = load_highs()
    highs = [item.strip() for item in highs]

    lows = load_lows()
    lows = [item.strip() for item in lows]

    return highs, lows


def choose_level(pos) -> str:
    """
    Chooses a house level to appoint the position from. \n
    Advisors are weighted 70/30 to lower houses. \n
    High council is weighted 70/30 to high houses. \n
    :param pos: should be a string of advisor for advisory council or lord for high council
    :return: returns a string value of which house choice (high or low) to select the lord from
    """
    levels = ['high', 'low']
    if pos == 'advisor':
        choice = random.choices(levels, weights=(30, 70), k=1)
        for item in choice:
            choice = item
        return choice
    elif pos == 'lord':
        choice = random.choices(levels,weights=(70,30), k=1)
        for item in choice:
            choice = item
        return choice
    else:
        sys.exit('Level choice should be advisor or lord!')


def writer(file):
    """
    Return a file handler to write to
    :param file: filename string
    :return: returns textIO for file handler
    """
    f = open(file, "a+")
    return f


def get_gov(list):
    substring = "Whitley"
    while True:
        try:
            random_from = random.choice(list)
            if substring in random_from:
                print("No Whitley for gov")
            else:
                return random_from
        except Exception as e:
            print(e)


def get_lord(highs: list, lows: list) -> (str, str):
    lvl = choose_level("lord")
    if lvl == "high":
        choice = random.choice(highs)
    else:
        choice = random.choice(lows)
    return lvl, choice


def get_adv(highs: list, lows: list) -> (str, str):
    lvl = choose_level("advisor")
    if lvl == "high":
        choice = random.choice(highs)
    else:
        choice = random.choice(lows)
    return lvl, choice


def write_loop(year: int, highs: list, lows: list, handle):
    def br(times: int):
        i = 0
        while i < times:
            handle.write("[br]\n")
            i += 1

    handle.write("[h2]{} LB[/h2]\n".format(year))
    gov = get_gov(highs)
    highs.remove(gov)
    handle.write("[h3]Governor: {}[/h3]\n".format(gov))
    level, lord = get_lord(highs, lows)
    if level == "high":
        highs.remove(lord)
    else:
        lows.remove(lord)
    handle.write("""[h3]Cabinet[/h3]\n\nLt. Governor: {}\n[br]""".format(lord))
    level, lord = get_lord(highs, lows)
    if level == "high":
        highs.remove(lord)
    else:
        lows.remove(lord)
    handle.write("""\nLord of the Land: {}\n[br]""".format(lord))
    level, lord = get_lord(highs, lows)
    if level == "high":
        highs.remove(lord)
    else:
        lows.remove(lord)
    handle.write("""\nLord of the Harbor: {}\n[br]""".format(lord))
    level, lord = get_lord(highs, lows)
    if level == "high":
        highs.remove(lord)
    else:
        lows.remove(lord)
    handle.write("""\nLord of Finances:{}\n[br]""".format(lord))
    level, lord = get_lord(highs, lows)
    if level == "high":
        highs.remove(lord)
    else:
        lows.remove(lord)
    handle.write("""\nTrademaster: {}\n""".format(lord))
    br(2)
    level, adv = get_adv(highs, lows)
    if level == "high":
        highs.remove(adv)
    else:
        lows.remove(adv)
    handle.write("""Advisory Council:\n[br]\nSr Adv: {}\n[br]\n""".format(adv))
    level, adv = get_adv(highs, lows)
    if level == "high":
        highs.remove(adv)
    else:
        lows.remove(adv)
    handle.write("""Adv: {}\n[br]\n""".format(adv))
    level, adv = get_adv(highs, lows)
    if level == "high":
        highs.remove(adv)
    else:
        lows.remove(adv)
    handle.write("""Adv: {}\n[br]\n""".format(adv))
    level, adv = get_adv(highs, lows)
    if level == "high":
        highs.remove(adv)
    else:
        lows.remove(adv)
    handle.write("""Adv: {}\n[br]\n""".format(adv))
    level, adv = get_adv(highs, lows)
    if level == "high":
        highs.remove(adv)
    else:
        lows.remove(adv)
    handle.write("""Adv: {}\n[br]\n[br]\n""".format(adv))


def main():
    while True:
        try:
            times = int(input("How many times to run? "))
            if times > 0:
                break
            print("Invalid number of times entered")
        except Exception as e:
            print(e)
    while True:
        try:
            year = int(input("Starting from what year? "))
            if 151 >= year > 0:
                break
            elif year > 151:
                print("Year cannot be over 151")
        except Exception as e:
            print(e)

    file = input("Name the output file: ")
    handle = writer(file)

    i = 0
    while i < times:
        highs, lows = build_lists()
        curr_year = year - i
        write_loop(curr_year, highs, lows, handle)
        i += 1


main()
