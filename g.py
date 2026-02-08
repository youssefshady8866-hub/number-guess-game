import random

def guess_game():
    number = random.randint(1, 100)
    attempts = 0
    print("--- Welcome to the number guessing game ---")
    print("I have chosen a number between 1 and 100. Can you guess it?")

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < number:
                print("Slightly larger! ⬆️")
            elif user_guess > number:
                print("Slightly larger! ⬇️")
            else:
                print(f"🎉 Genius! You knew the number. {number}  {attempts} Attempts.")
                break
        except ValueError:
            print("Please enter only a valid number!")

guess_game()