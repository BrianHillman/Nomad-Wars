import sprites,levels
import pygame,sys,ConfigParser,math
import math
import time

from pygame.locals import *   #constants defined here
from pygame.compat import geterror
fpsClock=pygame.time.Clock()

#----------------Initialize Game ------------------------------#
def gameInit():
    
    #Load Stuff
    print "Loading..."
    #pygame.event.set_allowed(pygame.MOUSEMOTION)

    #Clear Menu Objects


    #Run game loop once done loading
    gameLoop()

#-----------------------Main loop------------------------------#
def gameLoop():
    running=True
    e = pygame.event.wait()
    while (running):
        
        #Print Level
        printGame()

        #Check for User Input
        getMouseDirection(500,500)
        pygame.display.update()
        fpsClock.tick(2)

        #Update Game


#--- Takes character,map,network, etc objects and updates the game
def printGame():
    pygame.display.update()

def updateGame():
    a=0

#--- Returns the direction in degrees from player coordinates to mouse coordinates
def getMouseDirection(pX,pY):
    mX,mY,angle=0.0,0.0,0.0
    print pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==MOUSEMOTION:
            mX,mY=event.pos
    if mX>0:
        angle=math.degrees(math.atan(abs(float(mY-pY))/abs(float(mX-pX))))
    print angle
    print "-------------"