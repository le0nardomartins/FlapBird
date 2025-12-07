"""
Módulo de mecânica de gravidade
Gerencia a física de queda e movimento vertical do pássaro
"""

import config

def apply_gravity(bird, game_started):
    if not game_started:
        return
    
    bird.velocity += config.GRAVITY
    bird.y += bird.velocity

def limit_top_movement(bird):
    if bird.y < 0:
        bird.y = 0
        bird.velocity = 0

def calculate_rotation_angle(bird):
    max_angle = 30
    bird.angle = max(-max_angle, min(max_angle, bird.velocity * 3))
