import sys
import pygame as pyg
from ..characters.functs.input_controls import InputControls
from ..characters.functs.zombie_functs import ZombieFuncts
from .game_functs import GameFuncts
from .screen_control import ScreenControls

class GameLoop:
    @staticmethod
    def update_bullets(settings):
        """
        Update bullet positions and handle bullet collisions.

        Args:
        - settings (object): Game settings object containing bullets and screen dimensions.
        """
        bullets = settings.bullets
        screen_width = settings.screen_width
        screen_height = settings.screen_height

        bullets.update()

        for bullet in bullets.copy():
            if bullet.rect.bottom < 0 or bullet.rect.top > screen_height or bullet.rect.left < 0 or bullet.rect.right > screen_width:
                bullets.remove(bullet)
                ZombieFuncts.check_bullet_zombie_collisions(settings)

    @staticmethod
    def handle_pause(screen, player, settings):
        """
        Handle pausing the game.

        Args:
        - screen (object): Pygame screen object for displaying messages.
        - settings (object): Game settings object for resetting game state and managing pause state.
        """
        # Mostra texto "Jogo pausado" imediatamente
        GameFuncts.new_text(screen, settings, ["Jogo pausado", 0])
        while True:
            input_return = InputControls.usual_inputs(settings)

            pyg.display.flip()

            if input_return == 2: break
            if input_return in [2, 7]: GameLoop.get_input_action(screen, player, settings, input_return)
    
    @staticmethod
    def game_over(screen, player, settings):
        GameFuncts.play_sound(settings, "game/game-over-transition", "music")
        GameFuncts.play_sound(settings, "game/game-over-voice")

        msg = f"""
        Game Over\n
        Zombie destroyed: {settings.count}\n
        Stage: {settings.stage}\n\n
        Restart game?\n\n\n\n
        Development by: Luiz Augusto (Louiexz, github)"""

        GameFuncts.new_text(screen, settings, [msg, 0], 'enemies/zombie-reaching.png')

        while True:
            for button in settings.quit_buttons: button.draw(screen)
            pyg.display.flip()

            input_return = InputControls.usual_inputs(settings)

            if input_return == 6:
                GameFuncts.reset_game(settings, player)
                break
            elif input_return == 7: GameLoop.get_input_action(screen, player, settings, input_return)

    @staticmethod
    def get_input_action(screen, player, settings, action_type, is_game_over=False):
        """
        Process player input actions to perform corresponding game actions.

        Args:
        - screen (object): Pygame screen object for displaying messages and game elements.
        - player (object): Player object for performing player actions.
        - settings (object): Game settings object for managing game state and settings.
        - action_type (int): Type of action to perform.
        - is_game_over (bool, optional): Flag indicating if the game is over. Default is False.
        """
        if action_type == 1: GameFuncts.shoot(player, settings)
        elif action_type == 2: GameLoop.handle_pause(screen, player, settings)
        elif action_type == 3:
            GameFuncts.play_sound(settings, "zombie/zombie-music")
            GameFuncts.show_settings(screen, settings)
        elif action_type == 4: settings.estado_som = not settings.estado_som
        elif action_type == 5 or is_game_over: GameLoop.game_over(screen, player, settings)
        elif action_type == 7: sys.exit()
        elif action_type == 8:
            for bullet in settings.bullets:
                bullet.kill()
                break

    @staticmethod
    def run_game_loop(screen, settings, player):
        """
        Run the main game loop to handle game updates and rendering.

        Args:
        - screen (object): Pygame screen object for displaying game elements.
        - settings (object): Game settings object for managing game state and settings.
        - player (object): Player object for controlling player actions.
        """
        GameFuncts.play_sound(settings, "zombie/zombie-music", True)
        GameFuncts.show_settings(screen, settings)

        while settings.rodando:
            input_action = InputControls.handle_input(player, settings.game_buttons)
            logic_return = ZombieFuncts.handle_game_logic(screen, player, settings)

            GameLoop.get_input_action(screen, player, settings, input_action, logic_return[1])
            GameFuncts.get_logic_return(settings, logic_return)

            GameLoop.update_bullets(settings)
            player.update_state(screen)

            if len(settings.zombies.sprites()) < settings.zombies_allowed:
                ZombieFuncts.create_zombie(settings)

            GameFuncts.show_stats(screen, settings)
            ScreenControls.update_screen(screen, settings)
            GameFuncts.check_drop_collect(player, settings)
            ScreenControls.render_game(screen, player, settings)
            GameFuncts.control_frame_rate()
