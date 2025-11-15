import pygame
from .constants import *

class Config:
    def __init__(self):
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.fps = FPS
        self.title = "Mariella"
        
    def get_display(self):
        return pygame.display.set_mode((self.screen_width, self.screen_height))