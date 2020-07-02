from random import randint

def battleship():
    gameboard = ["O","O","O","O","O"]
    ship = randint(0,4)
    guess = 0

    while guess < 3:
        print(gameboard)
        attempt = input("Guess where my ship is: ")
        attempt = int(attempt)
        guess = guess + 1
        if attempt == ship+1:
            print("Congrats! You win!")
            break
        elif guess == 3:
            print("You missed my ship! You are out of guesses.")
        else:
            print("You missed my ship! Try again!")
            gameboard[attempt - 1] = "X"
    print("Here's the answer: ")
    gameboard[ship] = "S"
    print(gameboard)
    
    print("Good game")
            
        
    
