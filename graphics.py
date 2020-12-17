import pygame
from pygame.draw import *
import numpy as np
from constants import *
from classes import *
pygame.init()

size = 16  


platform_surface = pygame.Surface((platform_width, platform_height))
character_turned_left_surface = pygame.Surface((50, 50))
character_turned_right_surface = pygame.Surface((50, 50))
background_surface = pygame.Surface((screen_width, screen_height))

BROWN = (73, 50, 36)
GREEN = (1, 77, 3)
GREEN_TEA = (208, 240, 192)
YELLOW = (255, 195, 11)

rect(platform_surface, BROWN, (0, 0, platform_width, platform_height))


rect(background_surface, GREEN_TEA, (0, 0, screen_width, screen_height))


ellipse(character_turned_left_surface, YELLOW,
        ((int(25 - size/2), 50 - size*3, size, size * 3))
ellipse(character_turned_left_surface,
 YELLOW, (25 - size, 50 - size*3 + int(size/4), size, size))


    
ellipse(character_turned_left_surface, YELLOW, 
        (int(25 - size/2), 50 - size*3, size, size * 3))
ellipse(character_turned_left_surface,
        YELLOW, (25, 50 - size*3+ int(size/4), size, size))