import sprites,levels
import pygame,sys,ConfigParser
from pygame.locals import *   #constants defined here
from pygame.compat import geterror

#----------------Initialize Game ------------------------------#
def gameInit():
	
	#Load Stuff
	print "Loading..."

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


		#Update Game
		updateGame()

		#Exit
		print "Exit Now"
		running=False
		sys.exit()
		pygame.quit()

#--- Takes character,map,network, etc objects and updates the game
def printGame():
	print "Print Game Now"

def updateGame():
	print "Update Game Now"

#--- Returns the direction in degrees from player coordinates to mouse coordinates
def getMouseDirection(pX,pY)
	mX,mY=pygame.mouse.get_pos()
