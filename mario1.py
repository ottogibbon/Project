import pygame
import sys
from setting1 import tile_size, level_map
from level1 import Level
from player1 import Player
from enemy1 import Enemy

# Initialize Pygame
pygame.init()

# Screen setup
screen_width = 1500
screen_height = len(level_map) * tile_size
screen = pygame.display.set_mode((screen_width, screen_height))

# Clock for controlling FPS
clock = pygame.time.Clock()

# Create instances
game_level = Level(level_map, screen)  # Initialize level with screen surface
player = Player((100, screen_height // 2), game_level.tiles)  

# Main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update
    player.update(game_level.tiles)  # Passed game_level.tiles for collision detection
    game_level.run()

    # Draw
    screen.fill((0, 0, 0))  # Fill the screen with black
    game_level.tiles.draw(screen)  # Draw the level tiles
    screen.blit(player.image, player.rect)  # Draw the player

    # Refresh screen
    pygame.display.update()

    # Cap the frame rate
    clock.tick(60)


	