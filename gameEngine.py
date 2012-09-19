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


#----------------------
pygame.init()
player = sprites.playerCharacter()
allsprites = pygame.sprite.LayeredDirty(player)
screen.blit(background, (0, 0))
rects = allsprites.draw(screen)
pygame.display.update(rects)
allsprites.clear(screen, background)

