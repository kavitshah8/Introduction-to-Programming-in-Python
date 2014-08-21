# implementation of card game - Memory
import simplegui
import random

memory_deck = []
state = 0
flipped_card1 = 0
flipped_card2 = 0
exposed = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
click_count = 0

# helper function to initialize globals
def init():
    """
    1. Model the deck of cards used in Memory as a list consisting of 16 numbers with each 
    number lying in the range [0,8) and appearing twice. 
    3. Shuffle the deck using random.shuffle(). 
    
    """
    global memory_deck, state, click_count, exposed
    state = 0    
    click_count = 0
    exposed = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    memory_deck = []
    memory_deck1 = range (0,8)
    memory_deck2 = range (0,8)
    memory_deck = memory_deck1 + memory_deck2
    random.shuffle(memory_deck)
    
        
# define event handlers
def mouseclick(pos):
    global exposed, state
    global flipped_card1, flipped_card2
    global click_count
    # add game state logic here
    
    """
    5. Determine the index of the card from the posiotion of the mouse click
    6. Flip the card based on the index
    """
    i = pos [0] // 50
    
    if exposed[i] == False:
        
        if state == 0:
            exposed[i] = True
            state = 1
            flipped_card1 = i
            click_count +=1
            
        elif state == 1:
            exposed[i] = True
            state = 2
            flipped_card2 = i
            click_count +=1
            
        elif state == 2:
            
            if memory_deck[flipped_card1] != memory_deck[flipped_card2]:
                exposed[flipped_card1] = False
                exposed[flipped_card2] = False
                exposed[i] = True
                flipped_card1 = i
                flipped_card2 = 0
                state = 1  
                click_count +=1
                
            elif memory_deck[flipped_card1] == memory_deck[flipped_card2]:
                exposed[flipped_card1] = True
                exposed[flipped_card2] = True
                exposed[i] = True
                flipped_card1 = i
                flipped_card2 = 0
                state = 1
                click_count +=1
        else:
            pass
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    x_pos = 0
    """
    2.Write a draw handler that iterates through 
    the Memory deck using a for loop and uses draw_text to draw the number associated with each card on the canvas.
    
    4.
    Next, modify the draw handler to either draw a blank green rectangle or the card's value.
    To implement this behavior, we suggest that you create a second list called exposed.
    In the exposed list, the ith entry should be True if the ith card is face up and its value is visible 
    or False if the ith card is face down and it's value is hidden.
    We suggest that you initialize exposed to some known values while testing your drawing code with this modification.
    """
    for n in range(len(exposed)):
        if exposed[n] == True:  
            canvas.draw_text(str(memory_deck[n]),[x_pos+15,65],45,"White","serif")
            x_pos += 50
        else:
            canvas.draw_polygon([(n*50, 0), ((n*50 + 50), 0), (n*50 + 50, 100), ((n*50), 100)], 2, "White", "Green")
            x_pos += 50   
    label.set_text("Moves = "+ str(click_count))
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric
