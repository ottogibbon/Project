import pygame
from setting import tile_size  # Import statement appears correct

class Block(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((tile_size, tile_size))
        self.image.fill((255, 105, 180))  # Changed the color to RGB tuple for pink
        self.rect = self.image.get_rect(topleft=pos)


