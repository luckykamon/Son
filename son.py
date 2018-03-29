import time
import pygame
from pygame.locals import *

pygame.init()


son = pygame.mixer.Sound("tryo.aiff")
son.play()
time.sleep(5)
pygame.mixer.pause()
time.sleep(5)
pygame.mixer.unpause()
time.sleep(5)
pygame.mixer.stop()

