import os
import sys
import pygame as pyg
from .bullet import Bullet

class GameFuncts:
    @staticmethod
    def new_text(screen, settings, txt, image=None):
        font = pyg.font.SysFont(None, 44)
        lines = txt[0].split("\n")
        text_surfaces = []
        for line_number, line in enumerate(lines):
            text_surface = font.render(line, True, (255, 0, 0))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (settings.screen_width * txt[1], settings.screen_height * 0.5 + line_number * 30)
            text_surfaces.append((text_surface, text_rect, txt[2]))
        returns = [text_surfaces]
        if image:
            image_surface = pyg.image.load(image)
            image_rect = image_surface.get_rect()
            image_rect.midbottom = (settings.screen_width * 0.53, settings.screen_height * 0.4)
            returns.append([image_surface, image_rect])
        GameFuncts.show_text(screen, *returns)

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
    def play_sound(sound, tip=False):
        path = "./assets/sound/" + sound + ".mp3"
        if tip:
            if not pyg.mixer.music.get_busy():
                pyg.mixer.music.load(path)
                pyg.mixer.music.play()
        else: pyg.mixer.Sound(path).play()

    @staticmethod
    def shoot(character, bullets, settings):
        if len(bullets) < settings.bullets_allowed:
            GameFuncts.play_sound("game/shoot")
            new_bullet = Bullet(settings, settings.screen, character)
            bullets.add(new_bullet)

    @staticmethod
    def show_settings(screen, settings):
        msg = """
Zombie Apocalypse (Apocalipse zombie)\n
- Quit ou tecla Esc para sair do jogo;\n
- Stop/Rerun ou r: pause ou reinicia o jogo.\n
- E para instruções;\n
- Mover-se com: cima, baixo, esquerda, direita ou cliques;\n
- Mouse clique ou espaço para atirar;\n
"""
        text = [msg, 0.53, 3000]
        GameFuncts.new_text(screen, settings, text, './assets/imagens/enemies/zombie-male.jpg')
