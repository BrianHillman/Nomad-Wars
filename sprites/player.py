import pygame
class playerCharacter(pygame.sprite.DirtySprite):
	dirty = 1
	def __init__(self):
		pygame.sprite.DirtySprite.__init__(self)
	def update(self):
#players are always in motion ( idle animation or movement / attacking etc) so we make them permanently dirty
		self.dirty = 1
