import random
import numpy as np
from player import *

hagmanImg = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

class Game:
    """
        word
        wordAux
        errors
        player
        wrongLetters

    """

    def __init__(self, word, player):
        self._word = word.lower()
        self._wordAux = [" " for x in range(len(word))]
        self._player = player
        self._wrongLetters = []
        self._errors = 0

    def printGame(self):
        print(self._player)
        print("   {} letters".format(len(self._word)))
        print("wrong letters: {} ".format(self._wrongLetters))
        self.drawnHangman()
        for letter in self._wordAux:
            print(letter, end = ' ') 
        print("")
        for letter in self._wordAux:
            print("—", end = ' ') 
        print("")
        

    def drawnHangman(self):
        print(hagmanImg[self._errors])

    def tryLetter(self,letter):

        letter.lower()
        if letter in self._wrongLetters:
            print("Letter already tryed!") 
        elif letter in self._word:
            for i,l in enumerate(self._word): 
                if(l == letter)  :         
                    self._wordAux[i] = letter
        else:
            self._errors += 1
            self._wrongLetters.append(letter)

    def endGame(self):
        wordAux = ''.join(map(str, self._wordAux))
        print(wordAux)
        if wordAux == self._word:
            print("You win!")
            return True
        elif(self._errors > 5):
            print("You lose!")
            print("the word was {}".format(self._word))
            return True
        else:
            return False



def chooseWord():
    words = ["paralelepipedo", "amarelo", "tigre"]

    n = random.randint(0, len(words)-1)
    word = words[n];

    return word

