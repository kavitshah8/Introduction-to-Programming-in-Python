import simplegui
import random
import math

# initialize global variables used in your code
num_range = 100
ran_num = 0
trials = 0

# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range
    global ran_num
    global trials
    
    num_range = 100
    ran_num = random.randrange(0,100)
    trials = math.ceil (math.log(num_range,2))
    
    print "New Game. Range is 0 to 100"
    print "Number of remaining guess is ", int(trials) , "\n"    

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    global ran_num
    global trials
    
    num_range = 1000
    ran_num = random.randrange(0,1000)
    trials = math.ceil (math.log(num_range,2))
    
    print "New Game. Range is 0 to 1000"
    print "Number of remaining guess is ", int(trials) , "\n"    

def get_input(guess):    
    # main game logic goes here	
    global ran_num
    global trials
   
    trials = trials - 1
    
    if trials > 0:
        print "Guess was ",int(guess)
        print "Number of remaining guesses is ", trials,"\n"
    else:
        print "\nNice try but out of guesses"
        print "Try again : ) \n"
        range100()
    
            
    if int (guess) < ran_num:
            print "Higher!\n"
        
    elif int (guess) > ran_num:
            print "Lower!\n"
        
    elif int(guess)== ran_num:
            print "Correct!\n"
            range100()
     
       
# create frame
frame = simplegui.create_frame("Guess the number", 200,200)

# create control elements and register event handlers for control elements

frame.add_button("Range is [0,100)",range100)
frame.add_button("Range is [0,1000)",range1000)
frame.add_input("Enter a Guess",get_input,200)

# start frame
frame.start()
range100()

# always remember to check your completed program against the grading rubric
