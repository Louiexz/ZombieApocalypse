import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""Uma classe que administra projéteis disparados pela espaçonave"""
	def __init__(self, settings, screen, player):
		"""Cria um objeto para o projétil na posição atual da espaçonave."""
		super().__init__()
		self.screen = screen
		self.player = player
		# Cria um retângulo para o projétil em (0, 0) e, em seguida, define a # posição correta
		self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
		self.rect.centerx = player.rect.centerx
		self.rect.top = player.rect.top

		# Armazena a posição do projétil como um valor decimal
		self.y = float(self.rect.y)
		self.x = float(self.rect.x)
		self.color = settings.bullet_color
		self.speed_factor = settings.bullet_speed_factor
		
	def update(self):
		"""Move o projétil pela tela."""
		# Atualiza a posição decimal do projétil
		if self.player.image == self.player.image_up: self.y -= self.speed_factor
		elif self.player.image == self.player.image_left: self.x -= self.speed_factor
		elif self.player.image == self.player.image_right: self.x += self.speed_factor
		else: self.y += self.speed_factor
		# Atualiza a posição de rect
		self.rect.y = self.y
		self.rect.x = self.x
		
	def draw_bullet(self):
		"""Desenha o projétil na tela."""
		pygame.draw.rect(self.screen, self.color, self.rect)