#Time to make aliens
import sys
import pygame
#grabs the ship
from ship import Ship
#gets custom settings from the user
from settings import Settings
#get game events
import game_func as ga
from pygame.sprite import Group
from alien import Aliens
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
	#creates a screen for the player
	pygame.init()

	#creats an object of the settings calss imported
	ai_settings = Settings()

	#takes those values and puts it in play
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien invasion")

	play_button = Button(ai_settings, screen, "Play")

	#make ship
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)

	ga.create_fleet(ai_settings,screen,ship,aliens)
	#game loop 
	while True:
		#gets user input from keyboard and mouse
		"""may have put sb somehwer i shouldnt have"""
		ga.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
		if stats.game_active:
			ship.update()
			ga.update_bullet(ai_settings,screen,stats,sb,ship,aliens,bullets)
			ga.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
		ga.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
		#print(len(bullets))
run_game()