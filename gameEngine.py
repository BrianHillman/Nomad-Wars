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


		#Check for User Input


		#Update Game
		running=False
		pygame.quit()
		sys.exit()