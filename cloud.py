"""
Módulo de gerenciamento de nuvens
Cria e gerencia nuvens decorativas que aparecem no fundo
"""

import pygame
import random
import os
import config

class Cloud:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.image = pygame.image.load(os.path.join('assets', 'cloud.png'))
        
        self.width = self.image.get_width()
        self.height = self.image.get_height()
    
    def update(self, pipe_speed):
        self.x -= pipe_speed * config.CLOUD_SPEED_MULTIPLIER
    
    def draw(self, screen, camera_x):
        screen_x = self.x - camera_x
        screen.blit(self.image, (screen_x, self.y))

class CloudManager:
    def __init__(self):
        self.clouds = []
        self.spawn_timer = 0
        self.next_spawn_distance = random.randint(config.CLOUD_MIN_SPACING, config.CLOUD_MAX_SPACING)
    
    def spawn_cloud(self, last_x):
        new_x = last_x + self.next_spawn_distance
        new_y = random.randint(config.CLOUD_MIN_Y, config.CLOUD_MAX_Y)
        
        self.clouds.append(Cloud(new_x, new_y))
        
        self.next_spawn_distance = random.randint(config.CLOUD_MIN_SPACING, config.CLOUD_MAX_SPACING)
    
    def update(self, pipe_speed, camera_x):
        for cloud in self.clouds[:]:
            cloud.update(pipe_speed)
            
            if cloud.x + cloud.width < camera_x - 100:
                self.clouds.remove(cloud)
        
        if self.clouds:
            last_cloud_x = max([cloud.x for cloud in self.clouds])
            
            if last_cloud_x < camera_x + config.SCREEN_WIDTH + 300:
                self.spawn_cloud(last_cloud_x)
        else:
            start_x = camera_x + random.randint(100, config.SCREEN_WIDTH - 100)
            self.spawn_cloud(start_x)
            
            for i in range(2):
                next_x = start_x + (i + 1) * random.randint(config.CLOUD_MIN_SPACING, config.CLOUD_MAX_SPACING)
                self.spawn_cloud(next_x)
    
    def draw(self, screen, camera_x):
        for cloud in self.clouds:
            cloud.draw(screen, camera_x)
    
    def reset(self):
        self.clouds = []
        self.spawn_timer = 0
        self.next_spawn_distance = random.randint(config.CLOUD_MIN_SPACING, config.CLOUD_MAX_SPACING)
