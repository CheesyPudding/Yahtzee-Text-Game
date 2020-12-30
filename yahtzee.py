"""
Yahtzee Final Exam Hackathon
COMP 1510
Jasper Zhou
A01235376
"""

import doctest
import random


def YAHTZEE_BONUS():
    return 100


def YAHTZEE_POINTS():
    return 50


def YAHTZEE():
    return 5


def QUARTET():
    """Quadruple."""
    return 4


def FULL_HOUSE():
    """Points for scoring a full house."""
    return 25


def TRIPLET():
    """Triple."""
    return 3


def PAIR():
    """Double."""
    return 2


def UPPER_CATEGORY() -> tuple:
    """ These are the 6 sections in the upper row, one for each dice number."""
    return 1, 2, 3, 4, 5, 6


def GOT_OPTIONS() -> tuple:
    """ There are only 4 options a user can make with their dice turn."""
    return "Add dice to hand", "Return dice to pile", "Re-roll dice pile", "Add dice pile to hand (confirm hand)"


def DICE_ROLLS() -> int:
    """ There are only 5 dice rolls at a time."""
    return 5


def PLAYER_TWO() -> str:
    """ player two is distinguished by 2 on the scorecard."""
    return "2"


def PLAYER_ONE() -> str:
    """ player one is distinguished by 2 on the scorecard."""
    return "1"


def TURNS() -> int:
    """ Each player always starts with 3 rolls for their dice roll turn."""
    return 3


def DICE_ASCII_LINES() -> int:
    """ Ascii art always prints 5 lines."""
    return 5


def QUIT_COMMAND() -> str:
    """ User always enters 'q' to quit the program on the main menu."""
    return "q"


def round_end(scorecard: dict) -> None:
    """Print round scoreboard results.
    Given both player scorecards, calculate the final scores including the upper bonus and yahtzee bonus.

    :precondition: accepted dictionary will not have any key values as none.
    :param scorecard: Player one's scorecard with each key value representing the number for that score.
    :postcondition: Print but does not return a message based by calculation scores.
    """
    upper_bonus = 0
    total = 0
    for row in scorecard:
        total += scorecard[row]

    for score_row in UPPER_CATEGORY():
        upper_bonus += scorecard[score_row]
    if upper_bonus >= 63:
        scorecard['upper_bonus'] = 35

    print(f"Total score: {total}")


def fill_score(scorecard: dict, score_row, hand: list) -> dict:
    """Fill out a scorecard row with given hand.

    Given the dictionary scorecard, use the score_row param as the key, and hand as the value to calculate and enter the
    score for the specified row.

    :precondition: hand will have only 5 items, score_row will be a key that exists in scorecard dictionary
    :param scorecard: Dictionary to have a key value modified.
    :param score_row: Scorecard row user selected to fill out that is still -1 on the scorecard dictionary.
    :param hand: list of 5 integers(1-6) specified by the user.
    :return: modified scorecard dictionary.
    :postcondition: only returns the dictionary with one key value modified.
    """
    dice_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}  # empty dice dictionary where each dice number is a key value pair
    for dice in hand:
        dice_dict[dice] += 1

    if score_row in UPPER_CATEGORY():
        scorecard[score_row] = (dice_dict[score_row] * score_row)  # multiple number of dices by that dice number row
        print(scorecard)
        return scorecard

    scorecard[score_row] = 0

    if score_row == "three-of-a-kind":
        for dice in dice_dict:
            if dice_dict[dice] >= TRIPLET():
                scorecard[score_row] = sum(hand)

    if score_row == "four-of-a-kind":
        for dice in dice_dict:
            if dice_dict[dice] >= QUARTET():
                scorecard[score_row] = sum(hand)

    if score_row == "yahtzee":
        for dice in dice_dict:
            if dice_dict[dice] == YAHTZEE():
                scorecard[score_row] = YAHTZEE() * 10

    if score_row == "full-house":
        for triple in dice_dict:
            if list(dice_dict.keys())[list(dice_dict.values()).index(3)] == triple:
                for double in dice_dict:
                    if list(dice_dict.keys())[list(dice_dict.values()).index(2)] == (double and (not triple)):
                        scorecard[score_row] = FULL_HOUSE()

    if score_row == "small straight":
        if set(sorted(hand)).issubset([1, 2, 3, 4] or [2, 3, 4, 5] or [3, 4, 5, 6]):
            scorecard[score_row] = sum(hand)
    if score_row == "large straight":
        if set(sorted(hand)).issubset([1, 2, 3, 4, 5] or [2, 3, 4, 5, 6]):
            scorecard[score_row] = sum(hand)

    if score_row == "chance":
        scorecard[score_row] = sum(hand)

    return scorecard


def get_choice(scorecard: dict) -> str:
    """Choose a row to fill out with given hand.

    Given 5 dices rolled in roll_dice(), prompt user to fill out a column in their scorecard and return the scorecard
    with the updated score.

    :precondition: key values in scorecard dictionary still have -1 so a row can be filled.
    :param scorecard: player scorecard with each key value representing each column on a Yahtzee scorecard.
    :return: updated scorecard dictionary with one user specified key value modified.
    :postcondition: user must select one key value to modify, or the function will continue to run.
    """
    choice = ""
    score_list = []

    print("Select a row to score with current hand:")
    for row in scorecard:  # generate list of all empty score rows
        if scorecard[row] == -1:
            score_list.append(row)

    for item in score_list:  # print ordered list of all scorecard sections
        print(f"{score_list.index(item) + 1}. {item}")

    while True:
        try:
            choice = int(input("\nOption:")) - 1
            if 0 <= choice:
                return score_list[choice]
        except (IndexError, ValueError):
            print("Invalid option: failed to select a valid score row...")
            continue


def transfer_dice(taken_list: list) -> int:
    while True:
        print("Select a dice to add/return:")
        print(taken_list)
        for option, dice in enumerate(taken_list):
            print(f"{option + 1}. {dice}")

        try:
            choice = int(input("\nOption: ")) - 1
            if choice >= 0:
                return taken_list[choice]
            else:
                print("Invalid option: failed to select a valid dice...")
        except (IndexError, ValueError):
            print("Invalid option: failed to select a valid dice...")


def print_dice(dice_hand: list) -> None:
    """Print dice ascii art.

    Given the list of dices, print it out in a more visual way by converting the list of numbers into a string for
    each line.

    :param: dice_hand: list of numbers (1-6) where each integer item will be printed as a dice ascii art.
    :postcondition: only prints the list, doesn't modify it.
    """
    dice_ascii = ((" _______  ", "|       | ", "|   o   | ", "|       | ", " -------  "),
                  (" _______  ", "| o     | ", "|       | ", "|     o | ", " -------  "),
                  (" _______  ", "| o     | ", "|   o   | ", "|     o | ", " -------  "),
                  (" _______  ", "| o   o | ", "|       | ", "| o   o | ", " -------  "),
                  (" _______  ", "| o   o | ", "|   o   | ", "| o   o | ", " -------  "),
                  (" _______  ", "| o   o | ", "| o   o | ", "| o   o | ", " -------  "))

    dice_string = ["" for dice in range(DICE_ASCII_LINES())]

    for line in range(DICE_ASCII_LINES()):
        for dice in dice_hand:
            dice_string[line] += dice_ascii[dice - 1][line]

    print(*dice_string, sep='\n')
    print(f"{dice_hand}")
    """ this is what each dice will look like and be printed:
      _______  _______  _______  _______  _______  _______
     |       || o     || o     || o   o || o   o || o   o | 
     |   o   ||       ||   o   ||       ||   o   || o   o | 
     |       ||     o ||     o || o   o || o   o || o   o | 
      -------  -------  -------  -------  -------  -------
    """


def print_hands(dice_hand: list, hand: list, rolls_left: int) -> None:
    """Print current dice in hand, in pile, and rolls left.

    Print message to the player in an organized and visual way each time they make an action on their roll turn.

    :precondition: rolls_left will never be less than 0 and more than 3, sum of items in the two lists always = 5
    :param dice_hand: list of 1-5 (specified by the argument) items with random integers (1-6)
    :param hand: list of 1-5 (specified by the argument) items with random integers (1-6)
    :param rolls_left: integer amount of re-rolls left for player
    :precondition: only prints and doesn't return
    """
    print("current dice pile:")
    print_dice(dice_hand)
    print("current hand:")
    print_dice(hand)
    print(f"remaining rolls: {rolls_left}\n")


def make_dice_pile(rolled_dices: int) -> list:
    """Roll dice in dice pile.

    Generate a list of 1-5 items with random integers (1-6), and return the list.

    :precondition: rolled_dices parameter will always be an integer [1,5]
    :param: rolled_dices: integer number of dice in dice pile to re-roll.
    :return: list of 1-5 (specified by the argument) items with random integers (1-6)
    :postcondition: never returns an empty list
    """
    dice_pile = []
    for dice in range(rolled_dices):  # generate a list of random (1,6) integers for each dice rolled
        dice_pile.append(random.randint(1, 6))
    return dice_pile


def get_user_choice() -> int:
    """Print user options and prompt input.

    Player can either 1. add dice to hand, 2. Return dice to pile, 3. Re-roll dice pile, or 4.Add dice pile to hand
    (confirm hand). User then selects an index number and function returns the integer representing that option.
    Helper function for roll_dice().

    :precondition: function continues to prompt user until they input a correct option.
    :return: integer representing the option in GOT_OPTIONS().
    """
    while True:
        choice = 0
        print("Select an option: ")
        for option, choice in enumerate(GOT_OPTIONS()):  # user chooses to now change or submit hand
            print(f"{option + 1}. {choice}")
        try:
            choice = int(input("\nOption: ")) - 1
            if  4 > choice >= 0:
                return choice
        except (TypeError, IndexError, ValueError):
            print('Invalid option...')
            continue


def roll_dice(hand: list, rolls_left: int) -> list:
    """Simulate a dice roll turn.

    Recursive function that randomly generates a list of 1-5 integers (with random dice values). User is shown the roll
    then prompted to add dices from the pile to their hand or vise versa, roll again and subtract a roll, or lose all
    rolls and add the remaining pile of dices to their hand.

    :precondition: number of items in hand list or dice pile list will never be >6 (player can only have 5 dices).
    :param hand: list with dice numbers 1-6 as items. First iteration of roll_dice will always be an empty list.
    :param rolls_left: amount of rolls available for the turn, function repeats until rolls_left is 0.
    :return: list with 5 items with numbers 1-6.
    :postcondition: always returns a list that the user has specified through user input.
    """
    dice_hand = make_dice_pile(DICE_ROLLS() - len(hand))  # create another list as the dice pile "hand"

    while rolls_left > 0:  # if user still has rolls, run the choice loop, or else user must keep the dices rolled
        print_hands(dice_hand, hand, rolls_left)  # print current dice pile, user hand, and rolls left

        choice = get_user_choice()

        if (choice == 0) and (dice_hand != []):  # take a dice from dice pile and move to hand
            dice = transfer_dice(dice_hand)
            dice_hand.remove(dice)
            hand.append(dice)
        if choice == 1 and (hand != []):  # take a dice from hand and move to dice pile
            dice = transfer_dice(hand)
            hand.remove(dice)
            dice_hand.append(dice)
        if choice == 2:  # user keeps their dices in hand and re-rolls pile, lose a roll
            print("\nRe-rolling dice pile...\n")
            return roll_dice(hand, rolls_left - 1)
        if choice == 3:  # user is satisfied with their hand, no more re-rolling and return hand
            print("\nNo more rolls, choosing to use these dice...\n")
            return hand + dice_hand
    print("\nOut of rolls, must use this hand...\n")
    return hand + dice_hand


def print_scorecard(player: str, raw_scorecard: dict) -> None:
    """Compile dictionary and print into a visual Yahtzee scorecard.

    Updates the specified player's score visually by printing line by line to represent a Yahtzee scorecard.

    :precondition: player parameter should only be one character to maintain visually clarity.
    :param player: represents the number of the player (player x).
    :param raw_scorecard: player scorecard with each key value representing each row on a Yahtzee scorecard.
    :postcondition: doesn't return and only prints the current scorecard to the user.
    """
    scorecard = raw_scorecard.copy()  # create copy of dictionary where all -1 values are ""
    for score in raw_scorecard:  # change all key values -1 to ""
        if raw_scorecard[score] == -1:
            scorecard[score] = ""

    print(f"|***YAHTZEE PLAYER {player}***|\n|**   UPPER SECTION  **|\n"  # print out each line in the scorecard
          f"|ONES                ({scorecard[1]})|\n|TWOS                ({scorecard[2]})|\n"
          f"|THREES              ({scorecard[3]})|\n|FOURS               ({scorecard[4]})|\n"
          f"|FIVES               ({scorecard[5]})|\n|SIXES               ({scorecard[6]})|\n"
          f"|*>62 BONUS          ({scorecard['upper_bonus']})|\n|**   LOWER SECTION  **|\n"
          f"|3 OF A KIND         ({scorecard['three-of-a-kind']})|\n|4 OF A KIND         "
          f"({scorecard['four-of-a-kind']})|\n|FULL HOUSE          ({scorecard['full-house']})|\n"
          f"|SMALL STRAIGHT      ({scorecard['small straight']})|\n"
          f"|LARGE STRAIGHT      ({scorecard['large straight']})|\n|YAHTZEE             ({scorecard['yahtzee']})|\n"
          f"|CHANCE              ({scorecard['chance']})|\n|*YAHTZEE BONUS      ({scorecard['lower_bonus']})|\n"
          f"|*UPPER TOTAL        ({scorecard['u_total']})|\n|*LOWER TOTAL        ({scorecard['l_total']})|\n"
          f"|*TOTAL              ({scorecard['total']})|\n")


def check_score(scorecard: dict) -> bool:
    """Given the scorecard dictionary, checks if all key values are not -1.

    Guard clause for the while loop in play_round() that continues turns in a Yahtzee round if true,
    or false to break the loop and complete the round.

    :precondition: only checks dictionaries with the same key values generated in initialize_scorecard().
    :param scorecard: player scorecard with each key value representing each column on a Yahtzee scorecard.
    :return: True if a dictionary key value contains None, and False if -1 is not in any key value.
    :postcondition: returned boolean only used in the guard clause for the round for loop.

    >>> empty_card = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 'upper_bonus': 0, 'three-of-a-kind': -1, \
    'four-of-a-kind': -1, 'full-house': -1, 'small straight': -1, 'large straight': -1, 'yahtzee': -1, 'chance': -1, \
    'lower_bonus': 0, 'u_total': 0, 'l_total': 0, 'total': 0}
    >>> check_score(empty_card)
    True
    >>> filled_card = {1: 1, 2: 4, 3: 9, 4: 12, 5: 15, 6: 30, 'upper_bonus': 0, 'three-of-a-kind': 17, \
    'four-of-a-kind': 20, 'full_house': 25, 'small straight': 30, 'large straight': 40, 'yahtzee': 50, 'chance': 18, \
    'lower_bonus': 100, 'u_total': 71, 'l_total': 300, 'total': 371}
    >>> check_score(filled_card)
    False
    """
    for score in scorecard:
        if scorecard[score] == -1:
            return True

    return False


def initialize_scorecard() -> dict:
    """Create scoreboards for each player, as according to the Yahtzee standard.

    Generate a dictionary with all key values being either -1 (player fills these out) or 0 (to be only used for
    score) to be used for each player as the Yahtzee scoreboard.

    :precondition: function be be assigned in a variable to use the scorecard.
    :return: dictionary with each key value pair as each row on a Yahtzee scorecard.
    :postcondition: always returns a new identical dictionary, not a duplicate.

    >>> initialize_scorecard()
    {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 'upper_bonus': 0, 'three-of-a-kind': -1, 'four-of-a-kind': -1, \
'full-house': -1, 'small straight': -1, 'large straight': -1, 'yahtzee': -1, 'chance': -1, \
'lower_bonus': 0, 'u_total': 0, 'l_total': 0, 'total': 0}
    """
    return {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 'upper_bonus': 0, 'three-of-a-kind': -1, 'four-of-a-kind': -1,
            'full-house': -1, 'small straight': -1, 'large straight': -1, 'yahtzee': -1, 'chance': -1,
            'lower_bonus': 0, 'u_total': 0, 'l_total': 0, 'total': 0}


def play_round() -> None:
    """Loop turns for both players until both users have completely filled their scores.

    Uses initialize_scorecard() to start and round_end() to end the round. Loops player turns in a while loop until
    both users have completely filled their scorecards. Helper function to yahtzee().
    """
    print("\n...MATCH BEGIN...\n")
    scorecard_1 = initialize_scorecard()  # initialize player scorecards
    scorecard_2 = initialize_scorecard()  # initialize player scorecards

    while check_score(scorecard_1) and check_score(scorecard_2):  # keep while-looping turns for each player
        print_scorecard(PLAYER_ONE(), scorecard_1)  # print player 1 scorecard
        print("It is now player 1's turn...")
        hand_1 = []
        hand_1 = roll_dice(hand_1, TURNS())  # roll and get player 1 hand with 3 rolls
        print_dice(hand_1)  # user's final hand to use
        print_scorecard(PLAYER_ONE(), scorecard_1)  # print player 1 scorecard
        category = ""
        category = get_choice(scorecard_1)  # choose a row to fill out
        fill_score(scorecard_1, category, hand_1) # fill out a scorecard row with current hand

        print_scorecard(PLAYER_TWO(), scorecard_2)  # print player 1 scorecard
        print("It is now player 2's turn...")
        hand_2 = []
        hand_2 = roll_dice(hand_2, TURNS())  # roll and get player 1 hand with 3 rolls
        print_dice(hand_2)  # user's final hand to use
        print_scorecard(PLAYER_TWO(), scorecard_2)  # print player 1 scorecard
        category = ""
        category = get_choice(scorecard_2)  # choose a row to fill out
        fill_score(scorecard_2, category, hand_2)  # fill out a scorecard row with current hand

    # announce results of round
    print("Player 1 final score:")
    round_end(scorecard_1)
    print("Player 2 final score:")
    round_end(scorecard_1)


def yahtzee() -> None:
    """Run all game functions from start to end of program.

    Acts as the menu for the game. Prompts user to start a round or quit. Returns to this menu after every round.
    Function doesn't return, only prints. Runs forever until the user quits to exit the program.
    """
    command = ""

    while command != QUIT_COMMAND():
        print(f"\n\n/||||||||||||||||||||||||||||\\\n|      2-PLAYER YAHTZEE      |\n*  'enter' to begin a round  *"
              f"\n|      press '{QUIT_COMMAND()}' to quit     |\n\\||||||||||||||||||||||||||||/\n")
        command = input("Enter a command: ").strip().lower()

        if command == "":
            play_round()
            print("Thank you for playing Yahtzee!")
            print("Quitting Yahtzee.py...\n")
            return None

        if command == QUIT_COMMAND():
            print("Quitting Yahtzee.py...\n")
            return None

        else:
            print("Invalid command...")
            print("Returning to main menu...\n")
            continue


def main():
    """Execute the Program"""
    doctest.testmod()
    yahtzee()
    pass


if __name__ == "__main__":
    main()
