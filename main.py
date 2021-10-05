from player import *
from game import *

def main():
    name = "mic"
    player = Player(name)
    word = chooseWord()
    game = Game(word, player)

    while(not game.endGame()):
        game.printGame()
        letter = input("Chose a letter: ")
        game.tryLetter(letter)

if __name__ == "__main__":
    main()