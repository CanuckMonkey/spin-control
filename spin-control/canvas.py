import pygame as pg

from settings import *

class Canvas(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((WIDTH, HEIGHT))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rot = 0
        self.painting = False

    def daub(self):
        # Paint a small spot on a mouse click
        pass

    def stroke(self):
        # Paint a line when mouse button held down
        pass

    def paint(self, coords, dt):
        # Generic painting method
        pass

    def update(self, dt):
        if self.painting:
            self.coords = pg.mouse.get_pos
            self.paint(self.coords, dt)
