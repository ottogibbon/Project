import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, tiles):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.tiles = tiles
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.velocity = pygame.math.Vector2(0, 0)
        self.gravity = 1
        self.jump_power = -20  
        self.on_ground = False

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

    def update(self):
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
            self.rect.y = collisions[0].rect.top

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)
