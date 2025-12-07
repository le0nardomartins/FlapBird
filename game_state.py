"""
Módulo de mecânica de morte e reinício do jogo
Gerencia estados do jogo (início, jogando, game over) e reinício
"""

import config

def check_collisions(bird, pipes, game_started):
    if not game_started:
        return False
    
    if bird.check_ground_collision():
        return True
    
    bird_circle = bird.get_collision_circle()
    _, bird_y, bird_radius = bird_circle
    
    if bird_y - bird_radius < 0:
        return True
    
    for pipe in pipes:
        if pipe.check_collision(bird_circle):
            return True
    
    return False

def check_score(bird, pipes):
    for pipe in pipes:
        if pipe.check_passed(bird.x):
            return True
    return False

def reset_game_state(game):
    game.bird.x = 100
    game.bird.y = config.SCREEN_HEIGHT // 2
    game.bird.velocity = 0
    game.bird.angle = 0
    
    game.pipes = []
    game.camera_x = 0
    game.score = 0
    game.game_over = False
    game.game_started = False
    game.spawn_timer = 0
    game.pipe_speed = config.BASE_PIPE_SPEED
    
    from pipe import Pipe
    game.pipes.append(Pipe(700, game.pipe_speed))
    
    if hasattr(game, 'cloud_manager'):
        game.cloud_manager.reset()

def handle_game_start(game, event_type):
    if not game.game_started:
        game.game_started = True
        game.bird.jump()

def handle_game_restart(game, event_type):
    if game.game_over:
        reset_game_state(game)
