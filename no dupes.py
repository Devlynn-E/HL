already_guessed = []

secret = 7
guesses_used = 0
guesses_allowed = 5

guess = ""
while guess != secret:
    guess = int(input("Guess: "))

    # check if guess is duplicate
    if guess in already_guessed:
        print(f"You've already guessed {guess}. You've *still* used"
              f" {guesses_used} / {guesses_allowed} guesses")
        continue

    else:
        already_guessed.append(guess)

    guesses_used += 1
