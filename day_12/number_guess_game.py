import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
guess_num = random.randint(1,100)
diff_type = str(input("Choose a difficulty. Type 'easy' or 'hard': ")).lower()

if diff_type == "easy":
    chance = 10
    print(f"You have {chance} attempts remaining to guess the number.")
    guess_choice = int(input("Make a guess: "))
    while chance > 0:
        if guess_choice > guess_num:
            print("Too low.")
            print("Guess again.")
            chance = chance - 1
            print(f"You have {chance} attempts remaining to guess the number.")
        elif guess_choice < guess_num:
            print("Too high.")
            print("Guess again.")
            chance = chance - 1
            print(f"You have {chance} attempts remaining to guess the number.")
        elif guess_choice == guess_num:
            print(f"You got it! The answer was {guess_num}")

