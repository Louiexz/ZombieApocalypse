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
		self.rect.centery = self.rect.center[1]
		# Armazena um valor decimal para o centro do personagem
		self.center = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		self.bottom = float(self.rect.bottom)
		# Flags de movimento
		self.keys = [False] * 4 # 0 = direita, 1 - esquerda, 2 - cima, 3 - baixo
		self.value = 3# Direção da imagem do personagem
	
	def blitme(self):
		"""Desenha o personagem em sua posição atual."""
		self.screen.blit(self.image, self.rect)

	def update_image(self):
		if self.value == 0: self.image = self.image_right
		elif self.value == 1: self.image = self.image_left
		elif self.value == 2: self.image = self.image_up
		else: self.image = self.image_down

	def get_mouse_pos(self):
		mouse_pos = pyg.mouse.get_pos()
		"""Atualiza a posição do personagem de acordo com as flags de movimento."""
		dx = mouse_pos[0] - self.rect.centerx
		dy = mouse_pos[1] - self.rect.centery
		angle = math.degrees(math.atan2(-dy, dx))

		# Atualiza o sprite do jogador com base na direção do mouse
		if -45 < angle <= 45: self.value = 0
		elif 135 < angle <= 225: self.value = 1
		elif 45 < angle <= 135: self.value = 2
		else: self.value = 3

		self.update_image()
	
	def update_state(self, screen):
		"""Atualiza o movimento do personagem."""
		speed = self.ai_sets.player_speed_factor

		if self.keys[0] and self.rect.right < screen.get_rect().right:
			self.center += speed
		elif self.keys[1] and self.rect.left > 0: self.center -= speed

		if self.keys[2] and self.rect.top > 0: self.centery -= speed
		elif self.keys[3] and self.bottom < screen.get_rect().bottom:
			self.centery += speed
		
		self.rect.centerx = self.center
		self.rect.centery = self.centery

	def restart(self):
		"""Reinicia as configurações do personagem."""
		self.rect.center = (self.ai_sets.screen_width // 2, self.ai_sets.screen_height // 2)
		self.rect.centerx = self.rect.center[0]
		self.rect.centery = self.rect.center[1]
