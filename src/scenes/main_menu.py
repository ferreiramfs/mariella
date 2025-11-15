import pygame
import sys
from scenes.main_game import MainGame

class MainMenu:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.clock = game.clock
        self.config = game.config
        
        # Menu options
        self.options = ["Iniciar", "Sair"]
        self.selected_option = 0
        
        # Fonts
        self.title_font = pygame.font.Font(None, 74)
        self.options_font = pygame.font.Font(None, 48)
        
        # Colors
        self.normal_color = (3, 216, 243)
        self.selected_color = (252, 238, 12)
        self.title_color = (3, 116, 143)
        
        self.background_color = (0, 0, 0)
        
        # Visual effects
        self.animation_time = 0
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    self.execute_option()
                elif event.key == pygame.K_ESCAPE:
                    self.game.running = False
    
    # keep old name for backwards compatibility if needed
    def execute_option(self):
        return self._execute_option()

    def _execute_option(self):
        option = self.options[self.selected_option]
        
        if option == "Iniciar":
            # Switch to main game scene
            self.game.current_scene = MainGame(self.game)
        elif option == "Sair":
            self.game.running = False
    
    def update(self, dt):
        # Subtle animation to bring the menu to life
        self.animation_time += dt
    
    def render(self):
        # Background
        self.screen.fill(self.background_color)
        
        # Game title
        title = self.title_font.render("Mariella", True, self.title_color)
        title_rect = title.get_rect(center=(self.config.screen_width // 2, 150))
        self.screen.blit(title, title_rect)
        
        # Menu options
        for i, option in enumerate(self.options):
            # Choose color based on selection
            if i == self.selected_option:
                color = self.selected_color
                # Glow effect for selected option
                glow = int(50 * abs(pygame.time.get_ticks() % 1000 - 500) / 500)
                color = (min(255, self.selected_color[0] + glow),
                       min(255, self.selected_color[1] + glow),
                       min(255, self.selected_color[2] + glow))
            else:
                color = self.normal_color
            
            # Render option text
            text_surf = self.options_font.render(option, True, color)
            text_rect = text_surf.get_rect(center=(self.config.screen_width // 2, 300 + i * 80))
            
            # Indicator arrows for selected option
            if i == self.selected_option:
                left_arrow = self.options_font.render(">", True, self.selected_color)
                left_arrow_rect = left_arrow.get_rect(midright=(text_rect.left - 20, text_rect.centery))
                self.screen.blit(left_arrow, left_arrow_rect)
                
                right_arrow = self.options_font.render("<", True, self.selected_color)
                right_arrow_rect = right_arrow.get_rect(midleft=(text_rect.right + 20, text_rect.centery))
                self.screen.blit(right_arrow, right_arrow_rect)
            
            self.screen.blit(text_surf, text_rect)
        
        # Instructions
        instructions_font = pygame.font.Font(None, 24)
        instructions = [
            "Use ↑↓ para navegar",
            "ENTER para selecionar",
            "ESC para sair"
        ]
        
        for j, instruction in enumerate(instructions):
            inst_surf = instructions_font.render(instruction, True, (3, 216, 243))
            self.screen.blit(inst_surf, (20, self.config.screen_height - 100 + j * 30))
        
        pygame.display.flip()