import math
import pygame as pyg
from pygame.sprite import Sprite

class Player(Sprite):
	def __init__(self, screen, ai_sets=''):
		"""Inicializa o personagem e define sua posição inicial."""
		self.screen = screen
		self.ai_sets = ai_sets
		# Carrega a imagem do personagem e obtém seu rect
		path = "./assets/imagens/player/idle_"
		self.image_up = pyg.image.load(f"{path}up_40x40.png").convert_alpha()
		self.image_down = pyg.image.load(f"{path}down_40x40.png").convert_alpha()
		self.image_left = pyg.image.load(f"{path}left_40x40.png").convert_alpha()
		self.image_right = pyg.image.load(f"{path}right_40x40.png").convert_alpha()
		self.image = self.image_down  # Comece olhando para baixo
		self.rect = self.image.get_rect()
		self.rect.center = (ai_sets.screen_width // 2, ai_sets.screen_height // 2)  # Define a posição inicial do personagem
		# Inicia cada novo personagem no centro da tela
		self.rect.centerx = self.rect.center[0]
		# Armazena um valor decimal para o centro do personagem
		self.center = float(self.rect.centerx)
		self.bottom = float(self.rect.bottom)
		# Flags de movimento
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
	
	def blitme(self):
		"""Desenha o personagem em sua posição atual."""
		self.screen.blit(self.image, self.rect)

	def update_image(self):
		mouse_pos = pyg.mouse.get_pos()
		"""Atualiza a posição do personagem de acordo com as flags de movimento."""
		# Atualiza o valor do centro do personagem, e não o retângulo

		dx = mouse_pos[0] - self.rect.centerx
		dy = mouse_pos[1] - self.rect.centery
		angle = math.degrees(math.atan2(dy, dx))

		# Atualiza o sprite do jogador com base na direção
		if -45 < angle <= 45: self.image = self.image_right
		elif 45 < angle <= 135: self.image = self.image_down
		elif 135 < angle <= 180 or -180 <= angle <= -135: self.image = self.image_left
		else: self.image = self.image_up
	
	def update_state(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.ai_sets.player_speed_factor
		elif self.moving_left and self.rect.left > 0:
			self.centerx -= self.ai_sets.player_speed_factor
		elif self.moving_up and self.rect.top > 0:
			self.centery -= self.ai_sets.player_speed_factor
		elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.centery += self.ai_sets.player_speed_factor

	def restart(self):
		self.rect.centerx = self.rect.center[0]
