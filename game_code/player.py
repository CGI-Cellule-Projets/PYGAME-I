import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        player_walk_1 = pygame.image.load('player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 5
        self.facing_right = True
        self.max_health = 100
        self.current_health = 80
    def get_input(self):
        keys = pygame.key.get_pressed()

        # up and down

        if keys[pygame.K_UP]: self.direction.y = -1
        elif keys[pygame.K_DOWN]: self.direction.y = 1
        else: self.direction.y = 0

        # Left and Right

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0
    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        # Updates exact float position
        self.pos.x += self.direction.x * self.speed
        self.rect.centerx = round(self.pos.x)
        self.pos.y += self.direction.y * self.speed
        self.rect.centery = round(self.pos.y)

    def animate(self):
        if self.direction.magnitude() != 0:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
        else:
            self.player_index = 0
        current_image = self.player_walk[int(self.player_index)]
        if not self.facing_right:
            self.image = pygame.transform.flip(current_image, True, False)
        else:
            self.image = current_image

    def draw_health(self, display_surface, camera_offset):
        bar_width = 50
        bar_height = 6

        x = self.rect.centerx - (bar_width // 2) - camera_offset.x
        y = self.rect.bottom + 5 - camera_offset.y

        health_ratio = self.current_health / self.max_health
        current_bar_height = bar_width * health_ratio

        bg_rect = pygame.Rect(x, y, bar_width, bar_height)
        health_rect = pygame.Rect(x, y, current_bar_height, bar_height)

        pygame.draw.rect(display_surface, 'red', bg_rect)
        pygame.draw.rect(display_surface, '#32a852', health_rect)
        pygame.draw.rect(display_surface, 'white', bg_rect, 1)

    def update(self):
        self.get_input()
        self.move()
        self.animate()
