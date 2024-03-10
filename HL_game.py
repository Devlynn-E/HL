import math


import random


# checks for valid number of rounds
def rounds(question):
    error = "please enter an integer above 0, or <enter> for infinite mode"

    while True:

        to_check = input(question)

        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


def get_stats(stats_list):
    stats_list.sort()

    low = stats_list[0]
    high = stats_list[-1]
    average = sum(stats_list) / len(stats_list)

    return [low, high, average]


def yes_no(question):
    # starts loop
    while True:
        response = input(question).lower()

        # defines
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please answer yes or no")


def instructions():

    print('''

        **** instructions ****

        To begin, choose the number of rounds (or press <enter> for infinite mode).
        
        You will then chose a lower and higher number (inclusive) that will contain your secret number 
    
        You will then try to guess the number while the computer will give you hints for each guess
    
        You will receive statistics on your guesses used and will be able to see your game history at the end of the game
     
        Type <xxx> to end the game at anytime.
    
        🎂🎂🎂Good Luck🎂🎂🎂

            ''')


def int_check(question, low=None, high=None, exit_code=None):

    # if any int is allowed
    if low is None and high is None:
        error = "Please enter an integer"

    # if the number needs to be more than an
    # integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = (f"Please enter an integer that is"
                 f"more than / equal to {low}")

    # if the number needs to be between low and high
    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # check for inf mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # check the int is not low
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if response is valid, return it
            else:
                return response

        except ValueError:
            print(error)


def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


# main routine
mode = "regular"
rounds_played = 0
end_game = "no"
feedback = ""

game_history = []
all_scores = []

print("\n👆👆👆 Higher or Lower 👇👇👇")
print()

# instructions
wants_instructions = yes_no("Do you want to view the instructions? ")

if wants_instructions == "yes":
    # displays instructions
    instructions()

# ask for number of rounds (checks for infinite mode)
num_rounds = int_check("\nRounds <enter for infinite>: ", low=1, exit_code="")

if num_rounds == "":
    mode = "infinite"
    rounds_to_play = 37

else:
    rounds_to_play = num_rounds

default_params = yes_no("\nDo you want to use the default game parameters ")
if default_params == "yes":
    low_num = 0
    high_num = 10

else:
    low_num = int_check("\nLow Number: ")
    high_num = int_check("\nHigh Number: ", low=low_num + 1)

max_guesses = calc_guesses(low_num, high_num)

# games loop starts
while rounds_played < rounds_to_play:

    # rounds heading
    if mode == "infinite":
        heading = f"\n♾♾♾ Round {rounds_played + 1} (infinite mode) ♾♾♾"

    else:
        heading = f"\n🥊🥊🥊 Round {rounds_played + 1} of {rounds_to_play} 🥊🥊🥊"

    print(heading)

    # round starts
    guesses_used = 0
    already_guessed = []

    secret = random.randint(low_num, high_num)

    guess = ""

    while guess != secret and guesses_used < max_guesses:

        guess = int_check("\nGuess: ", low_num, high_num, "xxx")

        if guess == "xxx":
            end_game = "yes"
            break

        if guess in already_guessed:
            print(f"\nYou've already guessed {guess}. You've *still* used"
                  f" {guesses_used} / {max_guesses} guesses")
            continue

        else:
            already_guessed.append(guess)

        guesses_used += 1

        if guess < secret and guesses_used <= max_guesses:
            feedback = f"\nToo low, please try a higher number. " \
                       f"\nYou've used {guesses_used} / {max_guesses} guesses"

            result = ""

            print(feedback)

        elif guess > secret and guesses_used <= max_guesses:
            feedback = f"\nToo high, please try a lower number. " \
                       f"\nYou've used {guesses_used} / {max_guesses} guesses"
            result = ""

            print(feedback)

        elif guess == secret and guesses_used <= max_guesses:
            feedback = f"\nCongrats! You found the secret number! {secret} " \
                       f"\nYou used {guesses_used} / {max_guesses} guesses"

            result = feedback

            print(result)

        else:
            feedback = f"\nYou used all of your {max_guesses} guesses." \
                       f"\nYou lost. \t" \
                       f"The secret number was: {secret}"

            result = feedback

            print(result)

        all_scores.append(guesses_used)
        game_history.append(result)

    # round ends here

    if end_game == "yes":
        break

    rounds_played += 1

if rounds_played > 0:

    all_scores.sort()
    best_score = all_scores[0]
    worst_score = all_scores[-1]
    average_score = sum(all_scores) / len(all_scores)

    print("\n📊📊📊 Game Statistics 📊📊📊")
    print(f"\nBest: {best_score} | Worst: {worst_score} | Average: {average_score:.2f} ")
    print()

    see_history = yes_no("\ndo you want to see your game history? ")
    if see_history == "yes":
        print("\nGame History")
        for item in game_history:
            print(item)

    print("\nThank you for playing!")


else:
    print("\nwhy didn't you want to play?")
