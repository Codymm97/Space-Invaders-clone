#ship module
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	
	def __init__(self, ai_settings, screen):
		super(Ship, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
	
		#load in ship
		self.image = pygame.image.load('tieintercepter.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#start the ship at the bottom center
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#store the value for the ships center
		self.center = float(self.rect.centerx)

		#movement flags
		self.moving_right = False
		self.moving_left = False

	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed
		self.rect.centerx = self.center

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def center_ship(self, ship):
		self.center = self.screen_rect.centerx