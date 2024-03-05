def rounds(question):

    error = "please enter an integer above 0, or <enter> for infinite mode"

    while True:
        try:

            num_rounds = input(question)

            if num_rounds == "":
                ans = "infinite"
                return ans

            elif int(num_rounds) > 0:
                ans = num_rounds
                return ans

            else:
                print(error)

        except ValueError:
            print(error)


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

        At the start of each round, the user and the computer each roll two dice.  
        The initial number of points for each player is the total shown by the dice.  Then, taking turns, 
        the user and computer each roll a single die and add the result to their points.  
        The goal is to get 13 points (or slightly less) for a given round.  
        Once you are happy with your number of points, you can ‘pass’.

        - If you go over 13, then you lose the round (and get zero points).

        - If the computer goes over 13, the round ends and your score is the number of points that you have earned.

        - If the computer gets more points than you eg: you get 10 and they get 11, 
          then you lose your score stays the same 

        - If you get more points than the computer (but less than 14 points), you win and add your points to your score.  
          The computer’s score stays the same. 

        - If the first roll of your dice is a double, then your score is increased by double the number of points,
          provided you win.  If the computer’s first roll of the dice is a double, then its points are not doubled 
          (this gives the human player a slight advantage).

        - The ultimate winner of the game is the first one to get to the specified score goal.

        ''')


# main routine
mode = "regular"
rounds_played = 0
rounds_tied = 0
rounds_lost = 0
rounds_won = 0

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []

print("\n👆👆👆 Higher or Lower 👇👇👇")
print()

# instructions

# asks user
wants_instructions = yes_no("Do you want to view the instructions? ")

if wants_instructions == "yes":
    # displays instructions

    instructions()

# ask for number of rounds (checks for infinite mode)
num_rounds = rounds("How many rounds do you want to play? <enter> for infinite ")

if num_rounds == "infinite":
    mode = "infinite"
    rounds_to_play = 37

else:
    rounds_to_play = num_rounds

# games loop starts
while rounds_played < rounds_to_play:

    # rounds heading
    if mode == "infinite":
        heading = f"\n♾♾♾ Round {rounds_played + 1} (infinite mode) ♾♾♾"

    else:
        heading = f"\n🥊🥊🥊 Round {rounds_played + 1} of {rounds_to_play} 🥊🥊🥊"

    print(heading)

    user_weapon = string_checker("choose your weapon: ", rps_list)

    if user_weapon == "xxx":
        break

    # randomly chooses from the list (excluding the exit code)
    com_weapon = random.choice(rps_list[:-1])
    print("Computer chose ", com_weapon)

    result = rps_compare(user_weapon, com_weapon)

    if result == "tie":
        rounds_tied += 1
        feedback = "You Tied"

    elif result == "lose":
        rounds_lost += 1
        feedback = "You Lost"

    else:
        rounds_won += 1
        feedback = "You Won"

    round_feedback = f"{user_weapon} vs {com_weapon}, {feedback}"
    history_item = f"Round: {rounds_played + 1} - {round_feedback}"

    print(round_feedback)
    game_history.append(history_item)

    rounds_played += 1

    # if inf mode, increase number of rounds
    if mode == "infinite":
        rounds_to_play += 1

# calculate stats
if rounds_played > 0:
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tied = 100 - percent_won - percent_lost

    # Output Game Stats
    print("\n📊📊📊 Game Statistics 📊📊📊")
    print(f"👍 Won: {percent_won:.2f} \t "
          f"😥 Lost: {percent_lost:.2f} \t "
          f"⚖ Tied: {percent_tied:.2f}")

    show_history = string_checker("\nDo you want to see the game history? ")
    if show_history == "yes":
        print("\nGame History")

        for item in game_history:
            print(item)

        print()

else:
    print("\n🐔🐔🐔 B'kawk B'kawk - You chickened out 🐔🐔🐔")
    print()

print("Thanks for playing!")
