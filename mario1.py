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

    
    # Check if player is off the map and quit the game if so
    if player.rect.x < 0 or player.rect.x > (len(level_map[0]) * tile_size) or player.rect.y > screen_height:
        pygame.quit()
        sys.exit()
# Update
    player.update(game_level.tiles)  # Passed game_level.tiles for collision detection
    game_level.run()

    
    # Scrolling camera logic
    camera_offset = -player.rect.x + screen_width // 2  # Keep player in the center
    if camera_offset > 0:
        camera_offset = 0  # Don't scroll beyond the left edge of the level

    # Draw
    screen.fill((255, 255, 255))  # Fill the screen with black
    for tile in game_level.tiles:
        screen.blit(tile.image, (tile.rect.x + camera_offset, tile.rect.y))  # Draw the level tiles with camera offset
    screen.blit(player.image, (player.rect.x + camera_offset, player.rect.y))  # Draw the player with camera offset
# Refresh screen
    pygame.display.update()

    # Cap the frame rate
    clock.tick(60)