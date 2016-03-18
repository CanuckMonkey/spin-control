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
                                              self.rect.centery),
                           20)
        self.clean_image = self.image

    def paint(self, coords, dt):
        # Generic painting method
        draw_loc = coords.rotate(-self.rot)
        pg.draw.circle(self.clean_image, GREEN, draw_loc, 15)

    def update(self, dt):
        self.rot += RPM * dt * 360 / 60000
        if self.painting:
            coords = pg.mouse.get_pos
            self.coords = pg.math.Vector2(coords)
            self.paint(self.coords, dt)
        self.image = pg.transform.rotate(self.clean_image, self.rot)
        self.rect = self.image.get_rect(center=self.clean_center)
