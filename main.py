"""
Arquivo principal do jogo Flappy Bird
Coordena todos os módulos e gerencia o loop principal do jogo
"""

import pygame
import random
import config
from player import Bird
from pipe import Pipe
from cloud import CloudManager
import game_state

pygame.init()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 48)
        self.small_font = pygame.font.Font(None, 36)
        
        self.reset_game()
    
    def reset_game(self):
        self.bird = Bird(100, config.SCREEN_HEIGHT // 2)
        self.pipes = []
        self.camera_x = 0
        self.score = 0
        self.game_over = False
        self.game_started = False
        self.spawn_timer = 0
        self.pipe_speed = config.BASE_PIPE_SPEED
        
        self.pipes.append(Pipe(700, self.pipe_speed))
        
        self.cloud_manager = CloudManager()
    
    def spawn_pipe(self):
        last_pipe_x = max([pipe.x for pipe in self.pipes]) if self.pipes else config.SCREEN_WIDTH
        new_x = last_pipe_x + random.randint(config.PIPE_SPAWN_DISTANCE, config.PIPE_SPAWN_DISTANCE + 200)
        self.pipes.append(Pipe(new_x, self.pipe_speed))
    
    def update(self):
        if self.game_over:
            return
        
        self.bird.update(self.game_started)
        
        if not self.game_started:
            return
        
        if game_state.check_collisions(self.bird, self.pipes, self.game_started):
            self.game_over = True
            return
        
        if self.bird.x > config.SCREEN_WIDTH // 2:
            self.camera_x = self.bird.x - config.SCREEN_WIDTH // 2
        
        for pipe in self.pipes[:]:
            pipe.update(self.pipe_speed)
            
            if game_state.check_score(self.bird, [pipe]):
                self.score += 1
                
                if self.pipe_speed < config.MAX_PIPE_SPEED:
                    self.pipe_speed = min(config.MAX_PIPE_SPEED, self.pipe_speed + config.SPEED_INCREMENT)
            
            if pipe.x + pipe.width < self.camera_x - 100:
                self.pipes.remove(pipe)
        
        self.spawn_timer += 1
        
        if self.spawn_timer >= random.randint(60, 120):
            self.spawn_pipe()
            self.spawn_timer = 0
        
        self.cloud_manager.update(self.pipe_speed, self.camera_x)
    
    def draw(self):
        self.screen.fill(config.BLUE)
        
        self.cloud_manager.draw(self.screen, self.camera_x)
        
        for pipe in self.pipes:
            pipe.draw(self.screen, self.camera_x)
        
        self.bird.draw(self.screen, self.camera_x)
        
        score_text = self.font.render(f"Score: {self.score}", True, config.WHITE)
        score_rect = score_text.get_rect(center=(config.SCREEN_WIDTH // 2, 30))
        
        shadow_text = self.font.render(f"Score: {self.score}", True, config.BLACK)
        shadow_rect = shadow_text.get_rect(center=(config.SCREEN_WIDTH // 2 + 2, 32))
        self.screen.blit(shadow_text, shadow_rect)
        self.screen.blit(score_text, score_rect)
        
        if not self.game_started:
            start_text = self.font.render("Toque para começar", True, config.WHITE)
            start_rect = start_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2))
            
            shadow_start = self.font.render("Toque para começar", True, config.BLACK)
            shadow_start_rect = shadow_start.get_rect(center=(config.SCREEN_WIDTH // 2 + 2, config.SCREEN_HEIGHT // 2 + 2))
            self.screen.blit(shadow_start, shadow_start_rect)
            self.screen.blit(start_text, start_rect)
        
        if self.game_over:
            game_over_text = self.font.render("GAME OVER", True, config.WHITE)
            game_over_rect = game_over_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2))
            
            restart_text = self.small_font.render("Pressione ESPACO para reiniciar", True, config.WHITE)
            restart_rect = restart_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 + 50))
            
            shadow_go = self.font.render("GAME OVER", True, config.BLACK)
            shadow_go_rect = shadow_go.get_rect(center=(config.SCREEN_WIDTH // 2 + 2, config.SCREEN_HEIGHT // 2 + 2))
            shadow_restart = self.small_font.render("Pressione ESPACO para reiniciar", True, config.BLACK)
            shadow_restart_rect = shadow_restart.get_rect(center=(config.SCREEN_WIDTH // 2 + 2, config.SCREEN_HEIGHT // 2 + 52))
            
            self.screen.blit(shadow_go, shadow_go_rect)
            self.screen.blit(shadow_restart, shadow_restart_rect)
            self.screen.blit(game_over_text, game_over_rect)
            self.screen.blit(restart_text, restart_rect)
        
        pygame.display.flip()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.game_over:
                        game_state.handle_game_restart(self, "KEYDOWN")
                    elif not self.game_started:
                        game_state.handle_game_start(self, "KEYDOWN")
                    else:
                        self.bird.jump()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    game_state.handle_game_restart(self, "MOUSEBUTTONDOWN")
                elif not self.game_started:
                    game_state.handle_game_start(self, "MOUSEBUTTONDOWN")
                else:
                    self.bird.jump()
        
        return True
    
    def run(self):
        running = True
        
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(config.FPS)
        
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
