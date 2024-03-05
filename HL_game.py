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

print("\n👆👆👆 Higher or Lower 👇👇👇")
print()

# instructions
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

    weapon = input("choose your user_weapon: ")

    if weapon == "xxx":
        break

    rounds_played += 1

    # if inf mode, increase number of rounds
    if mode == "infinite":
        rounds_to_play += 1
