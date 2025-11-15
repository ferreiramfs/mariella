import pygame
import sys
from scenes.main_game import MainGame

class MainMenu:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.clock = game.clock
        self.config = game.config
        
        # Opções do menu
        self.opcoes = ["Iniciar", "Sair"]
        self.opcao_selecionada = 0
        
        # Fontes
        self.fonte_titulo = pygame.font.Font(None, 74)
        self.fonte_opcoes = pygame.font.Font(None, 48)
        
        # Cores
        self.cor_normal = (3, 216, 243)
        self.cor_selecionada = (252, 238, 12)
        self.cor_titulo = (3, 116, 143)
        
        self.background_color = (0, 0, 0)
        
        # Efeitos visuais
        self.tempo_animacao = 0
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.opcao_selecionada = (self.opcao_selecionada - 1) % len(self.opcoes)
                elif event.key == pygame.K_DOWN:
                    self.opcao_selecionada = (self.opcao_selecionada + 1) % len(self.opcoes)
                elif event.key == pygame.K_RETURN:
                    self.executar_opcao()
                elif event.key == pygame.K_ESCAPE:
                    self.game.running = False
    
    def executar_opcao(self):
        opcao = self.opcoes[self.opcao_selecionada]
        
        if opcao == "Iniciar":
            # Muda para a cena do jogo principal
            self.game.current_scene = MainGame(self.game)
        elif opcao == "Sair":
            self.game.running = False
    
    def update(self, dt):
        # Animação sutil para dar vida ao menu
        self.tempo_animacao += dt
    
    def render(self):
        # Fundo
        self.screen.fill(self.background_color)
        
        # Título do jogo
        titulo = self.fonte_titulo.render("Mariella", True, self.cor_titulo)
        titulo_rect = titulo.get_rect(center=(self.config.screen_width // 2, 150))
        self.screen.blit(titulo, titulo_rect)
        
        # Opções do menu
        for i, opcao in enumerate(self.opcoes):
            # Define a cor baseada na seleção
            if i == self.opcao_selecionada:
                cor = self.cor_selecionada
                # Efeito de brilho para opção selecionada
                brilho = int(50 * abs(pygame.time.get_ticks() % 1000 - 500) / 500)
                cor = (min(255, self.cor_selecionada[0] + brilho),
                       min(255, self.cor_selecionada[1] + brilho),
                       min(255, self.cor_selecionada[2] + brilho))
            else:
                cor = self.cor_normal
            
            # Renderiza o texto da opção
            texto = self.fonte_opcoes.render(opcao, True, cor)
            texto_rect = texto.get_rect(center=(self.config.screen_width // 2, 300 + i * 80))
            
            # Seta indicadora para opção selecionada
            if i == self.opcao_selecionada:
                seta = self.fonte_opcoes.render(">", True, self.cor_selecionada)
                seta_rect = seta.get_rect(midright=(texto_rect.left - 20, texto_rect.centery))
                self.screen.blit(seta, seta_rect)
                
                seta_fim = self.fonte_opcoes.render("<", True, self.cor_selecionada)
                seta_fim_rect = seta_fim.get_rect(midleft=(texto_rect.right + 20, texto_rect.centery))
                self.screen.blit(seta_fim, seta_fim_rect)
            
            self.screen.blit(texto, texto_rect)
        
        # Instruções
        fonte_instrucoes = pygame.font.Font(None, 24)
        instrucoes = [
            "Use ↑↓ para navegar",
            "ENTER para selecionar",
            "ESC para sair"
        ]
        
        for j, instrucao in enumerate(instrucoes):
            texto_inst = fonte_instrucoes.render(instrucao, True, (3, 216, 243))
            self.screen.blit(texto_inst, (20, self.config.screen_height - 100 + j * 30))
        
        pygame.display.flip()