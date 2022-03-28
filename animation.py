import pygame


# definir classe animation
class AnimateSprite(pygame.sprite.Sprite):

    # definir les choses à faire à la création de l'entité
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f"assets/{sprite_name}.png")
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0
        self.images = animation.get(sprite_name)
        self.animation = False

    # definir une mtd pour demarrer l animation
    def start_animation(self):
        self.animation = True

    # definir une methode pour animer le sprite
    def animate(self, loop=False):

        if self.animation:

            # passer à l image suivante
            self.current_image += 1

            # fin de l'animation
            if self.current_image >= len(self.images):
                self.current_image = 0

                # verifier si l'animation n'est pas en mode boucle
                if loop is False:

                    # desactivation animation
                    self.animation = False

            # changer d'animation
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)


# definir fonction pour charger les image du sprite
def load_animation_images(sprite_name):
    # charger les 24 image
    images = []
    # recuperer le chemin pour ce sprite
    path = f"assets/{sprite_name}/{sprite_name}"

    # boucler sur chaque image dans ce dossier
    for num in range(1, 24):
        image_path = path + str(num) + ".png"
        images.append(pygame.image.load(image_path))

    # renvoyer contenu a la liste d image
    return images


# definir un dictionnaire qui va contenir les images chargé de chaque dossiers
#mummy ~~ [.. mummy1.png, ..mummy2.png, ..]
#player : [...player 1.png, player2 ect ]
animation = {
    "mummy": load_animation_images("mummy"),
    "player": load_animation_images("player"),
    "alien": load_animation_images("alien")
}

