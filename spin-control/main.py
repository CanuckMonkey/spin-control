"""
Original:
https://www.reddit.com/r/pygame/comments/4aq3or/challenge_spin_class/

Spin Class
This challenge focuses on creating a paint program with a different spin -
the drawing canvas spins as the user is drawing. Thanks to my niece for the
idea on this one; she was pretty excited to show me the app like this that
she got for her tablet. You're on your own, there is no code provided for
this challenge and, thus, no github repo. Also, sorry it's taken so long to
put a new challenge up, it's been a hectic couple of weeks.

Challenge
Create an app that allows the user to draw on a spinning canvas. The final
results should look something like this:
http://applenapps.com/wp-content/uploads/2011/06/spinart_studio6.jpg.

Achievements
aRtPM: allow the user to adjust the rotation speed and direction of the canvas
Color Me Amused: allow the user to select a different color or colors to draw with
Brushed Asize: allow the user to select different brush sizes or patterns
For Posterity: allow the user to save the image they've created

Good luck, have fun and feel free to ask for help if you need it!
"""

import sys
import os

import pygame as pg
import random

from settings import *
from canvas import Canvas

class Game:
    # Core game actions and components.
    def __init__(self):
        # Initialize game window, etc.
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # Start a new game
        self.all_sprites = pg.sprite.Group()
        self.canvas = Canvas()
        self.all_sprites.add(self.canvas)
        self.playing = True
        #self.painting = False
        self.run()


    def run(self):
        # Game loop
        while self.playing:
            dt = self.clock.tick(FPS)
            self.events()
            self.update(dt)
            self.draw()

    def update(self, dt):
        # Game loop - update
        for sprite in self.all_sprites:
            sprite.update(dt)

    def events(self):
        # Game loop - process input (events)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.canvas.painting = True
            elif event.type == pg.MOUSEBUTTONUP:
                self.canvas.painting = False

    def draw(self):
        #Game loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def show_start_screen(self):
        # Display the startup screen
        pass

    def show_go_screen(self):
        # Display the game over screen
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
sys.exit(0)
