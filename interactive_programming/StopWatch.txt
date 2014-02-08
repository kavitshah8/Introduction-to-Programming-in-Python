# template for "Stopwatch: The Game"
#import templates
import simplegui
import time

# define global variables
current_time = 0
total_stops = 0
success_stops = 0
string = 0

# define helper functions
def format(t):
    """
    input : integer value of time in miliseconds
    return: a string A:BC.D (A = minutes,BC = seconds,D = tenth of a seconds)
    """
    global string        
    tenth_of_seconds = t % 10
    t = t // 10
    
    minutes = t // 60
    
    seconds = (t - minutes * 60)    
    unit_of_seconds = seconds % 10
    tens_of_seconds = seconds // 10
    
    string = str(minutes) +":" +str(tens_of_seconds)+str(unit_of_seconds)+"."+str(tenth_of_seconds)
    return string
   
# define event handlers 
def start_button_handler():
    """
    starts the timer
    """
    timer.start()
def stop_button_handler():
    """
    Does following thing:
    1) stops the timer
    2) Counts the # times stop is pressed
    3) Checks if the stop is success or not by checking the time is whole second or not
    """
    global total_stops
    global success_stops
    if(timer.is_running()):
        timer.stop()
        total_stops += 1
        if string[-1] == "0":
            success_stops +=1   

def reset_button_handler():
    """
    1) stops the timer
    2) resets the necesar global variables
    """
    global current_time
    global total_stops
    global success_stops
    
    if(timer.is_running()):
        timer.stop()
    current_time = 0
    total_stops = 0
    success_stops = 0
        
# define event handler for timer with 0.1 sec interval
def timer_handler():
    """
    updates the current_time by one
    """
    global current_time
    current_time += 1
    
# define draw handler
def draw_handler(canvas):
    """
    1) draws the valus of current time in A:BC.D format 
    2) draws the success / total stops in the upper right corner
    """
    text = format(current_time)
    canvas.draw_text(text,[150,150],50,"white")
    success_total = str(success_stops)+ " / " + str(total_stops)
    canvas.draw_text(success_total,[300,50],40,"white")
    
# create frame and timer
frame = simplegui.create_frame("Stop_Watch",400,300)
timer = simplegui.create_timer(100,timer_handler)

# register draw handlers and event handlers
frame.set_draw_handler(draw_handler)
start = frame.add_button ("Start",start_button_handler,70)
stop = frame.add_button("Stop",stop_button_handler,70)
reset = frame.add_button("Reset",reset_button_handler,70)

# start frame
frame.start()
