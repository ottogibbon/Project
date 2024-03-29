import pygame
from setting1 import tile_size

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, tiles):
        super().__init__()
        self.image = pygame.Surface((tile_size, tile_size))
        self.image.fill((255, 0, 0))  # Set enemy color to red (RGB tuple)
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(1, 0)  # Initial movement direction to the right
        self.velocity = pygame.math.Vector2(2, 0)  # Set the speed of the enemy
        self.tiles = tiles  # Reference to the tiles in the level

    def update(self):
        # Update the enemy position based on its velocity and direction
        self.rect.x += self.direction.x * self.velocity.x
        self.rect.y += self.direction.y * self.velocity.y

        # Collision detection with blocks
        for tile in self.tiles:
            if self.rect.colliderect(tile):
                self.direction.x *= -1  # Reverse direction upon collision
