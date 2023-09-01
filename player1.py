import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, tiles):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill((255, 0, 0))  # Set player color to red (RGB tuple)
        self.rect = self.image.get_rect(topleft=pos)
        self.tiles = tiles  # Reference to the tiles in the level
        self.direction = pygame.math.Vector2(0, 0)
        self.velocity = pygame.math.Vector2(0, 0)
        self.gravity = 1
        self.jump_power = -20
        self.on_ground = False
        self.load_images()

    def load_images(self):
        self.walking_frames = [
            pygame.image.load('mario_walk_frame_1.png'),
            pygame.image.load('mario_walk_frame_2.png'),
            pygame.image.load('mario_walk_frame_3.png')
        ]
        self.current_frame = 0
        self.animation_counter = 0  # Initialize animation counter in __init__


    def update(self, tiles):
        self.update_logic(tiles)
        
        self.animation_counter += 1  # Increment the counter each time update is called
        if self.animation_counter % 5 == 0:  # Change frame every 5 game loop iterations
            self.current_frame = (self.current_frame + 1) % len(self.walking_frames)
            self.image = self.walking_frames[self.current_frame]


    def update_logic(self, tiles):  # Added tiles parameter for collision detection
        self.get_input()
        self.apply_gravity()

        self.velocity.x = self.direction.x * 5
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        # Collision with the ground (assuming tiles is a sprite group containing tiles)
        collisions = pygame.sprite.spritecollide(self, tiles, False)
        if collisions:
            self.on_ground = True
            self.velocity.y = 0
            self.rect.y = collisions[0].rect.top - self.rect.height

    def apply_gravity(self):
        self.velocity.y += self.gravity
        if self.velocity.y > 10:
            self.velocity.y = 10

    def jump(self):
        if self.on_ground:
            self.velocity.y = self.jump_power
            self.on_ground = False

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()
