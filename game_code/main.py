import pygame
import random
from pytmx.util_pygame import load_pygame
from player import Player
from camera import CameraGroup
from enemy import Enemy
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)

def spawn_enemy(player_target, camera_group):
    random_x = random.randint(0, 2000)
    random_y = random.randint(0, 2000)
    speed = random.choice([2, 3, 4])
    Enemy((random_x, random_y), speed, player_target, camera_group)



pygame.init()
screen = pygame.display.set_mode((1280, 720))
tmx_data = load_pygame('C:\\tmx\\game_map.tmx')
sprite_group = pygame.sprite.Group()

camera_group = CameraGroup()
ENEMY_SPAWN_EVENT = pygame.event.custom_type()
pygame.time.set_timer(ENEMY_SPAWN_EVENT, 3000)
# cycle through all layers
for layer in tmx_data.visible_layers:
    if hasattr(layer, 'data'):
        for x,y, surf in layer.tiles():
            pos = (x * tmx_data.tilewidth, y * tmx_data.tileheight)
            Tile(pos=pos, surf=surf, groups=camera_group)

# cycle through objects
for obj in tmx_data.objects:
     pos = obj.x, obj.y
     if obj.type in 'Vegetation':
        Tile(pos=pos, surf=obj.image, groups=camera_group)

# Create the player

player = Player((400, 400), camera_group)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == ENEMY_SPAWN_EVENT:
            spawn_enemy(player, camera_group)

    screen.fill('black')
    camera_group.update()
    camera_group.custom_draw(player)
    pygame.display.update()
    pygame.time.Clock().tick(60)
