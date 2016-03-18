import pygame as pg
import numpy as np

from settings import *

class Canvas(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((WIDTH, HEIGHT))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.clean_center = self.rect.center
        self.center_vector = np.array(self.clean_center)
        self.rot = 0
        self.painting = False
        pg.draw.circle(self.image, GRAY, self.rect.center, self.rect.h / 2 - 10)
        if TEST:
            pg.draw.circle(self.image, BLUE,
                           (self.rect.centerx + 200,
                            self.rect.centery),
                           20)
        if GUIDES:
            pg.draw.line(self.image, BLACK, self.rect.midtop,
                            (self.rect.centerx, self.rect.top + GUIDE_LENGTH), GUIDE_WIDTH)
            pg.draw.line(self.image, BLACK, self.rect.midbottom,
                            (self.rect.centerx, self.rect.bottom - GUIDE_LENGTH), GUIDE_WIDTH)
            pg.draw.line(self.image, BLACK, self.rect.midleft,
                            (self.rect.left + GUIDE_LENGTH, self.rect.centery), GUIDE_WIDTH)
            pg.draw.line(self.image, BLACK, self.rect.midright,
                            (self.rect.right - GUIDE_LENGTH, self.rect.centery), GUIDE_WIDTH)
        self.clean_image = self.image

    def paint(self, dt):
        # Generic painting method
        vector = np.array(pg.mouse.get_pos())
        coords = vector - self.center_vector
        theta = np.radians(self.rot)
        c, s = np.cos(theta), np.sin(theta)
        R = np.matrix('{} {}; {} {}'.format(c, -s, s, c))
        draw_loc = R.dot(coords) + self.center_vector
        pg.draw.circle(self.clean_image, GREEN,
                       (int(draw_loc[0,0]), int(draw_loc[0,1])), BRUSH_SIZE)

    def update(self, dt):
        self.rot += RPM * dt * 360 / 60000
        self.rot = self.rot % 360
        if self.painting:
            self.paint(dt)
        self.image = pg.transform.rotate(self.clean_image, self.rot)
        self.rect = self.image.get_rect(center=self.clean_center)
