import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""Uma classe que administra projéteis disparados pela espaçonave"""
	def __init__(self, sets, screen, player):
		"""Cria um objeto para o projétil na posição atual da espaçonave."""
		super().__init__()
		self.screen = screen
		# Cria um retângulo para o projétil em (0, 0) e, em seguida, define a # posição correta
		self.rect = pygame.Rect(0, 0, sets.bullet_width, sets.bullet_height)
		self.rect.centerx = player.rect.centerx

		if player.image == player.image_up: self.rect.top = player.rect.top
		elif player.image == player.image_left: self.rect.top = player.rect.left
		elif player.image == player.image_right: self.rect.top = player.rect.right
		else: self.rect.top = player.rect.bottom

		# Armazena a posição do projétil como um valor decimal
		self.y = float(self.rect.y)
		self.color = sets.bullet_color
		self.speed_factor = sets.bullet_speed_factor
		
	def update(self):
		"""Move o projétil para cima na tela."""
		# Atualiza a posição decimal do projétil
		self.y -= self.speed_factor
		# Atualiza a posição de rect
		self.rect.y = self.y
		
	def draw_bullet(self):
		"""Desenha o projétil na tela."""
		pygame.draw.rect(self.screen, self.color, self.rect)