import os
import pygame as pyg
from ..zombie import Zombie

class ZombieFuncts():
    @staticmethod
    def nivels(settings):
        if settings.count % 100 == 0:
            settings.bullets_allowed += 2
            settings.player_speed_factor += 5
            settings.bg_color = settings.ruina
        
        settings.zombie_speed_factor += 1
        settings.stage += 1
        settings.zombies_allowed += 1
        if settings.bg_color != settings.ruina: settings.bg_color = settings.terra

    @staticmethod
    def zombies_killed(settings):
        if settings.count % 20 == 0: ZombieFuncts.nivels(settings)

    @staticmethod
    def check_bullet_zombie_collisions(bullets, zombies, settings):
        """Respond to bullet-zombie collisions."""
        # Remove any bullets and zombies that have collided
        collisions = pyg.sprite.groupcollide(bullets, zombies, True, True) 
        if collisions:
            for zombies in collisions.values():
                # each value is a list of zombies that were hit by the same bullet
                for zombie in zombies:
                    zombie.kill()
                    settings.count += 1
                    ZombieFuncts.zombies_killed(settings)
                    return True
        return False
    
    @staticmethod
    def checks_zombie(zombies, screen, player):
        for zombie in zombies.sprites():
            zombie.check_edges(screen)
            zombie.check_player(player)
    
    @staticmethod
    def update_zombies(zombies, screen, settings, player):
        ZombieFuncts.checks_zombie(zombies, screen, player)
        zombies.update(settings)
        zombies.draw(screen)

    @staticmethod
    def handle_game_logic(screen, player, bullets, zombies, settings):
        valores = []
        ZombieFuncts.update_zombies(zombies, screen, settings, player)
        valores.append(ZombieFuncts.check_bullet_zombie_collisions(bullets, zombies, settings))
        valores.append(ZombieFuncts.check_zombies_attack(screen, player, settings, zombies))
        return valores

    @staticmethod
    def check_zombies_attack(screen, player, settings, zombies):
        # Verifica se algum zombieígena alcançou a parte inferior da tela.
        screen_rect = screen.get_rect()

        # Check for zombies hitting the player
        for zombie in zombies.sprites():
            if abs(zombie.rect.centerx - player.rect.centerx) <= settings.tolerance:
                img = zombie.zombie_image.split('_')
                zombie.image = pyg.image.load(f'./assets/imagens/enemies/attack/{img[0]}_attack.png') 
                settings.player_lifes -= 1
                zombie.image = pyg.image.load(f'./assets/imagens/enemies/idle/{img[0]}_idle.png') 
                if settings.player_lifes < 1:
                    settings.rodando = False
                    return True
                return False
    
    @staticmethod
    def get_random_zombies():
        # Gera um índice aleatório usando os.urandom
        archives = os.listdir('./assets/imagens/enemies/idle')
        random = int.from_bytes(os.urandom(4), byteorder='big') % len(archives)
    
        return archives[random]
    
    @staticmethod
    def create_zombie(zombies, zombie_image, settings):
        zombie = Zombie(zombie_image, settings)
        zombie_width = zombie.rect.width
        zombie.x = zombie_width + 1.3 * zombie_width * 2
        zombie.rect.x = zombie.x
        zombies.add(zombie)
