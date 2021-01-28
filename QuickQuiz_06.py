# Guess the number
# Kind of binary search
# The number of guesses should be limited, i.e (5 or 9).
# Print the number of guesses left.
# Print the number of guesses he took to win the game.
# “Game Over” message should display if the number of guesses becomes equal to 0.

secretNumber = 17
guess = 1
while guess < 10 :
    userNum = int(input("Guess the number: "))
    if userNum == secretNumber :
        print("Congratulations you guessed the number in ", guess, "number of guesses!")
        break
    elif userNum > secretNumber :
        print("Guess a smaller number")
        guess = +1
        print(guess)
        continue
    elif userNum < secretNumber :
        print("Guess a bigger number")
        guess = +1
        print(guess)
        continue
