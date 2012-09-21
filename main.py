import sprites,levels
import gameEngine
import pygame,sys,ConfigParser

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

#Main menu
import sys, pygame, random
import gameEngine
from menu import *
def main(screen):
    print "main menu loaded"
    menu = cMenu(50, 50, 20, 5, 'vertical', 100, screen,
               [('Start Game', 1, None),
                ('Load Game',  2, None),
                ('Options',    3, None),
                ('Exit',       4, None)])
    menu.set_center(True, True)
    menu.set_alignment('center', 'center')
    state = 0
    prev_state = 1
    rect_list = []
    #pygame.event.set_blocked(pygame.MOUSEMOTION)

    while True:
        if prev_state != state:
            pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key = 0))
            prev_state = state

        e = pygame.event.wait()
        if e.type == pygame.KEYDOWN or e.type == EVENT_CHANGE_STATE:
            if state == 0:
                rect_list, state = menu.update(e, state)
            elif state == 1:
                print 'Start Game!'
                gameEngine.gameInit()
                state = 0
            elif state == 2:
                print 'Load Game!'
                state = 0
            elif state == 3:
                print 'Options!'
                state = 0
            else:
                print 'Exit!'
                pygame.quit()
                sys.exit()
        if e.type == pygame.QUIT:
            print 'test'
            pygame.quit()
            sys.exit()

        pygame.display.update(rect_list)

#---- Call Main Menu ------#
if __name__ == "__main__":
    main(screen)