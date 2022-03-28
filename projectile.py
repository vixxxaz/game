import pygame
import self as self

# definire la class qui va gerer le projectyle du joueur


class Projectile(pygame.sprite.Sprite):

    # definir le constructeur de la class
    def __init__(self, player):
        super().__init__()
        self.velocity = 8
        self.player = player
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # verifier si le projectile entre en collision avec un monster
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            # supprimer le projectyle
            self.remove()
            # infliger des degat
            monster.damage(self.player.attack)

        # supprimer projectile quand sort de l ecran
        if self.rect.x > 1368:
            self.remove()

