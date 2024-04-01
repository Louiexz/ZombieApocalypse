import sys
import pygame as pyg
from ..characters.functs.input_controls import InputControls
from ..characters.functs.zombie_functs import ZombieFuncts
from .game_functs import GameFuncts

class GameControls:
    @staticmethod
    def update_bullets(bullets, zombies, settings):
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
                ZombieFuncts.check_bullet_zombie_collisions(bullets, zombies, settings)

    @staticmethod
    def reset_game(settings, zombies, bullets, player):
        settings.restart() # Reinicie as configurações e objetos do jogo   
        zombies.empty() # Remova todos os self.zombies e balas restantes
        bullets.empty()
        player.restart() # Reposicione a espaçonave

        settings.pause = False
        
    @staticmethod
    def handle_stop_restart(settings, bullets, zombies, player, pause=False):
        if pause: GameControls.reset_game(settings, zombies, bullets, player)
    
    @staticmethod
    def update_screen(screen, player, bullets, zombies, settings, buttons):
        if not settings.pause:
            screen.fill(settings.bg_color)
            player.blitme()
            zombies.draw(screen)
            updated_rects = []
            for zombie in zombies.sprites(): updated_rects.append(zombie.rect)
            for bullet in bullets.sprites(): bullet.draw_bullet()
            for button in buttons: button.draw(screen)
            msg = f"""
Stage: {settings.stage}\nLifes: {settings.player_lifes}
Zombies killed: {settings.count}\nBullets: {settings.bullets_allowed - len(bullets)}"""
            GameFuncts.new_text(screen, settings, [msg, 0.1, 10])
            
            pyg.display.update(updated_rects)
    
    @staticmethod
    def game_over(screen, settings, bullets, zombies, player, buttons):
        GameFuncts.play_sound("game/game-over-transition", "music")
        GameFuncts.play_sound("game/game-over-voice")
        msg = f"Game Over\nZombie destroyed: {settings.count}\nStage: {settings.stage}"
        GameFuncts.new_text(screen, settings, [msg, 0.53, 10*5], './assets/imagens/enemies/zombie-reaching.jpg')
        while not settings.rodando:
            for event in pyg.event.get():
                if event.type == pyg.KEYDOWN and event.key == pyg.K_r:
                    GameControls.handle_stop_restart(settings, bullets, zombies, player, True)
                    settings.rodando = True
                elif event.type == pyg.QUIT or (event.type == pyg.KEYDOWN and event.key == pyg.K_ESCAPE): sys.exit()
                # Verifique se o clique foi com o botão esquerdo do mouse
                if event.type == pyg.MOUSEBUTTONDOWN and event.button == 1:
                    for button in buttons:
                        if button.rect.collidepoint(event.pos):
                            if button.text == "Stop/Rerun":
                                GameControls.handle_stop_restart(settings, bullets, zombies, player, True)
                                settings.rodando = True
                            else: sys.exit()
    
    @staticmethod
    def render_game(screen, player, bullets, zombies, buttons, settings):
        screen.fill(settings.bg_color)
        player.blitme()
        zombies.draw(screen)

        for bullet in bullets.sprites(): bullet.draw_bullet()
        for button in buttons: button.draw(screen)

        pyg.display.flip()
    
    @staticmethod
    def control_frame_rate():
        clock = pyg.time.Clock()
        clock.tick(60)
    
    @staticmethod
    def run_game_loop(screen, settings, buttons, bullets, zombies, player):
        GameFuncts.show_settings(screen, settings)
        GameFuncts.play_sound("zombie/zombie-music", True)

        while settings.rodando:
            input = InputControls.handle_input(player, buttons)
            if input == 1: GameFuncts.shoot(player, bullets, settings)
            elif input == 2:
                GameFuncts.new_text(screen, settings, ["Jogo pausado", 0.53, 10000])
                GameControls.handle_stop_restart(settings, bullets, zombies, player)
            elif input == 3:
                GameFuncts.play_sound("zombie/zombie-music")
                GameFuncts.show_settings(screen, settings)
            
            GameControls().update_bullets(bullets, zombies, settings)
            player.update()

            som = ZombieFuncts.handle_game_logic(screen, player, bullets, zombies, settings)
            if som[0] == True: GameFuncts().play_sound("zombie/zombie-death")
            if som[1] == True: GameControls().game_over(screen, settings, bullets, zombies, player, buttons)
            elif som[1] == False: GameFuncts().play_sound("zombie/zombie-bite")
            
            if len(zombies.sprites()) < settings.zombies_allowed:
                ZombieFuncts.create_zombie(zombies, ZombieFuncts.get_random_zombies(), settings)

            GameControls.update_screen(screen, player, bullets, zombies, settings, buttons)
            GameControls.render_game(screen, player, bullets, zombies, buttons, settings)
            GameControls.control_frame_rate()
