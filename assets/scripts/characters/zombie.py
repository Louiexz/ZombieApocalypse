import pygame as pyg
from pygame.sprite import Sprite
from random import randint

class Zombie(pyg.sprite.Sprite):
    """Representa um zumbi"""
    def __init__(self, image, settings):
        super().__init__()
        self.zombie_image = image
        self.image = pyg.image.load('./assets/imagens/enemies/idle/' + image)
        self.rect = self.image.get_rect()
        # Start each new zombie near the top left of the screen.
        self.rect.centerx = randint(10, int(settings.screen_width) - 10)  # Garante que o zumbi não fique muito próximo das bordas
        self.rect.bottom = randint(10, int(settings.screen_height) - 10)  # Garante que o zumbi não fique muito próximo das bordas
        # Store the zombie's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # Direção do zombie
        self.fleet_direction_x = 1
        self.fleet_direction_y = 1
        
    def check_edges(self, screen):
        if not 0 <= self.rect.left <= screen.get_rect().right:
            self.fleet_direction_x *= -1
        if not 0 <= self.rect.bottom <= screen.get_rect().top:
            self.fleet_direction_y *= -1

        
    def check_player(self, player):
        if player.rect.centerx < self.rect.centerx: self.fleet_direction_x = -1
        elif player.rect.centerx > self.rect.centerx: self.fleet_direction_x = 1
        if player.rect.centery < self.rect.centery: self.fleet_direction_y = -1
        elif player.rect.centery > self.rect.centery: self.fleet_direction_y = 1

    def update(self, settings):
        self.x += (settings.zombie_speed_factor *  self.fleet_direction_x)
        self.rect.x = int(self.x)

        self.y += (settings.zombie_speed_factor *  self.fleet_direction_y)
        self.rect.y = int(self.y)
