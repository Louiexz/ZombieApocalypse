import pygame as pyg
from .bullet import Bullet
from .drop import Drop

class GameFuncts:
    @staticmethod
    def control_frame_rate():
        """
        Control the frame rate to approximately 60 frames per second.
        """
        clock = pyg.time.Clock()
        clock.tick(60)
    
    @staticmethod
    def reset_game(settings, player):
        """
        Reset game state.

        Args:
        - settings (object): Game settings object to reset bullets, zombies, drops, and pause state.
        - player (object): Player object to reset player state.
        """
        settings.restart()
        settings.zombies.empty()
        settings.bullets.empty()
        settings.drops.empty()
        player.restart()
    
    @staticmethod
    def play_sound(settings, sound, tip=False):
        if settings.estado_som:
            path = "./assets/sound/" + sound + ".mp3"
            
            if tip:
                if not pyg.mixer.music.get_busy():
                    pyg.mixer.music.load(path)
                    pyg.mixer.music.play()
            else:
                pyg.mixer.Sound(path).play()
    
    @staticmethod
    def get_logic_return(settings, logic_return):
        """
        Process game logic results to play sounds and update game state.

        Args:
        - settings (object): Game settings object for sound management and game state updates.
        - logic_results (tuple): Tuple containing logic results from game logic processing.
        """
        if logic_return[0]:
            GameFuncts.play_sound(settings, "zombie/zombie-death")
            Drop.new_drop(settings)
        elif logic_return[1] == False:
            GameFuncts.play_sound(settings, "zombie/zombie-bite")

    @staticmethod
    def check_drop_collect(player, settings):
        # Check for drop collect by the player
        for drop in settings.drops.sprites():
            if drop.rect.colliderect(player.rect):
                drop.kill()
                GameFuncts.play_sound(settings, "game/collect-points")
                settings.drops_collected += 1

                drop.drop_rate()
    
    @staticmethod
    def shoot(character, settings):
        if len(settings.bullets) < settings.bullets_allowed:
            GameFuncts.play_sound(settings, "player/shoot")
            new_bullet = Bullet(settings, settings.screen, character)
            settings.bullets.add(new_bullet)
    
    @staticmethod
    def new_img(image, settings, width=0.5, height=0.4):
        image_surface = pyg.image.load("./assets/imagens/" + image)
        image_rect = image_surface.get_rect()
        image_rect.midbottom = (settings.screen_width * width, settings.screen_height * height)
        
        return [image_surface, image_rect]

    @staticmethod
    def show_text(screen, text_surfaces, image=None):
        rects = []
        for text_surface, text_rect, time in text_surfaces:
            screen.blit(text_surface, text_rect)
            rects.append(text_rect)
        if image:
            screen.blit(image[0], image[1])
            rects.append(image[1])
        pyg.display.update(rects)
        pyg.time.delay(time)
    
    @staticmethod
    def new_text(screen, settings, txt, image=False, color=(255, 255, 255), tamanho=36, width=0.5, height=0.5):
        font = pyg.font.SysFont(None, tamanho)
        lines = txt[0].split("\n")
        text_surfaces = []
        for line_number, line in enumerate(lines):
            text_surface = font.render(line, True, color)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (settings.screen_width * width, settings.screen_height * height + line_number * 15)
            text_surfaces.append((text_surface, text_rect, txt[1]))
        returns = [text_surfaces]
        if image: returns.append(GameFuncts.new_img(image, settings))

        GameFuncts.show_text(screen, *returns)
    
    @staticmethod
    def show_settings(screen, settings):
        msg = """
Zombie Apocalypse (Apocalipse zombie)\n\n
- Key Esc for exit game;\n
- Key E for instructions;\n
- Click or space for shoot;\n
- Key R for recharge;\n
- Key P: for pause the game.\n
- Move with arrows: UP, DOWN, LEFT and RIGHT;\n\n
Development by: Luiz Augusto (Louiexz, github)
"""
        text = [msg, 3000]
        GameFuncts.new_text(screen, settings, text, 'enemies/zombie-male.jpg')
    
    def show_stats(screen, settings):
        stats = [
            [f'Bullets\n\n{settings.bullets_allowed - len(settings.bullets)}', 0.3],
            [f'Stage\n\n{str(settings.stage).center(7)}', 0.36],
            [f'Lifes\n\n{str(settings.player_lifes).center(6)}', 0.41],
            [f'Zombies killed\n\n{str(settings.count).center(14)}', 0.50],
            [f'drops collected \n\n{settings.drops_collected}', 0.63],
        ]

        for stat in stats:
            GameFuncts.new_text(screen, settings, [stat[0], 0], tamanho=32, width=stat[1], height=0.1)
