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

# Function to draw a button on the screen
def draw_button(screen, msg, x, y, w, h, ic, ac, font):
    # Get mouse position and click status
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    # Check if mouse is over the button
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        # If button is clicked, return True
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))
    
    # Render text on the button
    text_surf, text_rect = text_objects(msg, font)
    text_rect.center = (x + w // 2, y + h // 2)
    screen.blit(text_surf, text_rect)
    return False

# Function to create text objects, useful for rendering text
def text_objects(text, font):
    text_surface = font.render(text, True, (0, 0, 0))
    return text_surface, text_surface.get_rect()

# Menu loop
game_exit = False
# Use a built-in Pygame font with size 20 for a retro look
retro_font = pygame.font.Font('freesansbold.ttf', 20)
while not game_exit:
    for event in pygame.event.get():
        # Check for quit events
        if event.type == pygame.QUIT:
            game_exit = True
            pygame.quit()
            quit()
    
    # Fill the screen with a retro background color (grayish)
    screen.fill((192, 192, 192))
    
    # Render the title text
    large_text = pygame.font.Font('freesansbold.ttf', 50)
    TextSurf, TextRect = text_objects('Remastered Mario by Otto', large_text)
    TextRect.center = ((screen_width // 2), (screen_height // 4))
    screen.blit(TextSurf, TextRect)
    
    # Draw the 'START' button and check for clicks
    if draw_button(screen, 'START', 150, 450, 100, 50, (0, 200, 0), (0, 255, 0), retro_font):
        game_exit = True
    
    # Update the screen
    pygame.display.update()
    clock.tick(15)
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
    screen.fill((0, 0, 0))  # Fill the screen with black
    for tile in game_level.tiles:
        screen.blit(tile.image, (tile.rect.x + camera_offset, tile.rect.y))  # Draw the level tiles with camera offset
    screen.blit(player.image, (player.rect.x + camera_offset, player.rect.y))  # Draw the player with camera offset
# Refresh screen
    pygame.display.update()

    # Cap the frame rate
    clock.tick(60)