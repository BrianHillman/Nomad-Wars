import sprites,menus,levels
import pygame,sys,ConfigParser
from pygame.locals import *   #constants defined here
from pygame.compat import geterror

if not pygame.font:
    print ('Warning, fonts disabled')
if not pygame.mixer:
    print ('Warning, sound disabled')

#----------------------Read in config file------------------------
parser = ConfigParser.SafeConfigParser()
parser.read('config')

fpsCap = parser.get('video', 'fpsCap')


#---------------------- Set Window Settings ----------------------
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Nomad Wars - By Grant G. and Brian H.")

#-----------------------Main loop------------------------------#