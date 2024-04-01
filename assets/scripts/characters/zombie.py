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
        self.rect.centerx = randint(10, int(settings.screen_width))
        self.rect.bottom = randint(10, int(settings.screen_height))
        # Store the zombie's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # Direção do zombie
        self.fleet_direction_x = 1
        self.fleet_direction_y = 1
        
    def check_edges(self, screen):
        if self.rect.right >= screen.get_rect().right: self.fleet_direction_x *= -1
        elif self.rect.left <= 0: self.fleet_direction_x *= -1
        if self.rect.top >= screen.get_rect().top: self.fleet_direction_y *= -1
        elif self.rect.bottom <= 0: self.fleet_direction_y *= -1
        return False

    def update(self, settings):
        self.x += (settings.zombie_speed_factor *  self.fleet_direction_x)
        self.rect.x = int(self.x)

        self.y += (settings.zombie_speed_factor *  self.fleet_direction_y)
        self.rect.y = int(self.y)
