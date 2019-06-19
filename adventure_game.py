import time
import random
import gameData


# build the paused mssage function
def printPause(msg):
    msg.lower()
    print(msg)
    time.sleep(2)


# build player input function
def trackInput(msg):
    resp = input(msg).lower()
    return resp

# build a user input router function


def router(resp, fun1, fun2, option1, option2):

    if resp == option1:
        return fun1()
    elif resp == option2:
        return fun2()
    elif resp != option1 or resp != option2:
        print("I can't understand this choice")
        router(trackInput(f"Enter  {option1}  or, Enter {option2}\n"),
               fun1, fun2, option1, option2)


# build a game closure
def game():
    def scenario():

        x = []
        for i in range(len(gameData.fields)):

            x.append(i)
        return (random.choice(x))

    # build the game field function
    def field():

        printPause("Hello Warrior, welcome to the middle of nowhere")
        printPause(f"you woke up to find yourself in a {gameData.fields[i]}")
        printPause(
            f"In front of you, there is a "
            f"creepy {gameData.dangerousPlaces[i]}")
        printPause(f"At your left, you can see a {gameData.savePlaces[i]}")
        printPause("You have to choose where to go")
        router(trackInput(
            f"Enter 1 to go to the {gameData.dangerousPlaces[i]},"
            f" Enter 2 to go to the {gameData.savePlaces[i]}\n"),
            dangerousPlaces, savePlaces, "1", "2")
    # build a winner function

    def win():

        printPause(
            f"WOW, you are really great in using {gameData.weapons[i]}"
            f" to kill a {gameData.enamies[i]}\n")
        printPause("Congratulations you won this game".upper())
        playAgain()

    # build a loser function
    def lose():

        printPause(f"Sorry, you lose this game\n")
        playAgain()

    # build play again function
    def playAgain():

        scenario()
        printPause("Love to play again?")
        router(trackInput(
            f"Enter 1 to Play Again, Enter 2 to Quit the Game\n"),
            game, quitGame, "1", "2")

    # build quit game function
    def quitGame():

        printPause(
            "mmm, you have something to do\nThat's OK, have a nice day, bye")

    # build weapon functionGame
    def collectWeapon():

        printPause(
            f"WOW, you found a {gameData.weapons[i]}in"
            f" the {gameData.savePlaces[i]}")
        printPause("you can take it now, it maybe useful")
        router(trackInput(
            f"Enter 1 to back to the {gameData.dangerousPlaces[i]} and "
            f"see who is there, Enter 2 to runaway\n"),
            fight, runAway, "1", "2")

    # build the runaway function
    def runAway():

        printPause("OH what a choice you made")
        printPause("after running for more than an hour")
        printPause("you are feeling so thursty")
        printPause("another 6 hours gone with no water")
        printPause("after 5 days, YOU ARE DEAD ")
        lose()

    # build explor function
    def explore():

        printPause(f"without a weapon you can't defend yourself")
        printPause(f"why don't you go to the {gameData.savePlaces[i]}")
        printPause("you may find a weapon")
        router(trackInput(
            f"Enter 1 to search a weapon, Enter 2 to runaway\n"),
            collectWeapon, runAway, "1", "2")

    # buils fight function
    def fight():

        printPause(f"OH, you can see a {gameData.enamies[i]}")
        printPause("you have to kill him now")
        printPause(f"{gameData.enamies[i]} is dangrous")
        printPause(f"but you can use the {gameData.weapons[i]}")
        win()

    # build dangerous places function
    def dangerousPlaces():

        printPause(f"OH It seems you realy have a lion heart")
        printPause(
            f"you are going to find what is going"
            f" on into this {gameData.dangerousPlaces[i]}")
        printPause(
            f"a {gameData.dangerousPlaces[i]} like this"
            f" is a good place for a {gameData.enamies[i]}"
            " to hide\nBE CAREFUL")
        router(trackInput(f"Enter 1 to explor, Enter 2 to runaway\n"),
               explore, runAway, "1", "2")

    # build save places function
    def savePlaces():

        printPause(
            f"mmm It seems you prefare being"
            f" alone in the {gameData.savePlaces[i]}")
        printPause("Now, you can see something shiny inside")
        router(trackInput(
            f"Enter 1 to enter the {gameData.savePlaces[i]},"
            f" Enter 2 to runaway\n"),
            collectWeapon, runAway, "1", "2")

    # call the functions
    i = scenario()
    field()


game()
