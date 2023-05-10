# Project Name: Blackjack
# Written and Programmed By: Celine Tannous
# Start Date: 09May23
# Finish Date: TBD

# program imports


# main function
def main():

    print("\n--------------")
    print("Casino Vegas")
    print("--------------\n")

    print("Welcome to Casino Vegas! Here we offer a wide range of games, but unfortunately all our machines are inoperable at the moment... However, our blackjack table is available!")
    print("Please see the options below to begin your game: \n")
    
    # opening menu to begin game or close program
    print("1. Begin Game")
    print("2. Quit\n")
    menuSelect = input("Enter your selection here: ")

    errorHandling(menuSelect)

    # first option tree for the player (not correctly written, look up switch cases for syntax)
    match menuSelect:
        case "1":
            return "Blackjack coming soon!\n"
        case "2":
            return "Thank you for playing!\n"
        case "3":
            return 

    return 

# Error Handling Function (not fully completed, still in progress)
def errorHandling(menuSelection):
    try:
        menuSelection = int(menuSelection)

    except:
        return "This is not a valid option input. Please Try Again."
    
    if menuSelection not in ["1", "2"]:
        return "This is not one of the available options. Please try again."
    
    return

# Blackjack function
def blackjack():

    # player variables
    bank = 500
    bet = 0
    bust = False
    total = 0
    hand = []

    # dealer variables
    bust = False
    total = 0
    hand = []
    deck = ["A","A","A","A",2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10]



# function calls main when program is run
if __name__ == "__main__":
    print(main())

