import pygame as pyg

class ScreenControls():
    @staticmethod
    def update_screen(screen, settings):
        """Update the game screen."""
        if not settings.pause:
            updated_rects = []
            screen.fill(settings.bg_color)

            for button in settings.game_buttons: button.draw(screen)
            # Draw all sprites at once
            for sprite_group in [settings.zombies, settings.drops, settings.bullets]:
                updated_rects.extend(sprite.rect for sprite in sprite_group.sprites())

            pyg.display.update(updated_rects)

    @staticmethod
    def render_game(screen, player, settings):
        """Render the game state to the screen."""
        screen.fill(settings.bg_color)
        player.blitme()
        settings.zombies.draw(screen)
        settings.drops.draw(screen)
        
        for button in settings.game_buttons: button.draw(screen)
        for bullet in settings.bullets: bullet.draw_bullet()

        pyg.display.flip()

