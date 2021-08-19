# *****************
# BY INBAR HAWKINS*
# *****************
import traffic_lights
import palindrom
import gematria
import dice


def show_menu():
    print("""What do you like to do?
      1. Change traffic light
      2. Check palindrome
      3. Calculate gematria value
      4. Play pig dice with your friends
      Quit (q/Q)
""")


def get_input():
    while True:
        user_choice = input("Please enter your choice: ")
        if user_choice in ['1', '2', '3', '4', 'q', 'Q']:
            break
        else:
            print("This is not a valid choice.")
            show_menu()
    return user_choice


while True:
    show_menu()
    user_choise = get_input()
    if user_choise == '1':
        current_color = input("Enter your current color (red/yellow/green): ")
        print(traffic_lights.update_light(current_color))
        continue
    elif user_choise == '2':
        palindrom.run_palindromes()
        continue
    elif user_choise == '3':
        print(
            f'the score of your string is: {gematria.get_final_score()}')
        continue
    elif user_choise == '4':
        dice.run_dice_game()
        dice
        continue
    else:
        break
