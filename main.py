import random
import art
Guessing_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44,
                 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65,
                 66, 67, 68, 69, 70, 71, 72, 73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,
                 91,92,93,94,95,96,97,98,99,100]

guess_no = random.choice(Guessing_data)

print(f"correct answer is {guess_no}")
print(art.logo)
print("Welcome to Number Guessing Game\n")

Number_of_guesses = 0
if input("You want to play easy or hard level :").lower() == "easy":
    Number_of_guesses = 10
else:
    Number_of_guesses = 5


Guessed_right = False

print(f"You have {Number_of_guesses} chances to guess the correct number")

while not Guessed_right:
    try:
        guess = int(input("\nMake a guess between 1 and 100: "))
    except ValueError:
        print("Please enter a valid number. ")
        continue
    Number_of_guesses -= 1
    if guess == guess_no:
        print("You guessed it right  🥳🥳")
        Guessed_right = True
    elif guess > guess_no:
        print("Too high")
        print(f"You have {Number_of_guesses} of attempts left ")
    else:
        print("Too low")
        print(f"You have {Number_of_guesses} of attempts left ")
    if Number_of_guesses == 0:
        print(f"\nYou ran out of chances 😔")
        Guessed_right = True


