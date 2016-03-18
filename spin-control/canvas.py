import pygame as pg

from settings import *

class Canvas(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((WIDTH, HEIGHT))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.clean_center = self.rect.center
        self.rot = 0
        self.painting = False
        pg.draw.circle(self.image, GRAY, self.rect.center, self.rect.h / 2 - 10)
        if TEST:
            pg.draw.circle(self.image, BLUE, (self.rect.centerx + 200,
                                              self.rect.centery), 20)
        self.clean_image = self.image

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
        self.rot += RPM * dt * 360 / 60000
        if self.painting:
            self.coords = pg.math.Vector2(pg.mouse.get_pos)
            self.paint(self.coords, dt)
        self.image = pg.transform.rotate(self.clean_image, self.rot)
        self.rect = self.image.get_rect(center=self.clean_center)
