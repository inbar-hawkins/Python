# *****************
# BY INBAR HAWKINS*
# *****************
from palindrom import rm_signs
import random
# I accept names as J.Holms, or K-Kathrin so "." and "-" are accepeted chars
# the winning rule is: if one player reached or exceedeed the max score, then all the other players
# should play in this round and the player with the highest score at the end of the entire round
#  is the winner.


def get_players():
    chars_list = [" ", "'", '"', "!", "?", "*",
                  "@", '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    while True:
        players_list = input(
            "Enter a list of players names seperated by commas: ").lower()
        players_list = rm_signs(players_list, chars_list).split(',')
        if players_list:
            break
    return players_list


def get_max_score():
    while True:
        try:
            max_score = int(input("Enter max score: "))
            break
        except Exception as e:
            print(f'An error occured:{repr(e)} ')
    return max_score


def roll_dice(player_name):
    dice = random.randint(1, 6)
    print(f'{player_name} rolled {dice}')
    return dice


def get_next_action(player_name):
    while True:
        next_action = input(
            f"{player_name}, Would you like to hold or roll again? (hold/roll): ").lower()
        if next_action not in ('hold', 'roll'):
            print("Please answer with 'hold' or 'roll': ")
        else:
            break
    return next_action


def play(scores):
    for i in scores:
        dice = roll_dice(i)
        points = 0
        if dice == 1:
            print(f'You scored {points} points in this round')
            continue
        else:
            points += dice
        next_action = get_next_action(i)
        while next_action == 'roll':
            dice = roll_dice(i)
            if dice == 1:
                scores[i] -= points
                if scores[i] < 0:
                    scores[i] = 0
                points = 0
                print(f'You scored {points} points in this round')
                winner_name = max(scores, key=scores.get)
                break
            else:
                points += dice
                print(f'You scored {points} points so far')
                next_action = get_next_action(i)
        if next_action == 'hold':
            scores[i] += points
            print(f'You scored {points} points in this round')
            points = 0
            print(scores)
            winner_name = max(scores, key=scores.get)

    return scores[winner_name]


# def init_scores(players_list):
#     scores = {}
#     for i in players_list:
#         scores[i] = get_score(i)
#     return scores


def run_dice_game():
    players_list = get_players()
    max_score = get_max_score()
    points = 0
    scores = {}
    for i in players_list:
        scores[i] = 0

    winner_name = max(scores, key=scores.get)
    best_score = scores[winner_name]

    while(best_score < max_score):
        best_score = play(scores)

    winner_name = max(scores, key=scores.get)

    print(f'CONGRATULATIONS {winner_name.upper()}! YOU ARE THE WINNER!!!')


if __name__ == "__main__":
    run_dice_game()
