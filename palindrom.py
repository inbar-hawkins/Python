# *****************
# BY INBAR HAWKINS*
# *****************

# BONUS CHALLENGE CHALLENGE: For the function check_palindrome(str).
# Import "re" module. Learn about re.sub() method and use it.

import palindrom_list
import random

my_list = palindrom_list.MyList


def rm_signs(str, chars_list):
    for i in str:
        if i in chars_list:
            str = str.replace(i, "")
    return str


def check_palindrome(str):
    str = str.lower()
    chars_list = [" ", "'", '"', "!", "?", ".", ",",
                  "-", "*", "@", "#", "$", "%", "&", "(", ")"]
    final_letters = {'ך': 'כ', 'ם': 'מ', 'ן': 'נ', 'ף': 'פ', 'ץ': 'צ'}
    str = rm_signs(str, chars_list)
    for i in str:
        if i in final_letters:
            str = str.replace(i, final_letters[i])
    return str == str[::-1]


def get_random():
    return random.choice(my_list)


def get_input():
    str = input("Enter a string in order to check if it is a palindrome: ")
    return str


def show_palindrome(str):
    if check_palindrome(str):
        print(f'{str} is a palindrome')
    else:
        print(f'{str} is not a palindrome')


def run_palindromes():
    show_palindrome(get_random())
    show_palindrome(get_input())


if __name__ == "__main__":
    run_palindromes()
