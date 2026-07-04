import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    max_attempts = 7
    attempts_used = 0
    close_threshold = 15  # if difference is <= this, give a "slightly" hint

    print("====================================")
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")
    print("====================================")

    while attempts_used<max_attempts:
        try:
            guess=int(input(f"\nAttempt {attempts_used+1}/{max_attempts}-Enter your guess: "))
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        if guess<1 or guess>100:
            print("Please guess a number Between 1-100.")
            continue

        attempts_used+=1
        difference = abs(guess-number_to_guess)

        if guess==number_to_guess:
            print(f"\n Congratulations!!! You guessed it right—the number was {number_to_guess}.")
            print(f"It took you {attempts_used} attempt(s).")
            break
        elif guess<number_to_guess:
            if difference<=close_threshold:
                print("Slightly low! You're getting close — try a bit higher.")
            else:
                print("Too low! Try a higher number.")
        else:
            if difference<=close_threshold:
                print("Slightly high! You're getting close — try a bit lower.")
            else:
                print("Too high! Try a lower number.")

        remaining=max_attempts-attempts_used
        if remaining > 0:
            print(f"Attempts remaining: {remaining}")
    else:
        print(f"\n😢 Game over! You've used all {max_attempts} attempts.")
        print(f"The correct number was {number_to_guess}.")

    print("\nThank You for playing!")


if __name__ == "__main__":
    number_guessing_game()