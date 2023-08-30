import pygame
from tiles import Tile
from player import Player

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, block in enumerate(row):
                if block == 'X':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if block == 'P':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    player_sprite = Player((x, y), self.tiles)
                    self.player.add(player_sprite)

    def run(self):
        self.tiles.draw(self.display_surface)
        self.tiles.update(self.world_shift)

        self.player.update()
        self.player.draw(self.display_surface)
