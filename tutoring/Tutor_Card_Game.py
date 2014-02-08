from random import *
NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2

deck = []
player = []
computer = []

cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")

def main():
    clearDeck()
    for i in range(5):
        assignCard(PLAYER)
        assignCard(COMP)

    showDeck()
    "showHand(PLAYER)"
    "showHand(COMP)"

def assignCard(num):
    if num == 1:
        player.append([rankName,suitName])
        cardLoc = [num]* NUMCARDS
    elif num == 2:
        computer.append([rankName,suitName])
        cardLoc = [num]* NUMCARDS
    else:
        pass

def clearDeck():
    global deck
    for i in range(NUMCARDS):
        deck.append([rankName,suitName])

def showDeck():
    for i in range(NUMCARDS):
        print deck[i]
        print "\n"

def showHand(num):
    if num == 1:
        for i in range(len(player)):
            print player[i]
    elif num == 2:
        for i in range(len(player)):
            print computer[i]
    else:
        pass

main()