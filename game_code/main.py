import pygame
from pytmx.util_pygame import load_pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)


pygame.init()
screen = pygame.display.set_mode((1280, 720))
tmx_data = load_pygame('C:\\tmx\\game_map.tmx')
sprite_group = pygame.sprite.Group()

# cycle through all layers
for layer in tmx_data.visible_layers:
    if hasattr(layer, 'data'):
        for x,y, surf in layer.tiles():
            pos = (x * tmx_data.tilewidth, y * tmx_data.tileheight)
            Tile(pos=pos, surf=surf, groups=sprite_group)

# cycle through objects
for obj in tmx_data.objects:
     pos = obj.x, obj.y
     if obj.type in 'Vegetation':
        Tile(pos=pos, surf=obj.image, groups=sprite_group)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill('black')
    sprite_group.draw(screen)
    pygame.display.update()
