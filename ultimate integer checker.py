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


# main routine

rounds = "test"
while rounds != "":
    rounds = int_check("Rounds <enter for infinite>: ", low=1, exit_code="")
    print(f"You asked for {rounds}")

low_num = int_check("Low Number? ")
print(f"You chose a low number of {low_num}")

high_num = int_check("High Number? ", low=1)
print(f"You chose a high number of {high_num}")

# Check user guesses
guess = ""
while guess != "xxx":
    guess = int_check("Guess: ", low=0, high=10, exit_code="xxx")
    print(f"You guessed {guess}")
    print()
