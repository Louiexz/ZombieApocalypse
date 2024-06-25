import os
import pygame as pyg
from pygame.sprite import Sprite
from random import randint

class Zombie(Sprite):
    """Representa um zumbi"""
    def __init__(self):
        super().__init__()
        self.zombie_image = Zombie.get_random_zombies()
        self.image = pyg.image.load('./assets/imagens/enemies/idle/' + self.zombie_image)
        self.rect = self.image.get_rect()

        self.zombie_life = 1

        # Store the zombie's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # Direção do zombie
        self.fleet_direction_x = 1
        self.fleet_direction_y = 1
    
    @staticmethod
    def get_random_zombies():
        # Gera um índice aleatório usando os.urandom
        archives = os.listdir('./assets/imagens/enemies/idle')
        random = int.from_bytes(os.urandom(4), byteorder='big') % len(archives)
    
        return archives[random]
    
    def spawn(self, settings):
        # Start each new zombie in the screen.
        self.rect.centerx = randint(10, settings.screen_width - 10)
        self.rect.bottom = randint(10, settings.screen_height - 10)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self, screen):
        if not 0 <= self.rect.left <= screen.get_rect().right: self.fleet_direction_x *= -1
        if not 0 <= self.rect.bottom <= screen.get_rect().top: self.fleet_direction_y *= -1
        
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
