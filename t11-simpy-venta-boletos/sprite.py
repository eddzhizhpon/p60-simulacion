from os import path

import pygame
from pygame.rect import Rect
from pygame.surface import Surface

import path_name


BLACK = (0, 0, 0)

class Sprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name: str = 'person.png'):
        super().__init__()
        image_path = path.join(path_name.SPRITES_PATH, sprite_name)
        
        self.image: Surface = pygame.image.load(image_path).convert()
        self.image.set_colorkey(BLACK)
        self.rect: Rect = self.image.get_rect()
