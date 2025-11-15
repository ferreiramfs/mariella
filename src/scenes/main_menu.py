import pygame

class MainMenu:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(None, 36)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.running = False
    
    def update(self, dt):
        pass
    
    def render(self):
        self.game.screen.fill((0, 0, 0))
        text = self.font.render("Menu Principal - Pressione ESC para sair", True, (255, 255, 255))
        self.game.screen.blit(text, (100, 100))
        pygame.display.flip()