import pygame
from pytmx.util_pygame import load_pygame
from player import Player
from camera import CameraGroup
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)


pygame.init()
screen = pygame.display.set_mode((1280, 720))
tmx_data = load_pygame('C:\\tmx\\game_map.tmx')
sprite_group = pygame.sprite.Group()

camera_group = CameraGroup()
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
    screen.fill('black')
    camera_group.update()
    camera_group.custom_draw(player)
    pygame.display.update()
    pygame.time.Clock().tick(60)
