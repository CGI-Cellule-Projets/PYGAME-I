import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, speed,  player_target, groups):
        super().__init__(groups)
        enemy_walk_1 = pygame.image.load('snail1.png').convert_alpha()
        enemy_walk_2 = pygame.image.load('snail2.png').convert_alpha()
        self.enemy_walk = [enemy_walk_1, enemy_walk_2]
        self.enemy_index = 0
        self.image = self.enemy_walk[self.enemy_index]
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = speed
        self.target = player_target

    def move_towards_player(self):
        # get player position
        player_pos = pygame.math.Vector2(self.target.rect.center)
        direction_vector = player_pos - self.pos
        distance = direction_vector.magnitude()
        if distance > 0:
            direction_vector = direction_vector.normalize()
            movement = direction_vector * self.speed
            self.pos += movement
            self.rect.center = (round(self.pos.x), round(self.pos.y))

    def enemy_animation(self):
        # 1. Cycle through the animation frames
        self.enemy_index += 0.05
        if self.enemy_index >= len(self.enemy_walk):
            self.enemy_index = 0
        current_image = self.enemy_walk[int(self.enemy_index)]
        # 2. Figure out which way the snail is walking so we can flip it
        # If the player's X is less than the snail's X, the player is to the left!
        if self.target.rect.centerx < self.rect.centerx:
            self.image = pygame.transform.flip(current_image, True, False)
        else:
            self.image = current_image

    def update(self):
        self.move_towards_player()
        self.enemy_animation()
