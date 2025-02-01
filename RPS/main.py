from graphics import Canvas
#import tkinter
   
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 200
NUM_Rounds = 0 #number of rounds
game = 0 #version of the game
points = 0 #Starting points for working out %

"""This is a game of Rock Paper Scissors, Rock Paper Scissors Lizard Spock or Cat Mouse Elephant
the game will start by asking you which version of the game you wish to play
then it will ask you how many rounds you will like to play 1, best of 3 or best of 5
You win the game by
Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
Rock crushes Scissors
For Cat Mouse Elephant the wining combos are:
Cat chases Mouse
Mouse spooks Elephant
Elephant scares cat

At the end of the rounds you will be told your results and also given a % result example 
3/5 game won would be 60%
At each round show an image that relates to the challenge"""

def main():
    game = Pick_Game()
    # Start game and pick game version
    Start_game(game)
    another_game()



    
def another_game():    
    while True:
        play_again = input("Do you want to play another game? ((Y)es/(N)o): ").upper() #upper added so that player can input either Y or y
        if play_again == "Y":
            game = Pick_Game()
            Start_game(game)  
        elif play_again == "N":
            print("\nSorry to see you go, come back soon")
            break
        else:
            print("Incorrect input. Please enter 'Y' for Yes or 'N' for No.\n")


def Start_game(game):
    points = 0 #Starting points for working out %
    NUM_Rounds = rounds()
    if game == 1:
        print("\nYou chose the game Rock Paper Scissors!\n\nWin combinations\nScissors cuts Paper\nPaper covers Rock\nRock crushes Scissors\n")
        for i in range(NUM_Rounds):
            points = RPS(points)
        pct = (points / NUM_Rounds) * 100
        pct = int(round(pct))
        print("You scored - "+str(points)+"/"+str(NUM_Rounds)+" "+str(pct)+"%")
        if points == NUM_Rounds:
            print("Wow! you played perfectly!")
        elif points > round(int(NUM_Rounds/2)):
            print("Good job! you played really well!")
        else:
            print("Better luck next time!")
        print ("Thanks for playing!\n")
    if game == 2:
        print("\nYou chose the Rock Paper Scissors Lizard Spock!\n\nwin combinations\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\nRock crushes Scissors")
        for i in range(NUM_Rounds):
            points = RPSLS(points)
        pct = (points / NUM_Rounds) * 100
        pct = int(round(pct))
        print("You scored - "+str(points)+"/"+str(NUM_Rounds)+" "+str(pct)+"%")
        if points == NUM_Rounds:
            print("Wow! you played perfectly!")
        elif points > round(int(NUM_Rounds/2)):
            print("Good job! you played really well!")
        else:
            print("Better luck next time!")
        print ("Thanks for playing!\n")
    elif game == 3:
        print("\nYou chose the game Cat Mouse Elephant!\n\nWin combinations\nCat chases Mouse\nMouse spooks Elephant\nElephant scares cat\n")
        for i in range(NUM_Rounds):
            points = CME(points)
        pct = (points / NUM_Rounds) * 100
        pct = int(round(pct))
        print("You scored - "+str(points)+"/"+str(NUM_Rounds)+" "+str(pct)+"%")
        if points == NUM_Rounds:
            print("Wow! you played perfectly!")
        elif points > round(int(NUM_Rounds/2)):
            print("Good job! you played really well!")
        else:
            print("Better luck next time!")
        print ("Thanks for playing!\n")
       

def Pick_Game():
    # Show the title of the game
    print("\n------------------------------------\nROCK PAPER SCISSORS\nROCK PAPER SCISSORS LIZARD SPOCK\nCAT MOUSE ELEPHANT\n------------------------------------\n")
    # Ask game version
    while True:
        game = input("Input the number of the game you want to play. \n1) Rock Paper Scissors\n2) Rock Paper Scissors Lizard Spock\n3) Cat Mouse Elephant\n")
        # Check if the input is an integer
        if game.isdigit():
            game = int(game)
            if game == 1 or game == 2 or game == 3:
                return game
            else:
                print("\nIncorrect input. Please enter 1, 2 or 3")
        else:
            print("\nInvalid input. Please enter a valid number.")


def rounds():
    # Ask for number of rounds
    while True:
        NUM_Rounds = input("\nInput the number of rounds you wish to play. \n1) Single round\n3) Best of three\n5) Best of Five\n")
        # Check if the input is an integer
        if NUM_Rounds.isdigit():
            NUM_Rounds = int(NUM_Rounds)
            if NUM_Rounds == 1 or NUM_Rounds == 3 or NUM_Rounds == 5:
                return NUM_Rounds
            else:
                print("\nIncorrect input. Please enter 1, 3 or 5")
        else:
            print("\nInvalid input. Please enter a valid number.")


  
def RPS(points):
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    import random
    computer = int(random.randint(1, 3))
    while True:
        player = input("Input the number for your selection:\n1-Rock\n2-Paper\n3-Scissors\nSelection = ")
        print("")
        # Check if the input is an integer
        if player.isdigit():
            player = int(player)
            if player == 1 or player == 2 or player == 3:
                break
            else:
                print("Incorrect input. Please enter 1, 2, or 3") # this code is for numbers
        else:
            print("Invalid input. Please enter a valid number.") # this code is for letters
    #win combinations
    """Scissors cuts Paper
    Paper covers Rock
    Rock crushes Scissors"""
    if player == 3 and computer == 2:
        print("You picked Scissors\nComputer picked Paper\nYou win\nScissors cuts Paper\n\n")
        canvas.create_image(0, 0, "WSCP.png")
        points = points + 1
    elif player == 2 and computer == 1:
        print("You picked Paper\nComputer picked Rock\nYou win\nPaper covers Rock\n\n")
        canvas.create_image(0, 0, "WPCR.png")
        points = points + 1
    elif player == 1 and computer == 3:
        print("You picked Rock\nComputer picked Scissors\nYou win\nRock crushes Scissors\n\n")
        canvas.create_image(0, 0, "WRCS.png")
        points = points + 1
    elif player == 2 and computer == 3:
        print("You picked Paper\nComputer picked Scissors\nYou lose\nScissors cuts Paper\n\n")
        canvas.create_image(0, 0, "LSCP.png")
        points = points
    elif player == 1 and computer == 2:
        print("You picked Rock\nComputer picked Paper\nYou lose\nPaper covers Rock\n\n")
        canvas.create_image(0, 0, "LPCR.png")
        points = points
    elif player == 3 and computer == 1:
        print("You picked Scissors\nComputer picked Rock\nYou lose\nRock crushes Scissors\n\n")
        canvas.create_image(0, 0, "LRCS.png")
        points = points
    elif player == 1 and computer == 1:
        print("You picked Rock\nComputer picked Rock\nIt's a Tie\n\n")
        canvas.create_image(0, 0, "TR.png")
        points = points   
    elif player == 2 and computer == 2:
        print("You picked Paper\nComputer picked Paper\nIt's a Tie\n\n")
        canvas.create_image(0, 0, "TP.png")
        points = points
    elif player == 3 and computer == 3:
        print("You picked Scissors\nComputer picked Scissors\nIt's a Tie\n\n")
        canvas.create_image(0, 0, "TS.png")
        points = points
    return points



def RPSLS(points):
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    import random
    computer = int(random.randint(1, 5))
    while True:
        player = input("Input the number for your selection:\n1-Rock\n2-Paper\n3-Scissors\n4-Lizard\n5-Spock\nSelection = ")
        print("")
        # Check if the input is an integer
        if player.isdigit():
            player = int(player)
            if player == 1 or player == 2 or player == 3 or player == 4 or player == 5:
                break
            else:
                print("Incorrect input. Please enter 1, 2, 3, 4 or 5") # this code is for numbers
        else:
            print("Invalid input. Please enter a valid number.") # this code is for letters
    #win combinations
    """Scissors cuts Paper
    Paper covers Rock
    Rock crushes Lizard
    Lizard poisons Spock
    Spock smashes Scissors
    Scissors decapitates Lizard
    Lizard eats Paper
    Paper disproves Spock
    Spock vaporizes Rock
    Rock crushes Scissors"""
    if player == 3 and computer == 2:
        print("You picked Scissors\nComputer picked Paper\nYou win\nScissors cut Paper\n\n")
        canvas.create_image(0,0,"WSCP.png")
        points = points + 1
    elif player == 2 and computer == 1:
        print("You picked Paper\nComputer picked Rock\nYou win\nPaper covers Rock\n\n")
        canvas.create_image(0,0,"WPCR.png")
        points = points + 1
    elif player == 1 and computer == 4:
        print("You picked Rock\nComputer picked Lizard\nYou win\nRock crushes Lizard\n\n")
        canvas.create_image(0,0,"WRCL.png")
        points = points + 1
    elif player == 4 and computer == 5:
        print("You picked Lizard\nComputer picked Spock\nYou win\nLizard poisons Spock\n\n")
        canvas.create_image(0,0,"WLPS.png")
        points = points + 1
    elif player == 5 and computer == 3:
        print("You picked Spock\nComputer picked Scissors\nYou win\nSpock smashes Scissors\n\n")
        canvas.create_image(0,0,"WSSS.png")
        points = points + 1
    elif player == 3 and computer == 4:
        print("You picked Scissors\nComputer picked Lizard\nYou win\nScissors decapitates Lizard\n\n")
        canvas.create_image(0,0,"WSDL.png")
        points = points + 1
    elif player == 4 and computer == 2:
        print("You picked Lizard\nComputer picked Paper\nYou win\nLizard eats Paper\n\n")
        canvas.create_image(0,0,"WLEP.png")
        points = points + 1
    elif player == 2 and computer == 5:
        print("You picked Paper\nComputer picked Spock\nYou win\nPaper disproves Spock\n\n")
        canvas.create_image(0,0,"WPDS.png")
        points = points + 1
    elif player == 5 and computer == 1:
        print("You picked Spock\nComputer picked Rock\nYou win\nSpock vaporizes Rock\n\n")
        canvas.create_image(0,0,"WSVR.png")
        points = points + 1
    elif player == 1 and computer == 3:
        print("You picked Rock\nComputer picked Scissors\nYou win\nRock crushes Scissors\n\n")
        canvas.create_image(0,0,"WRCS.png")
        points = points + 1
    elif player == 2 and computer == 3:
        print("You picked Paper\nComputer picked Scissors\nYou lose\nScissors cut Paper\n\n")
        canvas.create_image(0,0,"LSCP.png")
        points = points 
    elif player == 1 and computer == 2:
        print("You picked Rock\nComputer picked Paper\nYou lose\nPaper covers Rock\n\n")
        canvas.create_image(0,0,"LPCR.png")
        points = points
    elif player == 4 and computer == 1:
        print("You picked Lizard\nComputer picked Rock\nYou lose\nRock crushes Lizard\n\n")
        canvas.create_image(0,0,"LRCL.png")
        points = points
    elif player == 5 and computer == 4:
        print("You picked Spock\nComputer picked Lizard\nYou lose\nLizard poisons Spock\n\n")
        canvas.create_image(0,0,"LLPS.png")
        points = points
    elif player == 3 and computer == 5:
        print("You picked Scissors\nComputer picked Spock\nYou lose\nSpock smashes Scissors\n\n")
        canvas.create_image(0,0,"LSSS.png")
        points = points
    elif player == 4 and computer == 3:
        print("You picked Lizard\nComputer picked Scissors\nYou lose\nScissors decapitates Lizard\n\n")
        canvas.create_image(0,0,"LSDL.png")
        points = points
    elif player == 2 and computer == 4:
        print("You picked Paper\nComputer picked Lizard\nYou lose\nLizard eats Paper\n\n")
        canvas.create_image(0,0,"LLEP.png")
        points = points
    elif player == 5 and computer == 2:
        print("You picked Spock\nComputer picked Paper\nYou lose\nPaper disproves Spock\n\n")
        canvas.create_image(0,0,"LPDS.png")
        points = points
    elif player == 1 and computer == 5:
        print("You picked Rock\nComputer picked Spock\nYou lose\nSpock vaporizes Rock\n\n")
        canvas.create_image(0,0,"LSVR.png")
        points = points
    elif player == 3 and computer == 1:
        print("You picked Scissors\nComputer picked Rock\nYou lose\nRock crushes Scissors\n\n")
        canvas.create_image(0,0,"LRCS.png")
        points = points
    elif player == 1 and computer == 1:
        print("You picked Rock\nComputer picked Rock\nIt's a tie\n\n")
        canvas.create_image(0,0,"TR.png")
        points = points
    elif player == 2 and computer == 2:
        print("You picked Paper\nComputer picked Paper\nIt's a tie\n\n")
        canvas.create_image(0,0,"TP.png")
        points = points
    elif player == 3 and computer == 3:
        print("You picked Scissors\nComputer picked Scissors\nIt's a tie\n\n")
        canvas.create_image(0,0,"TS.png")
        points = points
    elif player == 4 and computer == 4:
        print("You picked Lizard\nComputer picked Lizard\nIt's a tie\n\n")
        canvas.create_image(0,0,"TL.png")
        points = points
    elif player == 5 and computer == 5:
        print("You picked Spock\nComputer picked Spock\nIt's a tie\n\n")
        canvas.create_image(0,0,"TSP.png")
        points = points
    return points

def CME(points):
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    import random
    computer = int(random.randint(1, 3))
    while True:
        player = input("Input the number for your selection:\n1-Cat\n2-Mouse\n3-Elephant\nSelection = ")
        print("")
        # Check if the input is an integer
        if player.isdigit():
            player = int(player)
            if player == 1 or player == 2 or player == 3:
                break
            else:
                print("Incorrect input. Please enter 1, 2, or 3") # this code is for numbers
        else:
            print("Invalid input. Please enter a valid number.") # this code is for letters
    #win combinations
    #Cat chases Mouse
    #Mouse spooks Elephant
    #Elephant scares cat
    if player == 3 and computer == 2:
        print("You picked Elephant\nComputer picked mouse\nYou lose\nMouse spooks Elephant\n\n")
        canvas.create_image(0,0,"LMSE.png") 
        points = points 
    elif player == 2 and computer == 1:
        print("You picked Mouse\nComputer picked Cat\nYou lose\nCat chases Mouse\n\n")
        canvas.create_image(0,0,"LCCM.png") 
        points = points
    elif player == 1 and computer == 3:
        print("You picked Cat\nComputer picked Elephant\nYou lose\nElephant scares cat\n\n")
        canvas.create_image(0,0,"LESC.png") 
        points = points
    elif player == 2 and computer == 3:
        print("You picked Mouse\nComputer picked Elephant\nYou Win\nMouse spooks Elephant\n\n")
        canvas.create_image(0,0,"WMSE.png") 
        points = points + 1
    elif player == 1 and computer == 2:
        print("You picked Cat\nComputer picked Mouse\nYou Win\nCat chases Mouse\n\n")
        canvas.create_image(0,0,"WCCM.png") 
        points = points + 1
    elif player == 3 and computer == 1:
        print("You picked Elephant\nComputer picked Cat\nYou Win\nElephant scares cat\n\n")
        canvas.create_image(0,0,"WESC.png") 
        points = points + 1
    elif player == 1 and computer == 1:
        print("You picked Cat\nComputer picked Cat\nIt's a Tie\nCat Befriends Cat\n\n")
        canvas.create_image(0,0,"TC.png") 
        points = points
    elif player == 2 and computer == 2:
        print("You picked Mouse\nComputer picked Mouse\nIt's a Tie\nMouse Befriends Mouse\n\n")
        canvas.create_image(0,0,"TM.png") 
        points = points
    elif player == 3 and computer == 3:
        print("You picked Elephant\nComputer picked Elephant\nIt's a Tie\nElephant Befriends Elephant\n\n")
        canvas.create_image(0,0,"TE.png") 
        points = points
    return points


if __name__ == '__main__':
    main()