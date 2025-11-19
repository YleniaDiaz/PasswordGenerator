#Random password gen
import random
import string

def get_configuration():
    use_all = input("Do you want to use all alphanumeric characters and symbols? (y/n): ").lower() == 'y'
    if use_all:
        characters = {
            'letters': string.ascii_letters,
            'numbers': string.digits,
            'symbols': string.punctuation
        }
    else:
        letters = input("Enter the alphabetic characters you want to use: ")
        numbers = input("Enter the numeric characters you want to use: ")
        symbols = input("Enter the symbols you want to use: ")
        characters = {
            'letters': letters,
            'numbers': numbers,
            'symbols': symbols
        }
    return characters

def get_character_counts():
    use_default_config = input("Do you want to use the default configuration for the characters? (y/n): ").lower() == 'y'
    if use_default_config:
        print("===============DEFAULT CONFIGURATION===============")
        print("TOTAL = 25  LETTERS = 10  NUMBERS = 10  SYMBOLS = 5")
        print("===================================================")
        total = 25
        letters = 10
        numbers = 10
        symbols = 5
    else:
        total = int(input("How many characters do you want in total?: "))
        letters = int(input("How many alphabetic characters?: "))
        numbers = int(input("How many numeric characters?: "))
        symbols = int(input("How many symbols?: "))

        if letters + numbers + symbols != total:
            print("=============COUNTING ERROR=============")
            print("SUM NOT MATCHING TOTAL. ADJUSTING VALUES")
            print("========================================")
            letters = total // 3
            numbers = total // 3
            symbols = total - letters - numbers
        print("===============CURRENT CONFIGURATION===============")
        print(f"TOTAL = {total}  LETTERS = {letters}  NUMBERS = {numbers}  SYMBOLS = {symbols}")
        print("===================================================")
    return letters, numbers, symbols

def generate_segment(characters, count):
    return [random.choice(characters) for _ in range(count)]

def generate_password():
    config = get_configuration()
    letters, numbers, symbols = get_character_counts()

    letter_segment = generate_segment(config['letters'], letters)
    number_segment = generate_segment(config['numbers'], numbers)
    symbol_segment = generate_segment(config['symbols'], symbols)

    password = letter_segment + number_segment + symbol_segment
    random.shuffle(password)
    return ''.join(password)

# Execution
password = generate_password()
print(f"========GENERATED PASSWORD========\n {password.center(32)}")
