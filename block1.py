import pygame
from setting1 import tile_size

class Block(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((tile_size, tile_size))
        self.image.fill((255, 105, 180))  # Set block color to pink (RGB tuple)
        self.rect = self.image.get_rect(topleft=pos)



