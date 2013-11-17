""" cardGame.py
    basic card game framework
    keeps track of card locations for as many hands as needed
"""
from random import *

NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2

cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")

def main():
  clearDeck()
  """
  for i in range(5):
    assignCard(PLAYER)
    assignCard(COMP)
  """
  showDeck()
  """
  showHand(PLAYER)
  showHand(COMP)
"""
def clearDeck():
  for cardNum in range(NUMCARDS):
    cardLoc[cardNum] = 0
def showDeck():
  for cardNum in range(NUMCARDS):
    print "%d %d" % (cardNum, cardLoc[cardNum])
  print

def assignCard(hand):
  keepGoing = True
  while keepGoing:
    cardNum = randrange(0, NUMCARDS)
    if cardLoc[cardNum] == DECK:
      cardLoc[cardNum] = hand
      keepGoing = False

def showHand(hand):
  print playerName[hand]
  for cardNum in range(NUMCARDS):
    if cardLoc[cardNum] == hand:
      print getCardName(cardNum)
  print


def getCardName(cardNum):
  #given a cardNum, get a cardName
    print "Displaying Computer Hand"
    for i in range(51):
        if cardLoc[i] ==2:
            cardNum = i /13
            cardRank = i % 13
            print "card Rank #: " + str(cardRank) + "card Suit #: " + str(cardSuit)
            print "t" + rankName[cardRank] + " of " + suitName(cardSuit)

  #get suit
  #get rank
  #concatenate to string
  #return output

if __name__ == "__main__":
  main()