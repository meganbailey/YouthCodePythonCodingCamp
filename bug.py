#try to fix the bug in this program

def guessNumber(correctNumber):
    guess = input("Guess a number. ")
    while guess != str(correctNumber):
        guess = input("That was incorrect, please guess another number. ")
    return
