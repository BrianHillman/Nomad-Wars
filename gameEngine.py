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
	probe=0
	running=True
	e = pygame.event.wait()
	while (running):
		
		#Print Level
		printGame()

		#Check for User Input
		print (getMouseDirection(2,3))
		pygame.display.update()
		fpsClock.tick(30)

		#Update Game
		updateGame()

#--- Takes character,map,network, etc objects and updates the game
def printGame():
	print "Print Game Now"
	pygame.display.update()
def updateGame():
	print "Update Game Now"

#--- Returns the direction in degrees from player coordinates to mouse coordinates
def getMouseDirection(pX,pY):
	mX,mY=0
	print pygame.mouse.get_pos()
	#mX,mY=pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type==MOUSEMOTION:
			mX,mY=event.pos
	return math.atan((mY - pY)/(mX - pX))
