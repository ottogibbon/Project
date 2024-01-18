import pygame
from block1 import Block  # Import Block class from block1.py
from player1 import Player  # Import Player class from player1.py
from setting1 import tile_size  # Import tile_size from setting1.py

# Load new scenery sprites 
ground_sprite = pygame.image.load('scenery_ground.png')
brick_sprite = pygame.image.load('scenery_brick.png')
question_block_sprite = pygame.image.load('scenery_question_block.png')
pipe_top_sprite = pygame.image.load('scenery_pipe_top.png')
pipe_bottom_sprite = pygame.image.load('scenery_pipe_bottom.png')

class Level:
    def __init__(self, level_map, screen):
        self.level_map = level_map
        self.screen = screen
        self.tiles = pygame.sprite.Group()
        
        # Create the level layout based on the level_map
        tile_height, tile_width = ground_sprite.get_height(), ground_sprite.get_width()
        for row_idx, row in enumerate(self.level_map):
            for col_idx, tile_type in enumerate(row):
                x, y = col_idx * tile_width, row_idx * tile_height
                
                if tile_type == 'G':
                    tile = tile(ground_sprite, x, y)
                elif tile_type == 'B':
                    tile = tile(brick_sprite, x, y)
                elif tile_type == 'Q':
                    tile = tile(question_block_sprite, x, y)
                elif tile_type == 'T':
                    tile = tile(pipe_top_sprite, x, y)
                elif tile_type == 'P':
                    tile = tile(pipe_bottom_sprite, x, y)
                else:
                    continue
                
                self.tiles.add(tile)
