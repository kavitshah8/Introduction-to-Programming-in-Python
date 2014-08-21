# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left

def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    """
    2. Add code to the function ball_init that spawns a ball in the middle of the table and assigns the ball a fixed velocity (for now).
       Ignore the parameter right for now.
    """
    ball_pos = [WIDTH // 2, HEIGHT//2]
    ball_vel = [0,0]
    
    
    """
    5. Add randomization to the velocity in ball_init(right)
       The velocity of the ball should be upwards and towards the right if right == True
       The velocity of the ball should be upwards and towards the left if right == False. 
    """    
    if bool(right) == True :
        """
        5. Ball Velocity Upwards and towards Right 
        """
        ball_vel[0] = random.randrange(2,4)
        ball_vel[1] = -random.randrange(1,3)
            
    elif bool(right) == False:
        """
        5. Ball velocity Upwardss and towards Left
        """
        ball_vel[0] = -random.randrange(2,4)
        ball_vel[1] = -random.randrange(1,3)
     
    # define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    
    #12. Reset the scores before calling them
    score1 = 0
    score2 = 0
    #3. Add a call to ball_init in the function new_game which starts a game of Pong
    ball_init(random.randrange(0,2))
    
    #7.The vertical positions of these two paddles should depend on two global variables.
    paddle1_pos = HEIGHT //2 
    paddle2_pos = HEIGHT//2
    
    #8.The update should reference two global variables that contain the vertical velocities of the paddles
    paddle1_vel = 0 
    paddle2_vel = 0

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    #10. TO keep the paddles on the canvas
    global paddle1_vel, paddle2_vel
    """
    1. We recommend that you add the positional update for the ball to 
    the draw handler as shown in the second part of the "Motion" video.
    """
    ball_pos[0] += ball_vel[0] 
    ball_pos[1] += ball_vel[1] 
    
    """
    4.Modify your code such that the ball collides with and bounces off 
      of the top and bottom walls.
    """    
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= (HEIGHT - 1)- BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    # 6. ,11. , 12. 
    #6. Collision with the left and right gutters.
    #11. To check did ball hit the paddle or not
    #12. Modertely increase he speed of the ball everytime it hits the paddle
    elif ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if ball_pos[1]<= paddle1_pos + HALF_PAD_HEIGHT and ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT:
            ball_vel[0] = -(1.1*ball_vel[0])                    
        else:
            score2 += 1
            ball_init (True)
    elif ball_pos[0] >= (WIDTH-1)-(BALL_RADIUS + PAD_WIDTH):
        if ball_pos[1]<= paddle2_pos + HALF_PAD_HEIGHT and ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT:
            ball_vel[0] = -(1.1*ball_vel[0])                    
        else:
            score1 += 1
            ball_init (False)
    
    
    # update paddle's vertical position, keep paddle on the screen
    # 8.Add code that modifies the values of these vertical positions via an update in the draw handler.    
    # 10.Restrict your paddles to stay entirely on the canvas by adding a check before you update 
    #    the paddles' vertical positions in the draw handler.
    
    if (paddle1_pos - HALF_PAD_HEIGHT > 0 or paddle1_vel > 0):
        paddle1_pos += paddle1_vel
    else :
        paddle1_vel = 0        
    
    if paddle1_pos + paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    else :
        paddle1_vel = 0        
        
    if (paddle2_pos - HALF_PAD_HEIGHT > 0 or paddle2_vel > 0):
        paddle2_pos += paddle2_vel
    else :
        paddle2_vel = 0        
    
    if paddle2_pos + paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel
    else :
        paddle2_vel = 0      
    
    
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    #7.Next, add code that draws the left and right paddles in their respective gutters
    c.draw_line([0, paddle1_pos-(PAD_HEIGHT//2)], [0, paddle1_pos+(PAD_HEIGHT//2)],2*PAD_WIDTH,"White")
    c.draw_line([WIDTH, paddle2_pos-(PAD_HEIGHT//2)], [WIDTH, paddle2_pos+(PAD_HEIGHT//2)],2*PAD_WIDTH,"White") 
    # update ball
            
    # draw ball and scores
    #1. Add code to the program template that draws a ball moving across the Pong table.
    c.draw_circle(ball_pos,BALL_RADIUS,1,"Red","white")
    c.draw_text(str(score1),[100,30],30,"Red")
    c.draw_text(str(score2),[400,30],30,"Red")
            
def keydown(key):
    global paddle1_vel, paddle2_vel
    """
    9. Update the values of these two vertical velocities using key handlers
       The left paddle moves up at a constant velocity if the "w" key is pressed 
       And moves down at a constant velocity if the "s" is pressed 
       And is motionless if neither is pressed.
    """
    acc = 1
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = acc
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = acc
    
      
def keyup(key):
    global paddle1_vel, paddle2_vel
    """
    9. Update the values of these two vertical velocities using key handlers
       The left paddle moves up at a constant velocity if the "w" key is pressed 
       And moves down at a constant velocity if the "s" is pressed 
       And is motionless if neither is pressed.
    """
    acc = 0
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = acc
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = acc

def restart():
    new_game()
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
restart = frame.add_button("Restart",restart)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# 3.Then add a call to new_game in the main body of your program
new_game()

# start frame
frame.start()
