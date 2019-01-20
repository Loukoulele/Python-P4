import pygame
from pygame.locals import *

def init_map(gamedisplay, color):
    a = 70
    x = 0
    while x <= 6:
        b = 60
        i = 0
        while i <= 5:
            pygame.draw.circle(gamedisplay, color, [a, b], 40)
            b = b + 100
            i += 1
        x += 1
        a = a + 110
