import pygame
from tiles import Tile
from settings import tile_size

class Level:
    def __init__(self,level_data,surface):
        self.display_surface = surface
        self.setup_level(level_data)

    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        for row_index,row in enumerate(layout):
            for col_index,block in enumerate(row):
                if block == 'X':
                    print(f'{row_index}{col_index}:{block}')
    def run(self):
        self.tiles.draw(self.display_surface)