class Settings():
	"""Uma classe para armazenar todas as configurações da Invasão
	zombie."""
	def __init__(self, screen_width, screen_height, screen):
		# Configurações da tela
		self.screen = screen
		self.screen_width = screen_width
		self.screen_height = screen_height
		# Background
		self.bg_color = (100, 100, 100)
		self.ruina = (250, 75, 0)
		self.terra = (150, 75, 0)
		# Levels
		self.stage = 0
		# Configurações dos projéteis
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 150
		self.bullet_speed_factor = 4
		self.bullets_allowed = 3
		# Configurações da espaçonave
		self.player_speed_factor = 3
		self.player_lifes = 3
		# Configurações dos zombies
		self.zombie_speed_factor = 2
		self.zombies_allowed = 5
		# zombies mortos
		self.count = 0
		# Botões
		button1_rect = [screen_width * 0.75, screen_height * 0.05, 160, 40, (0, 0, 0), "Instructions"]
		button2_rect = [20, screen_height * 0.2, 140, 40, (255, 0, 0), "Quit"]
		button3_rect = [20, screen_height * 0.25, 140, 40, (0, 0, 0), "Stop/Rerun"]

		self.buttons = [button1_rect, button2_rect, button3_rect]
		# Loop
		self.pause = False
		self.rodando = True

	def restart(self):
		# Resetar:
		# Game
		self.bg_color = (100, 100, 100)
		self.stage = self.count = 0
		# Bala
		self.bullets_allowed = self.bullet_speed_factor = 3
		# Zumbi
		self.zombie_speed_factor = 2
		self.zombies_allowed = 5
		# Player
		self.player_speed_factor = self.player_lifes = 3
		