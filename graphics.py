import pygame
from pygame.draw import *
import numpy as np
pygame.init()

platform_surface = pygame.Surface((100, 100))
character_turned_left_surface = pygame.Surface((50, 50)) 
character_turned_right_surface = pygame.Surface((50, 50))
background_surface = pygame.Surface((700, 500))

BROWN = (73, 50, 36)
GREEN = (1, 77, 3)
GREEN_TEA = (208, 240, 192)
YELLOW = (255, 195, 11)

def platform(Surface, COLOR, x, y, size):
    rect(Surface, COLOR, (x, y, size*8, size))

 
def background(Surface, x, y, size):
    rect (Surface, GREEN_TEA, (x, y, size_width, size_height))
    
    
def character_turned_left(Surface, x, y, size):
    ellipse(Surface, YELLOW, (x, y, size, size*3))
    ellipse(Surface, YELLOW, (x-int(size/2), y+int(size/5), size, size))
    #not the final version
    

def character_turned_right(Surface, x, y, size):
    ellipse(Surface, YELLOW, (x, y, size, size*3))
    ellipse(Surface, YELLOW, (x+size-int(size/2), y+int(size/5), size, size))
    #not the final version
  