import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, tiles):
        super().__init__()
        
        # Initialize attributes
        self.tiles = tiles
        self.direction = pygame.math.Vector2(0, 0)
        self.velocity = pygame.math.Vector2(0, 0)
        self.gravity = 1
        self.jump_power = -20
        self.on_ground = False
        
        # Load images and initialize animation variables
        self.load_images()
        
        # Set the initial image
        self.image = self.stand_frame
        self.rect = self.image.get_rect(topleft=pos)
    
    def load_images(self):
        # Load new Mario sprites
        self.stand_frame = pygame.image.load('stand.png')
        self.jump_frame = pygame.image.load('jump.png')
        self.walking_frames = [
            pygame.image.load('walk1.png'),
            pygame.image.load('walk2.png'),
            pygame.image.load('walk3.png')
        ]
        self.current_frame = 0
        self.animation_counter = 0
    
    def update(self, tiles):
        self.get_input()
        self.apply_gravity()
        
        # Update position
        self.velocity.x = self.direction.x * 5
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
        
        # Collision detection
        collisions = pygame.sprite.spritecollide(self, tiles, False)
        if collisions:
            self.on_ground = True
            self.velocity.y = 0
            self.rect.y = collisions[0].rect.top - self.rect.height
        else:
            self.on_ground = False
        
        # Update animation
        if self.on_ground:
            if self.direction.x != 0:
                self.animation_counter += 1
                if self.animation_counter % 5 == 0:
                    self.current_frame = (self.current_frame + 1) % len(self.walking_frames)
                self.image = self.walking_frames[self.current_frame]
            else:
                self.image = self.stand_frame
        else:
            self.image = self.jump_frame
        
        self.rect = self.image.get_rect(topleft=self.rect.topleft)

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
