import pygame as pyg
from .bullet import Bullet

class GameFuncts:
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
        if image:
            image_surface = pyg.image.load(image)
            image_rect = image_surface.get_rect()
            image_rect.midbottom = (settings.screen_width * width, settings.screen_height * height)
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
    def play_sound(settings, sound, tip=False):
        if settings.estado_som == True:
            path = "./assets/sound/" + sound + ".mp3"
            
            if tip:
                if not pyg.mixer.music.get_busy():
                    pyg.mixer.music.load(path)
                    pyg.mixer.music.play()
            else:
                pyg.mixer.Sound(path).play()
    
    @staticmethod
    def shoot(character, bullets, settings):
        if len(bullets) < settings.bullets_allowed:
            GameFuncts.play_sound(settings, "player/shoot")
            new_bullet = Bullet(settings, settings.screen, character)
            bullets.add(new_bullet)

    @staticmethod
    def show_settings(screen, settings):
        msg = """
Zombie Apocalypse (Apocalipse zombie)\n\n
- Quit ou tecla Esc para sair do jogo;\n
- Stop/Rerun ou r: pause ou reinicia o jogo.\n
- E para instruções;\n
- Mover-se com: cima, baixo, esquerda, direita ou cliques;\n
- Mouse clique ou espaço para atirar;\n\n
Desenvolvido por: Luiz Augusto (Louiexz, github)
"""
        text = [msg, 3000]
        GameFuncts.new_text(screen, settings, text, './assets/imagens/enemies/zombie-male.jpg')
    
    def show_stats(screen, settings, bullets):
        stats = [
            [f'Bullets\n\n{settings.bullets_allowed - len(bullets)}', 0.35],
            [f'Stage\n\n{str(settings.stage).center(7)}', 0.43],
            [f'Lifes\n\n{str(settings.player_lifes).center(6)}', 0.5],
            [f'Zombies killed:\n\n{str(settings.count).center(14)}', 0.62],
        ]

        for stat in stats:
            GameFuncts.new_text(screen, settings, [stat[0], 0], tamanho=32, width=stat[1], height=0.1)

