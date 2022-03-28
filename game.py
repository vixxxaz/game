import pygame
from sound import SoundManager
from comet_event import CometFallEvent
from monster import Mummy, Alien
from player import Player


# creer une seconde class qui represente game


class Game:

    def __init__(self):
        # definir si jeu a demarrer ou non
        self.is_playing = False
        # generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # generer l event
        self.comet_event = CometFallEvent(self)
        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        # gerer le son
        self.sound_manager = SoundManager()
        # mettre le score à zero
        self.font = pygame.font.Font("assets/police.ttf", 30)
        self.score = 0
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def add_score(self, points=10):
        self.score += points

    def game_over(self):
        # remettre le jeu a zero ,plus de monstre, remettre le joueur a 100
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.comet_event.reset_percent()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.score = 0
        self.sound_manager.play("game_over")

    def update(self, screen):
        # affiche le score sur l'ecran
        score_text = self.font.render(f"score : {self.score}", 1, (22, 39, 248))
        screen.blit(score_text, (50, 50))

        # appliquer image joueur
        screen.blit(self.player.image, self.player.rect)

        #actualiser la barre event
        self.comet_event.update_bar(screen)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # actualiser animation du joueur
        self.player.update_animation()

        # recuperer les projectile du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monstres dans le jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # recuperer  les cometes
        for comet in self.comet_event.all_comets:
            comet.fall()

        # appliquer l ensemble des image de mon groupe de projectile
        self.player.all_projectiles.draw(screen)

        # appliquer mon groupe monster
        self.all_monsters.draw(screen)

        # dessiner ensemble image group comet
        self.comet_event.all_comets.draw(screen)

        # verifier si le joueur souhaite aller à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_rigth()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))
