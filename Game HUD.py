import pygame
import sys

pygame.init()

# taille de la fenêtre
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Menu")

font = pygame.font.SysFont(None, 40)

# variables
coins = 100
player_name = ""
active_input = False

# HUD variables
health = 100
stamina = 80
wave = 1

# boutons
play_button = pygame.Rect(325, 300, 150, 50)
exit_button = pygame.Rect(325, 370, 150, 50)
shop_button = pygame.Rect(325, 440, 150, 50)

# zone de texte
input_box = pygame.Rect(300, 200, 200, 40)

running = True
while running:

    screen.fill((30, 30, 40))

    # ------------------------
    #  HUD ELEMENTS
    # ------------------------

    #  Health Bar
    pygame.draw.rect(screen,(255,255,255),(20,50,200,20),2)
    pygame.draw.rect(screen,(255,0,0),(20,50,health*2,20))
    screen.blit(font.render("Health",True,(255,255,255)),(20,20))

    #  Stamina Bar
    pygame.draw.rect(screen,(255,255,255),(20,100,200,20),2)
    pygame.draw.rect(screen,(0,255,0),(20,100,stamina*2,20))
    screen.blit(font.render("Stamina",True,(255,255,255)),(20,70))

    # Wave
    wave_text = font.render("Wave: " + str(wave), True, (255,255,255))
    screen.blit(wave_text,(600,20))

    # Coins (déplacé à droite)
    coins_text = font.render("Coins: " + str(coins), True, (255,255,0))
    screen.blit(coins_text,(600,60))

    # ------------------------
    # MENU (ton code)
    # ------------------------

    pygame.draw.rect(screen,(255,255,255),input_box,2)
    name_text = font.render(player_name,True,(255,255,255))
    screen.blit(name_text,(input_box.x+5,input_box.y+5))

    label = font.render("Player Name:",True,(255,255,255))
    screen.blit(label,(300,160))

    pygame.draw.rect(screen,(0,200,0),play_button)
    pygame.draw.rect(screen,(200,0,0),exit_button)
    pygame.draw.rect(screen,(0,0,200),shop_button)

    play_text = font.render("PLAY",True,(255,255,255))
    exit_text = font.render("EXIT",True,(255,255,255))
    shop_text = font.render("SHOP",True,(255,255,255))

    screen.blit(play_text,(play_button.x+40,play_button.y+10))
    screen.blit(exit_text,(exit_button.x+40,exit_button.y+10))
    screen.blit(shop_text,(shop_button.x+40,shop_button.y+10))

    # ------------------------
    # EVENTS
    # ------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # clic souris
        if event.type == pygame.MOUSEBUTTONDOWN:

            if input_box.collidepoint(event.pos):
                active_input = True
            else:
                active_input = False

            if play_button.collidepoint(event.pos):
                print("Game Start for:", player_name)

            if shop_button.collidepoint(event.pos):
                print("Shop Opened")

            if exit_button.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

        # clavier (nom)
        if event.type == pygame.KEYDOWN and active_input:

            if event.key == pygame.K_BACKSPACE:
                player_name = player_name[:-1]
            else:
                player_name += event.unicode

        #  contrôle HUD (test)
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_h:
                health = max(0, health - 10)

            if event.key == pygame.K_j:
                health = min(100, health + 10)

            if event.key == pygame.K_s:
                stamina = max(0, stamina - 10)

            if event.key == pygame.K_d:
                stamina = min(100, stamina + 10)

            if event.key == pygame.K_w:
                wave += 1

            if event.key == pygame.K_c:
                coins += 10

    pygame.display.update()

pygame.quit()