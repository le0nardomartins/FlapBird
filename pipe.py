"""
Módulo de construção e gerenciamento dos canos
Gerencia criação, desenho e colisão dos obstáculos
"""

import pygame
import random
import config

class Pipe:
    def __init__(self, x, pipe_speed):
        self.x = x
        self.width = config.PIPE_WIDTH
        self.pipe_speed = pipe_speed
        
        self.gap_size = random.randint(config.MIN_PIPE_GAP, config.MAX_PIPE_GAP)
        
        min_gap_y = 100
        max_gap_y = config.SCREEN_HEIGHT - 100 - self.gap_size
        self.gap_y = random.randint(min_gap_y, max_gap_y)
        
        self.passed = False
    
    def update(self, pipe_speed):
        self.pipe_speed = pipe_speed
        self.x -= self.pipe_speed
    
    def draw(self, screen, camera_x):
        screen_x = self.x - camera_x
        
        if screen_x + self.width < -100 or screen_x > config.SCREEN_WIDTH + 100:
            return
        
        top_rect = pygame.Rect(screen_x, 0, self.width, self.gap_y)
        pygame.draw.rect(screen, config.GREEN, top_rect)
        pygame.draw.rect(screen, config.DARK_GREEN, top_rect, 3)
        
        bottom_y = self.gap_y + self.gap_size
        bottom_height = config.SCREEN_HEIGHT - bottom_y
        
        bottom_rect = pygame.Rect(screen_x, bottom_y, self.width, bottom_height)
        pygame.draw.rect(screen, config.GREEN, bottom_rect)
        pygame.draw.rect(screen, config.DARK_GREEN, bottom_rect, 3)
    
    def check_collision(self, bird_circle):
        bird_x, bird_y, bird_radius = bird_circle
        
        if bird_x + bird_radius < self.x or bird_x - bird_radius > self.x + self.width:
            return False
        
        if bird_y - bird_radius < self.gap_y:
            return True
        
        if bird_y + bird_radius > self.gap_y + self.gap_size:
            return True
        
        return False
    
    def check_passed(self, bird_x):
        if not self.passed and bird_x > self.x + self.width:
            self.passed = True
            return True
        return False
