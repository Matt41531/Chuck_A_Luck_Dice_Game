from graphics import *
from random import *
def draw_dice(x,y,dienum,win):
    '''
    Purpose: draw a dice image on the screen at the location given, using
         the corresponding gif file
    Pre-conditions:  (int) x and y of location, (int) number of the die, 
         (GraphWin) graphics window
    Post-condition:  (Image) returns the Image object created
    '''
    
    point = Point(x,y)
    dice = ''.join([str(dienum), '.gif'])
    die = (Image(point, dice))
    die.draw(win)
    return die

def getbet(pot, win):
    '''
    Purpose:  get the amount of the bet from the user
    while not letting the user bet less than 1 dollar and not more
    than they have in the pot
    Pre-conditions:  (int) the amount of the pot and the graphics window
    Post-conditions:  (int) the validated user's input (from 1 to amount of pot)
    '''    
    inputs = "Enter a bet from 1 - " + str(pot) +"$"
    input_txt = Text(Point(400,400), inputs)
    input_txt.draw(win)
    bet_box = Entry(Point(400, 450), 5)
    bet_box.draw(win)
    bet_box.setText(1) #To prevent misclicks from crashing program with '' <1 in while loop
    
    win.getMouse()
    bet = bet_box.getText()
    bet = int(bet)
    while bet<1 or bet>pot:
        if bet <1:
            feedback_txt = Text(Point(400,500), 'That bet is too low!')
        else:
            feedback_txt = Text(Point(400,500), 'You don\'t have that much money!')
        feedback_txt.draw(win)
        bet_box.setText(1)
        win.getMouse()
        bet = int(bet_box.getText())
        feedback_txt.undraw()   
    input_txt.undraw()
    bet_box.undraw()
    
    return bet
        
def getnumber(win):
    
    '''     
    Purpose: get the die number the user wants to bet on (1-6) 
    Pre-conditions:  graphics window
    Post-conditions:   validated user's input (1-6)
    '''
    
    number_txt = Text(Point(400,350), "Enter a die number to bet on 1-6")
    number_txt.draw(win)
    number_box = Entry(Point(400,400), 5)
    number_box.draw(win)
    number_box.setText('1')
    
    win.getMouse()
    user_roll = number_box.getText() #To avoid crash, do not convert to int until anwser validated as 1-6
    
    while user_roll not in "123456":
        feedback = Text(Point(400,600), "That's not a valid bet!")
        feedback.draw(win)
        number_box.setText('1')
        win.getMouse()
        user_roll = number_box.getText()
        feedback.undraw()
        
    user_roll = int(user_roll)
    number_box.undraw()
    number_txt.undraw()
    return user_roll   

def check_matches(roll1, roll2, roll3, user_roll):
    
    '''
    Purpose:  compare the user's roll to the three rolls 
    and find out if there are 0, 1, 2, or 3 matches
    Pre-conditions:  three rolls and user's roll
    Post-conditions:  0-3, number of matches
    '''
    num_matches = 0
    
    if user_roll == roll1:
        num_matches += 1
        
    if user_roll == roll2:
        num_matches += 1
        
    if user_roll == roll3:
        num_matches += 1    
        
    return num_matches
    
def in_box(point1, point2, clickpoint):
    '''
    Purpose:  to test a point to see if it is in a box defined by
    two other points (upper right and lower left) 
    Pre-conditions:  two points that define the box, a third point
    Post-conditions:  True if point3 is inside the box,
        False if not
    Design:
        initialize flag
        if the point's X is inside the other points' X's and
           the point's Y is inside the other points' Y's
              flag is set True
        return the flag
        '''
    flag = False
    clickpointX = clickpoint.getX()
    clickpointY = clickpoint.getY()
    point1X = point1.getX()
    point1Y = point1.getY()
    point2X = point2.getX()
    point2Y = point2.getY()
    
    if (clickpointX >=point1X and clickpointX <= point2X) and (clickpointY >=point1Y and clickpointY <= point2Y):
        flag = True
    return flag
        

def playagain(win):

    '''
    Purpose:  ask the user if they want to play again, get their
    Yes or No response, validated by ignoring any clicks
    anywhere on the screen except in the Yes and No boxes
    Pre-conditions:   the graphics window
    Post-conditions:  a bool value, True means the user chose Yes,
    False otherwise
    '''
    
    play_txt = Text(Point(400, 100), "Do you wanna play another game?")
    play_txt.draw(win)
    
    yes_box = Rectangle(Point(100,400), Point(200,550))
    yes_box.draw(win)
    
    no_box = Rectangle(Point(600,400), Point(700,550))
    no_box.draw(win)
    
    yes_txt = Text(Point(150, 475), "Yes?")
    yes_txt.draw(win)
    
    no_txt = Text(Point(650, 475), "No?")
    no_txt.draw(win)
    
    response = win.getMouse()
    
    while (in_box(Point(100,400), Point(200,550), response) == False) and (in_box(Point(600,400), Point(700,550), response) == False):
        error = Text(Point(400, 175), "That is not a valid response")
        error.draw(win)
        response = win.getMouse()
        error.undraw()
        
    play_txt.undraw()
    
    if (in_box(Point(100,400), Point(200,550), response)):
        yes_box.undraw()
        no_box.undraw()
        yes_txt.undraw()
        no_txt.undraw()
        return True
    
    else:
        yes_box.undraw()
        no_box.undraw()
        yes_txt.undraw()
        no_txt.undraw()        
        return False
    
def main():
    win = GraphWin('Chuck-a-Luck', 800,800)
    playagain_flag = True
    pot = 100
    chuckaluck = Text(Point(400,50), 'Chuck-a-Luck!')
    chuckaluck.draw(win)
    
    while (playagain_flag) and (pot >0):
        bet = getbet(pot,win)
        user_roll = getnumber(win)
        
        roll1 = randrange(1,7)
        roll2 = randrange(1,7)
        roll3 = randrange(1,7)
        
        die1 = draw_dice(100,175,roll1,win)
        die2 = draw_dice(400,175,roll2,win)
        die3 = draw_dice(700,175,roll3,win)
        
    
        matches = check_matches(roll1,roll2,roll3, user_roll)
        
        matches_str = "You had " + str(matches) + " matches."
        matches_txt = Text(Point(400,700), matches_str)
        matches_txt.draw(win)
        
        winnings = 0
        if matches == 1:
            winnings = bet
            
        elif matches == 2:
            winnings = bet * 5
        
        elif matches == 3:
            winnings = bet * 10
        else:
            winnings = -bet
            
        pot = pot + winnings
        if winnings >0:
            feedback = "You won " + str(winnings) + "$"
        else:
            feedback = "You lost " + str(bet)
            
        feedback_txt = Text(Point(400, 755), feedback)   
        feedback_txt.draw(win)
        num_pot = "The pot is now " + str(pot) + "$"
        pot_txt = Text(Point(400, 775), num_pot)
        pot_txt.draw(win)
        win.getMouse()
        
        die1.undraw()
        die2.undraw()
        die3.undraw()    
        
        pot_txt.undraw()
        feedback_txt.undraw()  
        matches_txt.undraw()
        
        if pot > 0:
            playagain_flag = playagain(win)
        else: 
            playagain_flag = False
        pot_txt.undraw()
        feedback_txt.undraw()
        
        
    if pot >0:
        results = "You left with " + str(pot) +"$"
    else:
        results = "You lost!"
        
    results_txt = Text(Point(400,400), results)
    results_txt.draw(win)
    
    win.getMouse()
    win.close()

        
        
main()
