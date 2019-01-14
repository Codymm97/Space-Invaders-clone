#settings
class Settings:

	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		#ship settings
		self.ship_speed = 1.5
		self.ship_limit = 3

		#bullet settings
		self.bullet_speed = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 50,205,50
		self.bullets_allowed = 5

		#alien settings
		self.alien_speed = 1
		self.fleet_drop = 10
		self.fleet_direction = 1
		self.alien_points = 50

		#game speeds up
		self.speedup_scale = 1.1
		self.score_scale = 1.5
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		self.ship_speed = 1.5
		self.bullet_speed = 3
		self.alien_speed = 1
		self.fleet_direction = 1
	
	def increase_speed(self):
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
		print(self.alien_points)