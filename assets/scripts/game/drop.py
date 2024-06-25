import pygame
from random import randint
from pygame.sprite import Sprite

class Drop(Sprite):
    """Representa um item dropado"""
    def __init__(self, settings):
        super().__init__()
        self.setts = settings
        self.img = Drop.drop_image()
        self.image = pygame.image.load('./assets/imagens/game/' + self.img + '.png')
        self.rect = self.image.get_rect()

        # Start each new coin in the screen.
        self.rect.centerx = randint(10, int(settings.screen_width) - 10)
        self.rect.bottom = randint(10, int(settings.screen_height) - 10)
        # Store the coin's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    @staticmethod
    def new_drop(settings):
        drop = Drop(settings)
        settings.drops.add(drop)
    
    @staticmethod
    def drop_image():
        if randint(0, 10) <= 1: return "heart"
        return "coin"
    
    def drop_rate(self):
        if self.img == "heart": self.setts.player_lifes += 1
        elif randint(0, 10) <= 3: Drop.new_drop(self.setts)
        else: self.setts.bullet_speed_factor += 0.1
