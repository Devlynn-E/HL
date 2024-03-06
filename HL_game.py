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

        To begin, choose the number of rounds (or press <enter> for infinite mode).
        
        You will then chose a lower and higher number (inclusive) that will contain your secret number 
    
        You will then try to guess the number while the computer will give you hints for each guess
    
        You will receive statistics on your guesses used and will be able to see your game history at the end of the game
     
        Type <quit> to end the game at anytime.
    
        🎂🎂🎂Good Luck🎂🎂🎂

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
