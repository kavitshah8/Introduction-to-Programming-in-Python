""" cardGame.py
    basic card game framework
    keeps track of card locations for as many hands as needed
"""
from random import *

NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2

card = [0] * NUMCARDS
cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")

def main():
  clearDeck()

  for i in range(5):
    assignCard(PLAYER)
    assignCard(COMP)
  showDeck()
  showHand(PLAYER)
  showHand(COMP)

def clearDeck():
  for num in range(NUMCARDS):
    card[num] = str(rankName[num%13])+" of "+str(suitName[num/13])
    cardLoc[num] = playerName[0]

def showDeck():
  print "#" + "\tcard\t\t\t"+"  location"
  for num in range(NUMCARDS):
    print str(num)+"\t"+card[num]+"\t\t"+cardLoc[num]

def assignCard(hand):
  rand_num = randrange(0, NUMCARDS)
  cardLoc[rand_num] = playerName[hand]

def showHand(hand):
  print "Displaying ", playerName[hand],"hand:"
  for num in range(NUMCARDS):
    if cardLoc[num] == playerName[hand]:
        print card[num]

if __name__ == "__main__":
  main()