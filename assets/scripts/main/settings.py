from pygame.sprite import Group
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
		# Reprodução de sons
		self.estado_som = True
		# Levels
		self.stage = 0
		# Grupos de imagens
		self.bullets = Group()
		self.zombies = Group()
		self.drops = Group()
		# Moedas coletadas
		self.drops_collected = 0
		# Configurações dos projéteis
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 150
		self.bullet_speed_factor = 4
		self.bullets_allowed = 3
		# Configurações da espaçonave
		self.player_speed_factor = 3
		self.player_lifes = 10
		# Configurações dos zombies
		self.zombie_speed_factor = 2
		self.zombies_allowed = 5
		# zombies mortos
		self.count = 0
		# Botões
		buttons = [
			[screen_width * 0.85, screen_height * 0.05, "Instructions"],
			[screen_width * 0.85, screen_height * 0.15, "Sound"],
			[screen_width * 0.4, screen_height * 0.69, "Yes"],
			[screen_width * 0.53, screen_height * 0.69, "No"],
			[20, screen_height * 0.3, "Pause"],
			[20, screen_height * 0.2, "Quit"],
		]

		for button in buttons:
			# Set default color (black)
			button.append(160)  # Width attribute
			button.append(40)   # Height attribute
			if button[2] == "Quit": button.append((255, 0, 0))  # Red color for "Quit" button
			else: button.append((0, 0, 0))  # Black color for other buttons
			button.append(button.pop(2))  # Move label to the end of the button sublist
		
		self.game_buttons = [buttons[0], buttons[4], buttons[5], buttons[1]]
		self.quit_buttons = [buttons[4], buttons[5], buttons[2], buttons[3]]

		# Loop
		self.pause = False
		self.rodando = True

	def restart(self):
		# Resetar:
		# Game
		self.bg_color = (100, 100, 100)
		self.stage = self.count = self.drops_collected = 0
		# Bala
		self.bullets_allowed = self.bullet_speed_factor = self.player_speed_factor = 3
		# Zumbi
		self.zombie_speed_factor = 2
		self.zombies_allowed = 5
		# Player
		self.player_lifes = 10

		