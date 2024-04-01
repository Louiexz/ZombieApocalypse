import sys
import pygame as pyg

class InputControls():
    @staticmethod
    def handle_keyboard_events(event, player):
        if event.key == pyg.K_RIGHT: player.moving_right = True
        elif event.key == pyg.K_LEFT: player.moving_left = True
        elif event.key == pyg.K_UP: player.moving_up = True
        elif event.key == pyg.K_DOWN: player.moving_down = True
        elif event.key == pyg.K_SPACE: return 1
        elif event.key == pyg.K_r: return 2
        elif event.key == pyg.K_e: return 3

    @staticmethod
    def _process_mouse_input(event, player, buttons):
        if event.button == 1:  # Verifique se o clique foi com o botão esquerdo do mouse
            for button in buttons:
                if button.rect.collidepoint(event.pos):
                    if button.text == "Stop/Rerun": return 2
                    elif button.text == "Instructions": return 3
                    else: sys.exit()
        
        player.update_image()
        return 1

    @staticmethod
    def handle_input(player, buttons):
        for event in pyg.event.get():
            if event.type == pyg.QUIT or (event.type == pyg.KEYDOWN and event.key == pyg.K_ESCAPE): sys.exit()
            elif event.type == pyg.KEYDOWN: return InputControls.handle_keyboard_events(event, player)
            elif event.type == pyg.MOUSEBUTTONDOWN: return InputControls._process_mouse_input(event, player, buttons)
