# *****************
# BY INBAR HAWKINS*
# *****************

# BONUS CHALLENGE CHALLENGE: For the function check_palindrome(str).
# Import "re" module. Learn about re.sub() method and use it.


def get_input():
    str = input(
        "Enter a string to calculate it's numerology value: ").lower()
    is_valid = True
    while True:
        for i in str:
            if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                is_valid = False
        if is_valid:
            break
        else:
            str = input(
                "Please enter a string without using any digits: ").lower()
            is_valid = True

    return str


def create_numerology():
    import gematria_lists
    letters_list = []
    for i in gematria_lists.letters_str:
        letters_list += i
    numerology = {}
    counter = 1
    for i in letters_list:
        numerology[i] = counter
        counter += 1
    return numerology


def get_score(str, numeric_dict):
    from palindrom import rm_signs
    sum = 0
    chars_list = [" ", "'", '"', "!", "?", ".", ",", "-", "*",
                  "@", '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    str = rm_signs(str, chars_list)
    for i in str:
        sum += numeric_dict[i]
    return sum


def create_gematria():
    import gematria_lists
    digits = {}
    tens = {}
    hundreds = {}
    counter_digits = 0
    counter_tens = 0
    counter_hundreds = 0

    for i in gematria_lists.digits:
        digits[i] = counter_digits
        counter_digits += 1

    for i in gematria_lists.tens:
        tens[i] = counter_tens
        counter_tens += 10

    for i in gematria_lists.hundreds:
        hundreds[i] = counter_hundreds
        counter_hundreds += 100

    digits.update(tens)
    digits.update(hundreds)

    return digits


def get_final_score():
    language = input("Choose your language: (he/en) ").lower()
    if language == 'en':
        sum = get_score(get_input(), create_numerology())
    else:
        str = get_input()[::-1]
        sum = get_score(str, create_gematria())

    return sum


if __name__ == "__main__":
    print(f'The score of your string is: {get_final_score()}')
