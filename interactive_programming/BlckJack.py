# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

DEALER_POS = (60, 175)
PLAYER_POS = (60, 425)

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.has_ace = False
        self.busted = False
        pass	# create Hand object

    def __str__(self): # return a string representation of a hand
        hand = "Hand Contains "
        for i in range(len(self.cards)):
            hand += str(self.cards[i]) + " "
        return  hand 
    
    def add_card(self, card):
        self.cards.append(card)
        pass	# add a card object to a hand

    def get_value(self):  # compute the value of the hand, see Blackjack video
        
        self.value = 0
        for i in range(len(self.cards)):      
            self.value += VALUES[self.cards[i].get_rank()]
            
            if self.cards[i].get_rank() == 'A': # Checks if the hand has an Ace
                self.has_ace = True               
                           
        if self.has_ace == True:   # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
            if (self.value + 10) <= 21:
                return self.value + 10
            else:
                return self.value
        else:
            return self.value        
  
   
    def draw(self, canvas, pos):  # draw a hand on the canvas, use the draw method for cards
        
        hand_loc = pos[0]
        for i in range(len(self.cards)):
            self.cards[i].draw(canvas, ((hand_loc + (i * 80)), pos[1]))
       
# define deck class 
class Deck:
    def __init__(self):   # create a Deck object
        
        self.cards = []
        for n in SUITS:
            for m in RANKS:
                self.cards.append(Card(n,m))                                                                       

    def shuffle(self):   # add cards back to deck and shuffle
        random.shuffle(self.cards)   # use random.shuffle() to shuffle the deck
        
    def deal_card(self):  # deal a card object from the deck
        if (len(self.cards)) >= 1:
            return self.cards.pop(random.randrange(0,len(self.cards)))
        else:
            print "Not enough cards left!"
    
    def __str__(self): # return a string representing the deck
        deck = "Deck Contains "
        for i in range(len(self.cards)):
            deck += str(self.cards[i]) + " "
        return deck 
    

#define event handlers for buttons
def deal():  # shuffles a new deck, deals out cards
    global outcome, in_play, score
    global my_deck, players_hand, dealers_hand

    if in_play == True:  # Clicking on Deal during round stops round and player loses
        outcome = "You Lost! New Deal?"
        score -= 1
        in_play = False
        return       
    
    my_deck = Deck()
    my_deck.shuffle()
    players_hand = Hand()
    dealers_hand = Hand()
    
    for i in range(2):
        players_hand.add_card(my_deck.deal_card())
        dealers_hand.add_card(my_deck.deal_card())
        
    outcome = "Hit or Stand?"
    
    in_play = True
    
def hit():   # if the hand is in play, hit the player
    global my_deck, players_hand, dealers_hand
    global outcome, in_play, score
    
    if in_play == True:  # Checks if playing or not
        
        players_hand.add_card(my_deck.deal_card())  # adds card to hand
        if players_hand.get_value() > 21:  # Player busts
            players_hand.busted = True
            outcome = "You Lost. New Deal?"
            score -= 1
            in_play = False

def stand():
    global my_deck, players_hand, dealers_hand
    global outcome, in_play, score
    
    if in_play == True:  # Checks if playing or not
        
        if players_hand.busted == True:
            return
        else:
            while (dealers_hand.get_value() < 17):  # dealer hits if under 17
                dealers_hand.add_card(my_deck.deal_card())
                           
            if dealers_hand.get_value() > 21:  # dealer busted
                dealers_hand.busted = True
                score += 1
                outcome = "You won! New Deal?"

            else:
                if dealers_hand.get_value() < players_hand.get_value():
                    outcome = "You won! New Deal?"
                    score += 1
                else:
                    outcome = "You lost! New Deal?"
                    score -= 1
                      
        in_play = False    


# draw handler    
def draw(canvas):
   
    dealers_hand.draw(canvas, DEALER_POS)
    players_hand.draw(canvas, PLAYER_POS)
    
    if in_play == True:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [DEALER_POS[0] + CARD_BACK_CENTER[0], DEALER_POS[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
       
    canvas.draw_text("Blackjack", (175, 50), 55, "Blue")
    canvas.draw_text("Score: " + str(score), (450, 80), 25, "Black")
    canvas.draw_text("Dealer's Hand", (70, 150), 30, "Blue")
    canvas.draw_text("Player's Hand", (70, 400), 30, "Blue")
    canvas.draw_text("Dealer stands on 17 or above and wins ties.", (40, 80), 20, "Black")
    canvas.draw_text(str(outcome), (350, 400), 25, "Blue")
    
    if players_hand.busted == True:
        canvas.draw_text("Busted", (250, 400), 25, "Red")
        
    if dealers_hand.busted == True:
        canvas.draw_text("Busted", (275, 150), 25, "Red")
        
    if in_play == False:
        canvas.draw_text("Player: "+str(players_hand.get_value()), (100, 550), 25, "Aqua")
        canvas.draw_text("Dealer: "+str(dealers_hand.get_value()), (100, 300), 25, "Aqua")

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
frame.start()

# more globals
my_deck = Deck()
players_hand = Hand()
dealers_hand = Hand()




# remember to review the gradic rubric
