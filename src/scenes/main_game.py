import pygame

class MainGame:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.clock = game.clock
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Return to the main menu
                    from scenes.main_menu import MainMenu
                    self.game.current_scene = MainMenu(self.game)
    
    def update(self, dt):
        # Main game logic goes here
        pass
    
    def render(self):
        # Temporary game screen
        self.screen.fill((50, 120, 80))
        
        # Informational text
        font = pygame.font.Font(None, 48)
        text = font.render("Jogo - Esc para sair", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.game.config.screen_width // 2, 
                                          self.game.config.screen_height // 2))
        self.screen.blit(text, text_rect)
        
        pygame.display.flip()