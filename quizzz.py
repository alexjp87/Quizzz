### SETUP

#
#
#

## Modules and Packages

# Import math and random modules
import math
import random

# Import pygame and sys modules
import pygame, sys

# Import tkinter package
import tkinter as tk
# Import messagebox module from tk
from tkinter import messagebox


#-------------------------------------------------------------#

## Classes

# Create cube object using class keyword:
class cube(object):
    # set intial rows to 20
    rows = 20
    # set intial w to 500 pixels
    w = 500
    # Assign paramters for class creation using __init__ function
    def __init__(self, start, dirnx=1, dirny=0, colour=(255,0,0)): # default direction values used so that snake moves automatically without requiring initial input event

    # Define parameters:
    # why self.pos?
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.colour = colour

    # Create move function:
    def move(self, dirnx, dirny):
        # define paramters:
        self.dirnx = dirnx
        self.dirny = dirny
        # set direction?
        self.pos = (self.pos[0] + dirnx, self.pos[1] + dirny)

    # Create draw function:
    def draw(self, surface, eyes=False):
        # set gap size (dis) to width // rows  - WHY? [// (integer divide) = round down to nearest whole number e.g. 7 // 4 = 1, 9 // 4 = 2]
        dis = self.w // self.rows
        # store x and y positions in variables (for ease of typing later)
        i = self.pos[0] # rows (x)
        j = self.pos[1] # columns (y)
        # draw rectangle (snake, or individual cube of snake???), parameters: surface, colour, (x, y, width, height) [draw.rect() draws a rectangle on a given surface (+ 1 pixels x and y and -2 pixels width and height means snake rectangle will be inside grid lines so grid lines remain visible???)]
        pygame.draw.rect(surface, self.colour, (i*dis+1, j*dis+1, dis-2, dis-2))
        # Check if cube has 'eyes' (i.e. is the head cube):
        if eyes:
            # if so, find middle of cube
            centre = dis // 2
            # set 'eye' radius
            radius = 3
            # set 'eye' positions (x,y)
            circleMiddle = (i*dis+centre-radius, j*dis+8)
            circleMiddle2 = (i*dis + dis - radius*2, j*dis+8)
            # draw 'eyes', parameters: surface, colour, centre (of circle), radius (of circle) [draw.circle() draws a circle on a given surface]
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)


# Create snake object using class keyword:
class snake(object):
    # create empty body list
    body = []
    # create empty turns dictionary
    turns = {}
    # Assign paramters for class creation using __init__ function (colour, position)
    def __init__(self, colour, pos):
        # Define parameters:        
        self.colour = colour
        # track position of lead cube object, i.e. snake head
        self.head = cube(pos)
        # and append to snake body list (LINE 45) - want snake cubes ordered in body list so can then manipulate list i.e. manipulate snake
        self.body.append(self.head)
        # track snake direction (if x = 1 or -1, y = 0, and vice versa because snake only moves in one direction at a time i.e. vertical OR horizontal)
        self.dirnx = 0
        self.dirny = 1
    # Create move function:
    def move(self):
        # Listen for input events:
        # check if quit event has occurred (e.g. click x in top right corner of window) [event.get() fetches then removes all input events from event queue]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
            # if so, uninitialise all currently initialised pygame modules, i.e. quit game (***changed <pygame.quit()> to <sys.exit() (imported LINE 14) to avoid error: "pygame.error: video system not initialized"***)
                sys.exit()
            
            # Else:
            # Create a (dictionary?) containing every key on keyboard as keys with booleans as values (True = pressed)
            # Using this method to move snake instead of e.g.<if event.type = key_LEFT> because smoother - e.g. adjusts to multiple key presses at once better than other method - WHY? Something to do with not having to process each event before can listen for next one? ...             
            keys = pygame.key.get_pressed()
            # loop through keys and check if any boolean values = True
            for key in keys:
                # if left key (K_LEFT) value = True, i.e.the left key has been pressed:
                if keys[pygame.K_LEFT]:
                    # x axis direction = -1
                    self.dirnx = -1
                    # y axis direction = 0 (because SEE LINE 56)                    
                    self.dirny = 0
                    # tell every cube in snake body list (SEE LINE 54) to turn in same direction as head when reach same position by appending to turns dictionary LINE 47 (key = head coordinates ([x,y]) at turn event position, value = turn direction (e.g.[0,-1]))
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    # [: index poisiton = slice() all items in a sequence (e.g. dictionary) (makes a copy)]

                # repeat for if right (K_RIGHT), up (K_UP) or down (K_DOWN) values = True:
                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        
        # enumerate() self.body list LINE 55 and loop through indexes (i) and cube objects LINE 27 (c) (for each cube in the snake, before moving check upcoming position to see if in turns list) [enumerate() turns a collection (e.g. list) into an enumerate object using a counter as keys and the collection items as values (e.g. [(0, 'a'), (1, 'b')] or {(0 : 'a'), (1 : 'b')}) ]
        for i, c in enumerate(self.body):
            # declare p variable as cube object position (SEE LINE 53)            
            p = c.pos[:]
            # Check if position exists in self.turns LINE 81
            if p in self.turns:
                # if so, declare turn variable as position ([x,y])
                turn = self.turns[p]
                # move cube object in specified direction?
                c.move(turn[0], turn[1])
                # check if we have reached the last cube object of the self.body list, i.e. the last cube of the snake (because length of list = length of snake, so length of list - 1 = last cube)
                if i == len(self.body)-1:
                    # if so, remove the position from self.turns (so snake doesn't try to turn every time hits that position) [.pop() removes an element from a specified position in a sequence e.g. list]
                    self.turns.pop(p)
            # Else:       
            else:
                # Check if snake has reached left edge of grid (i.e. if moving left (dirnx == -1) and x axis value of position is <= 0, i.e. further than the left boundary of the grid (top left corner = [0,0]))
                if c.dirnx == -1 and c.pos[0] <= 0:
                    # if so, set x axis position to right side of grid and keep y axis position the same (rows = 20 (LINE 208), so c.rows - 1 = 19, i.e. right edge position of grid)
                    c.pos = (c.rows - 1, c.pos[1])
                # repeat check for if snake has reached right, bottom or top grid edge and re-assign positions as appropriate:
                elif c.dirnx == 1 and c.pos[0] >= c.rows - 1: # right edge
                    c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows - 1: # bottom edge
                    c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0: # top edge
                    c.pos = (c.pos[0], c.rows - 1)
                
                # Else (if snake isn't turning and hasn't reached an edge):
                else:
                    # continue moving in the cube object's current direction
                    c.move(c.dirnx, c.dirny)

    # Create reset function:
    def reset(self, pos):
        # reset length, position and direction of snake (SEE snake class LINES 74-87)
        self.body = []
        self.turns = {}
        self.head= cube(pos)
        self.body.append(self.head)
        self.dirnx = 0 
        self.dirny = 1 

    # Create addCube function:
    def addCube(self):
        # find end of snake (last item in body list)
        tail = self.body[-1]
        # find direction values for x and y axes (-1, 0 or 1)
        dx, dy = tail.dirnx, tail.dirny
        # check if snake tail is moving right
        if dx == 1 and dy == 0:
            # if so, append new cube to the left side of the tail (x position - 1)           
            self.body.append(cube((tail.pos[0] - 1, tail.pos[1])))
        # repeat check for if snake tail is moving left, down or up and append new cube to appropriate position:
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0] + 1, tail.pos[1]))) # direction left: append x + 1
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0], tail.pos[1] - 1))) # direction down: append y - 1
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0], tail.pos[1] + 1))) # direction up: append y + 1
        # set direction for appended cube (same as tail cube)
        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy


    # Create draw function:
    def draw(self, surface):
        # loop through indexes (i) and cube objects (c) in enumerated self.body list (LINE 55) (i.e. loop through snake)
        for i, c in enumerate(self.body):
            # check if current cube object is the head (i.e. leading cube)
            if i == 0:
                # if so, draw cube with 'eyes' (LINE 39) (so user knows which end of snake is the front)
                c.draw(surface, True)
            # else:
            else:
                # draw cube without 'eyes' (default 'eyes' value is False LINE 47)
                c.draw(surface)


#-------------------------------------------------------------#

## Functions

# Create drawGrid function:
def drawGrid(w, rows, surface):
    # set gap size (gapBtwn) to width // rows  - WHY? [// (integer divide) = round down to nearest whole number e.g. 7 // 4 = 1, 9 // 4 = 2]
    gapBtwn = w // rows
    # declare initial x and y axis variables with value 0
    x = 0
    y = 0
    # loop through number of rows (20):
    for row in range(rows):
        # redeclare x and y axis variables
        x = x + gapBtwn
        y = y + gapBtwn
        # draw grid lines using pygame draw module [draw.line() draws a straight line, takes 4 arguments: surface, colour, start position, end position] - UNDERSTAND START AND END POSITION VALUES??
        pygame.draw.line(surface, (255,255,255), (x,0), (x, w)) # vertical lines
        pygame.draw.line(surface, (255,255,255), (0,y), (w, y)) # horizontal lines      

# Create redrawWindow function:
def redrawWindow(surface):
    # make width, rows, s and snack variables global
    global width, rows, s, snack
    # set (fullscreen mode?) + black background [surface.fill() fills display with colour (no position argument = whole display filled)]
    surface.fill((0,0,0))
    # draw snake using draw function LINE ?
    s.draw(surface)
    # draw snack
    snack.draw(surface)
    # call drawGrid() function
    drawGrid(width, rows, surface)
    # update window using pygame display module [display.update() updates a portion of a software display, value given as argument (no argument = update entire display)]
    pygame.display.update()

# Create randomSnack function:
def randomSnack(rows, item): # <item> parameter = snake object
    # make copy of snake cube objects list (LINE 85)
    positions = item.body
    # Create infinite loop to randomise 'snack' grid position:
    while True:
        # pick random x and y co-ordinates between 0 and 20 [random.randrange() returns a randomly selected element from a specified range (only one value in range defaults to stop value)(rows = 20, LINE 29)]
        x = random.randrange(rows)
        y = random.randrange(rows)
        # check if the randomised position (x,y) is currently occupied by a snake cube object [filter(<function>,<iterable>) returns an iterable that is run through a function which tests items against a condition] [lambda denotes an anonymous funtion]
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            # if so, loop again (i.e. re-randomise co-ordinates)
            continue
        # else:
        else:
            # break loop
            break
    # and return randomised snack position
    return (x,y)

# Create message_box function:
def message_box(subject, content):
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


## Create game function
def game():
    ## Create game grid:
    # make width, rows, s and snack variables global
    global width, rows, s, snack
    # set initial width to 500 (height not needed because creating square grid (20 rows x 20 columns, 500px width x 500px height))
    width = 500
    # set initial rows to 20 (needs to divide by height)
    rows = 20
    # create game grid using pygame display module [display.set_mode() creates a display surface (i.e. initialises a window or screen for display)]
    win = pygame.display.set_mode((width, width))
    # create snake using snake class LINE 73 (colour (red), position (row 10 column 10))
    s = snake((255,0,0), (10,10))
    # create random snack (LINE 213) using cube class (LINE 27)
    snack = cube(randomSnack(rows, s), colour=(0,255,0))
    # declare flag as True
    flag = True
    # Create Clock object using pygame time module [time.Clock() creates an object for tracking time]
    clock = pygame.time.Clock()

    
    ## Loop:
    
    # Create infinite loop:
    while flag:
        # Define game speed:
        # pause programme for 0.05 seconds (per frame?) to reduce game speed (works in conjuntion with clock.tick()) (lower value = higher game speed because less delay) [time.delay() pauses programme for number of milliseconds given as argument]
        pygame.time.delay(50)
        # prevent game from running at > 10 frames per second - means snake can move max 10 squares per second? (lower value = lower game speed because less frames per second) ['tick' argument = framerate per second, value in milliseconds]
        clock.tick(10)

        # Call move function (LINE 89?)
        s.move()

        # Check if head snake cube has hit snack poisiton:
        if s.body[0].pos == snack.pos:
            # increase snake object length by 1 using addCube function LINE 162
            s.addCube()
            # create new random snack
            snack = cube(randomSnack(rows, s), colour=(0,255,0))
        # Check for snake colliding with self:
        for x in range(len(s.body)):
            # check if the position (x,y) of any snake body cube object is currently occupied by another snake cube object, i.e. snake has collided with itself [filter(<function>,<iterable>) returns an iterable that is run through a function which tests items against a condition] [lambda denotes an anonymous funtion]
            if s.body[x].pos in list(map(lambda z:z.pos, s.body[x+1:])):
                # if so, print message to console (score = length of snake)
                print('Score: ', len(s.body))
                # display message box using message_box() function LINE 253 - ???
                message_box('You lost!', 'Play again...')
                # reset snake to start position (middle of grid) using reset function LINE 158
                s.reset((10,10))
                # break loop
                break

        # redraw window (LINE 202) surface (win variable LINE 241):
        redrawWindow(win)

    
#-------------------------------------------------------------#

## Call game()
game()





"""
- Add condition so can't turn back on self? e.g. if moving left can only turn up or down not right, or if moving up can only move left or right not down

"""