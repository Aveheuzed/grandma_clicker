#!/usr/bin/env python3

import pygame
from pygame.constants import *
from time import sleep

class App :

        def __init__(self, main, fond, gran, pigeon, miette, **dummy_kwargs) :
                self.main = main
                self.fond = fond
                self.gran = gran
                self.pigeon = pigeon
                self.miette = miette
                self.miettes = list()
                self.build()

        def build(self):
                self.main.blit(self.fond,(0,0))
                self.main.blit(self.gran, (0,fond.get_height()-gran.get_height()))
                self.main.blit(self.pigeon, (850,475))
                for miette, t in self.miettes :
                        self.main.blit(miette, (self.x(t), self.y(t)))
                self.miettes = [(surf, n+1) for surf, n in self.miettes if self.x(n+1)<850+self.pigeon.get_width()]#self.fond.get_width()]
##                self.miettes = [(surf, n+1) for surf, n in self.miettes if self.y(n+1) < 475+self.pigeon.get_height()]
                pygame.display.flip()

        def x(self, t):
                v0_cos_alpha = 57
                x0 = self.gran.get_width()
                return v0_cos_alpha*t + x0
        def y(self, t):
                g = 10 # g>0 car repère y vers le bas
                v0_sin_alpha = -57 # v0<0 car //
                y0 = fond.get_height()-gran.get_height()/2
                return 0.5*g*t**2 + v0_sin_alpha*t + y0

        # équation horaire du mouvement :
        # x(t) = cos(alpha)*v0*t + x0
        # y(t) = 0.5g*t**2 + sin(alpha)*v0*t + y0

        def mainloop(self):
                d = 0.1 # one loop lasts 0.1 sec
                while True :
                        for event in pygame.event.get():
                                if event.type == QUIT :
                                        return
                                elif event.type == MOUSEBUTTONDOWN and event.button == 1 :
                                        self.miettes.append((self.miette.copy(), 0))
                        self.build()# temp ; dedent by 2 for the final version
                        try :
                                sleep(d)
                        except ValueError :
                                continue

if __name__ == '__main__':
        main = pygame.display.set_mode((1360, 768))

        fond = pygame.image.load("background.png").convert()
        gran = pygame.image.load("grandma.gif").convert_alpha()
        pigeon = pygame.image.load("pigeon.png").convert_alpha()
        miette = pygame.image.load("miette.png").convert_alpha()

        ##fond : 1980x1080 -> 1360x768
        ##gran : 321x513
        ##pigeon : 1000x1000 -> 250x250
        ##miette : 210x210 -> 20x20

        fond = pygame.transform.scale(fond, (1360,768))
        pigeon = pygame.transform.scale(pigeon, (250,250))
        miette = pygame.transform.scale(miette, (20,20))

        app = App(**locals())
        app.mainloop()
