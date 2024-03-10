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


secret = 7

low_num = 0
high_num = 10
guesses_allowed = 5

guesses_used = 0
already_guessed = []

guess = ""
while guess != secret and guesses_used < guesses_allowed:

    guess = int_check("Guess: ", low_num, high_num, "xxx")

    if guess == "xxx":
        end_game = "yes"
        break

    if guess in already_guessed:
        print(f"You've already guessed {guess}. You've *still* used"
              f" {guesses_used} / {guesses_allowed} guesses")
        continue

    else:
        already_guessed.append(guess)

    guesses_used += 1

    if guess < secret and guesses_used < guesses_allowed:
        feedback = f"Too low, please try a higher number. " \
                   f"You've used {guesses_used} / {guesses_allowed} guesses"
