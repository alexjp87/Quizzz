### SETUP

#
#
#

## Import Modules and Packages

# Import 'math' and 'random' modules
import math
import random

# Import 'pygame' module
import pygame

# Import 'tkinter' package
import tkinter as tk
# Import 'messagebox' module from tk
from tkinter import messagebox


#-------------------------------------------------------------#

## Create Classes

# Create cube object using class keyword:
class cube(object):
# set intial rows to 0
    rows = 0
# set intial w to 0
    w = 0
# assign paramters for class creation using __init__ function (placeholder)
    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        pass
# create move function (placeholder)
    def move(self):
        pass
# create draw function (placeholder)
    def draw(self, surface, eyes=False):
        pass

# Create snake object using class keyword:
class snake():
# create empty body list
    body = []
# create empty turns dictionary
    turns = {}
# Assign paramters for class creation using __init__ function (colour, position)
    def __init__(self, col, pos):
# Define parameters:        
        self.col = col
# track position of snake head - HOW?
        self.head = cube(pos)
# and append to snake body list (LINE 45) - want snake cubes ordered in body list so can then manipulate list i.e. manipulate snake
        self.body.append(self.head)
# track snake direction (if x = 1 or -1, y = 0, and vice versa because snake only moves in one direction at a time i.e. vertical OR horizontal)
        self.dirnx = 0
        self.dirny = 1
# Create snake move function:
    def move(self):
    # Listen for input events:
    # check if quit event has occurred (e.g. click x in top right corner of window) [event.get() fetches then removes all input events from event queue]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
        # if so, uninitialise all currently initialised pygame modules, i.e. quit game
                pygame.quit()
# Else:
# Create a (dictionary?) containing every key on keyboard as keys with booleans as values (True = pressed)
    # Using this method to move snake instead of e.g.<if event.type = key_LEFT> because smoother - adjusts to multiple key presses at once better than other method - WHY? Something to do with not having to process each event before can listen for next one? ...             
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
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny] # [: index poisiton = slice() all items in dictionary]

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

# Create reset function (placeholder)
    def reset(self, pos):
        pass
# Create addCube function (placeholder)
    def addCube(self):
        pass
# Create draw function (placeholder)
    def draw(self, surface):
        pass


#-------------------------------------------------------------#

## Create Functions

# Create drawGrid function:
def drawGrid(w, rows, surface):
# set gap size to width // rows  - WHY? (integer divide = nearest whole number e.g. 7 // 4 = 1, 9 // 4 = 2)
    gapBtwn = w // rows
# declare initial x and y axis variables with value 0
    x = 0
    y = 0
# loop through number of rows (20):
    for row in range(rows):
# redeclare x and y axis variables
        x = x + gapBtwn
        y = y + gapBtwn
# draw grid lines using pygame draw module [draw.line() draws a straight line, taking 4 arguments: surface, colour, start position, end position] - UNDERSTAND START AND END POSITION VALUES??
# vertical
        pygame.draw.line(surface, (255,255,255), (x,0), (x, w))
# horizontal       
        pygame.draw.line(surface, (255,255,255), (0,y), (w, y))


# Create redrawWindow function:
def redrawWindow(surface):
# make width and rows variables global
    global width, rows
# set fullscreen mode + black background [Surface.fill() fills display with colour - no argument = whole display filled]
    surface.fill((0,0,0))
# call drawGrid() function
    drawGrid(width, rows, surface)
# update window using pygame display module [display.update() updates a portion of a software display, value given as argument (no argument = update entire display)]
    pygame.display.update()

# Create randomCube function (placeholder)
def randomCube(rows, items):
    pass

# Create message_box function (placeholder)
def message_box(subject, contact):
    pass


#-------------------------------------------------------------#



### GAME

#
#
#

## Create game function (placeholder)
def game():
## Create game grid:
# make width and rows variables global
    global width, rows
# set initial width to 500
    width = 500
# set initial height to 500
    height = 500
# set initial rows to 20 (needs to divide by height)
    rows = 20
# create game grid using pygame display module
    win = pygame.display.set_mode((width, height))
# create snake - takes colour and position arguments: red and position (position is the middle because rows set to 20?)
    s = snake((255,0,0), (10,10))

# Create Clock object using pygame time module [].Clock() creates an object for tracking time]
    clock = pygame.time.Clock()

# Create flag variable - WHY?
    flag = True


## Loop:
# Declare while loop condition as flag = True? WHY?
    while flag:

# Define game speed:
# prevent game from running at > 10 frames per second - means snake can move max 10 squares per second? (lower value = lower game speed because less frames per second) ['tick' argument = framerate per second, value in milliseconds]
        clock.tick(10)
# pause programme for 0.5 seconds to further reduce game speed - works in conjuntion with clock.tick() (lower value = higher game speed because less delay) [time.delay() pauses programme for number of milliseconds given as argument]
        pygame.time.delay(50)

# set redrawWindow surface to win variable (LINE 170):
        redrawWindow(win)

