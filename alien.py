#a class for Aliens
import pygame
from pygame.sprite import Sprite
class Aliens(Sprite):
	def __init__(self, ai_settings,screen):
		super(Aliens, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		#load in alien image
		self.image = pygame.image.load('X Wing.bmp')
		self.rect = self.image.get_rect()

		#start alien in lhs
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#store alien in an exact position
		self.x = float(self.rect.x)

		#draw the alien
	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def update(self):
		self.x += (self.ai_settings.alien_speed * self.ai_settings.fleet_direction)
		self.rect.x = self.x
	
	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True