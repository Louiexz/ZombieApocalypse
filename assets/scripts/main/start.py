import pygame as pyg
from ..characters.player import Player
from .settings import Settings
from ..game.button import Button
from ..game.game_loop import GameLoop

class InitializeGame:
    def __init__(self):
        pyg.init()
        pyg.display.set_caption("Apocalypse Zombie")

        screen_info = pyg.display.Info()
        width = screen_info.current_w
        height = screen_info.current_h
        screen = pyg.display.set_mode((width, height))

        ai_sets = Settings(width, height, screen)
        player = Player(screen, ai_sets)

        ai_sets.game_buttons = [Button(pyg, *button) for button in ai_sets.game_buttons]
        ai_sets.quit_buttons = [Button(pyg, *button) for button in ai_sets.quit_buttons]

        GameLoop.run_game_loop(screen, ai_sets, player)
       
if __name__ == "__main__": InitializeGame()