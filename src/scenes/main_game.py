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
                    # Volta para o menu principal
                    from scenes.main_menu import MainMenu
                    self.game.current_scene = MainMenu(self.game)
    
    def update(self, dt):
        # Aqui vai a lógica principal do jogo
        pass
    
    def render(self):
        # Tela temporária do jogo
        self.screen.fill((50, 120, 80))
        
        # Texto indicativo
        fonte = pygame.font.Font(None, 48)
        texto = fonte.render("Jogo Principal - ESC para voltar", True, (255, 255, 255))
        texto_rect = texto.get_rect(center=(self.game.config.screen_width // 2, 
                                          self.game.config.screen_height // 2))
        self.screen.blit(texto, texto_rect)
        
        pygame.display.flip()