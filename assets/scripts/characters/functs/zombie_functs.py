import pygame as pyg
from ..zombie import Zombie

class ZombieFuncts():
    @staticmethod
    def create_zombie(settings):
        zombie = Zombie()
        if "Boss_idle" in zombie.zombie_image: zombie.zombie_life = 2
        zombie.spawn(settings)
        settings.zombies.add(zombie)
    
    @staticmethod
    def nivels(settings):
        if settings.count % 100 == 0:
            settings.bullets_allowed += 1
            settings.player_speed_factor += 2
            settings.bg_color = settings.ruina
        
        settings.zombie_speed_factor += 0.5
        settings.stage += 1
        settings.zombies_allowed += 0.2
        if settings.bg_color != settings.ruina: settings.bg_color = settings.terra

    @staticmethod
    def zombies_killed(settings):
        if settings.count % 20 == 0: ZombieFuncts.nivels(settings)
    
    @staticmethod
    def checks_zombie(zombies, screen, player):
        for zombie in zombies.sprites():
            zombie.check_edges(screen)
            zombie.check_player(player)
    
    @staticmethod
    def update_zombies(screen, settings, player):
        ZombieFuncts.checks_zombie(settings.zombies, screen, player)
        settings.zombies.update(settings)
        settings.zombies.draw(screen)
    
    @staticmethod
    def check_bullet_zombie_collisions(settings):
        """Respond to bullet-zombie collisions."""
        # Detect collisions between bullets and zombies
        collisions = pyg.sprite.groupcollide(settings.bullets, settings.zombies, True, False)

        # Process each collision
        for bullet, zombies_hit in collisions.items():
            for zombie in zombies_hit:
                zombie.zombie_life -= 1
                if zombie.zombie_life <= 0:
                    zombie.kill()
                    settings.count += 1
                    ZombieFuncts.zombies_killed(settings)
                    return True  # Return True if a zombie was killed
        return False  # Return False if no zombies were killed
    
    @staticmethod
    def check_zombies_attack(player, settings):
        # Check for zombies hitting the player
        for zombie in settings.zombies.sprites():
            if zombie.rect.colliderect(player.rect):
                img = zombie.zombie_image.split('_')
                zombie.image = pyg.image.load(f'./assets/imagens/enemies/attack/{img[0]}_attack.png') 
                
                settings.player_lifes -= zombie.zombie_life
                
                zombie.zombie_life -= 1
                if zombie.zombie_life == 0: zombie.kill()

                if settings.player_lifes < 1: return True
                return False
            
    @staticmethod
    def handle_game_logic(screen, player, settings):
        valores = []
        ZombieFuncts.update_zombies(screen, settings, player)
        valores.append(ZombieFuncts.check_bullet_zombie_collisions(settings))
        valores.append(ZombieFuncts.check_zombies_attack(player, settings))
        return valores
