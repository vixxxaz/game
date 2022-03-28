import pygame
import math
from game import Game

pygame.init()

# definir clock
clock = pygame.time.Clock()
FPS = 100

# generer la fenetre de notre jeu
pygame.display.set_caption("comet fall game")
screen = pygame.display.set_mode((1368, 768))

# importer charger arriere plan du jeu
background = pygame.image.load("assets/bg.jpg")

# importer charger banniere
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 3.5)

# charger notre bouton pour lancer partie
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# charger notre jeu
game = Game()

running = True

# boucle tant que cette condition est vrai
while running:

    # appliquer l arriere plan au jeu
    screen.blit(background, (0, -200))

    # verifier si le jeu a commencer ou non
    if game.is_playing:
        # declencher les instruction de la partie
        game.update(screen)
    # verifier si le jeu n a pas commencer
    else:
        # ajouter ecran bienvenu
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # metre a jour l ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():

        # si l evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
        # detecter si un joueur lache une touch
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si la touche espace est enclenché pour lancer le projectile
            if event.key == pygame.K_SPACE:
               if game.is_playing:
                   game.player.launch_projectile()
               else:
                   # mettre le jeu en mode lancer
                   game.start()
                   # jouer le son du bouton play
                   game.sound_manager.play("click")

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification si la souris et en position avec le button jouer
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode lancer
                game.start()
                # jouer le son du bouton play
                game.sound_manager.play("click")
    # fixer le nombre de fps sur ma clock
    clock.tick(FPS)
