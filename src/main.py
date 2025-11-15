import pygame
from utils.config import Config
from scenes.main_menu import MainMenu

class Game:
    def __init__(self):
        pygame.init()
        self.config = Config()
        self.screen = self.config.get_display()
        pygame.display.set_caption(self.config.title)
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Scene system - start at the main menu
        self.current_scene = MainMenu(self)
    
    def run(self):
        while self.running:
            # Calculate delta time for smooth animations
            dt = self.clock.tick(self.config.fps) / 1000.0
            
            # Process current scene
            self.current_scene.handle_events()
            self.current_scene.update(dt)
            self.current_scene.render()
            
        pygame.quit()

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()