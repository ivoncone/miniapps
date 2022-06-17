import pygame
from pygame.locals import *
import sys
import random

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

cardImage = pygame.image.load('cardS/13_of_hearts.png')
window.blit(cardImage, (100, 200))
pygame.display.update()
clock.tick(FRAMES_PER_SECOND)