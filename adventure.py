def adventure():
    #river
    choice = input("You have come across a river. Would you like to swim (1) or boat (2) across?")
    if choice == "1": 
        choice = input("The current is stronger than you thought. Do you keep swimming (1) or try to flag down a boat (2)?")
        if choice == "1": 
            print("You didn't make it! It looks like the current swept you away. Game over.")
            return
        else:
            print("You were saved by a boat! They caried you safely to the other side of the river")
    else: 
        print("The boat carried you safely to the other side of the river.")

    #bear
    choice = input("There is a bear sleeping in the way of your path. Do you tiptoe around the bear (1), or try to jump over the bear (2)?")
    if choice == "1":
        print("You made it around the bear safely! Good job!")
    else:
        choice = input("Oh no! you woke up the bear. He ate you for breakfast. Game over.")
        return

    #cliff
    choice = input("You walk up to a cliff. You have to get to the top somehow. Do you get out your climbing gear and climb up (1), or do you borrow a helicopter (2)?")
    if choice == "1":
        print("Your climbing rope broke while you were on the cliff! You fell to your death. Game over.")
        return
    else:
        print("The helicoper caught on fire, and you plummeted to your death. Game over.")
        return
                   
