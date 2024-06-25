import pygame as pyg

class InputControls():
    @staticmethod
    def handle_keyboard_down_events(event, player):
        if event.key == pyg.K_RIGHT:
            player.value = 0
            player.keys[0] = True
        elif event.key == pyg.K_LEFT:
            player.value = 1
            player.keys[1] = True
        elif event.key == pyg.K_UP:
            player.value = 2
            player.keys[2] = True
        elif event.key == pyg.K_DOWN:
            player.value = 3
            player.keys[3] = True
        player.update_image()
        
        if event.key == pyg.K_SPACE: return 1
        elif event.key == pyg.K_p: return 2
        elif event.key == pyg.K_e: return 3
        elif event.key == pyg.K_m: return 4
        elif event.key == pyg.K_ESCAPE: return 5
        elif event.key == pyg.K_r: return 8

    @staticmethod
    def handle_keyboard_up_events(event, player):
        if event.key == pyg.K_RIGHT: player.keys[0] = False
        elif event.key == pyg.K_LEFT: player.keys[1] = False
        elif event.key == pyg.K_UP: player.keys[2] = False
        elif event.key == pyg.K_DOWN: player.keys[3] = False
        else: player.keys = [False] * 4

    @staticmethod
    def _process_mouse_input(event, player, buttons):
        if event.button == 1:  # Verifique se o clique foi com o botão esquerdo do mouse
            for button in buttons:
                if button.rect.collidepoint(event.pos):
                    if button.text == "Pause": return 2
                    elif button.text == "Instructions": return 3
                    elif button.text == "Sound": return 4
                    elif button.text == "Quit": return 5
        player.get_mouse_pos()
        return 1
    
    @staticmethod
    def usual_inputs(settings):
        for event in pyg.event.get():
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_p: return 2
                elif event.key == pyg.K_y: return 6
                elif event.key == pyg.K_n or event.key == pyg.K_ESCAPE: return 7
            elif event.type == pyg.QUIT: return 7
            elif event.type == pyg.MOUSEBUTTONDOWN and event.button == 1:
                for button in settings.quit_buttons:
                    if button.rect.collidepoint(event.pos):
                        if button.text == "Yes": return 6
                        elif button.text == "Pause": return 2
                        elif button.text == "No" : return 7
    
    @staticmethod
    def handle_input(player, buttons):
        for event in pyg.event.get():
            if event.type == pyg.QUIT: return 7
            elif event.type == pyg.MOUSEBUTTONDOWN: return InputControls._process_mouse_input(event, player, buttons)
            if event.type == pyg.KEYDOWN: return InputControls.handle_keyboard_down_events(event, player)
            elif event.type == pyg.KEYUP: return InputControls.handle_keyboard_up_events(event, player)
