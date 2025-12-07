"""
Módulo de construção e gerenciamento do jogador (pássaro)
Gerencia sprites, animação, desenho e colisão do pássaro
"""

import pygame
import os
import config
import gravity

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0
        self.angle = 0
        
        self.animation_frame = 0
        self.animation_timer = 0
        
        self.sprite1 = pygame.image.load(os.path.join('assets', '1.png'))
        self.sprite2 = pygame.image.load(os.path.join('assets', '2.png'))
        
        self.sprite1 = pygame.transform.scale(self.sprite1, (50, 50))
        self.sprite2 = pygame.transform.scale(self.sprite2, (50, 50))
        
        self.width = self.sprite1.get_width()
        self.height = self.sprite1.get_height()
        
        self.radius = min(self.width, self.height) // 2 - 5
        
    def update(self, game_started=True):
        self.animation_timer += 1
        
        if self.animation_timer >= 10:
            self.animation_frame = (self.animation_frame + 1) % 2
            self.animation_timer = 0
        
        if not game_started:
            self.velocity = 0
            self.angle = 0
            return
        
        gravity.apply_gravity(self, game_started)
        gravity.limit_top_movement(self)
        gravity.calculate_rotation_angle(self)
    
    def jump(self):
        self.velocity = config.JUMP_STRENGTH
    
    def draw(self, screen, camera_x):
        current_sprite = self.sprite1 if self.animation_frame == 0 else self.sprite2
        
        rotated_sprite = pygame.transform.rotate(current_sprite, -self.angle)
        
        rect = rotated_sprite.get_rect(center=(self.x - camera_x + self.width // 2, 
                                                self.y + self.height // 2))
        
        screen.blit(rotated_sprite, rect)
    
    def get_collision_circle(self):
        center_x = self.x + self.width // 2
        center_y = self.y + self.height // 2
        return (center_x, center_y, self.radius)
    
    def check_ground_collision(self):
        bird_circle = self.get_collision_circle()
        _, bird_y, bird_radius = bird_circle
        return bird_y + bird_radius >= config.SCREEN_HEIGHT
