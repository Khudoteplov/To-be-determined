import pygame
from pygame.draw import *
import numpy as np
from  constant.py import *
from classes.py import *
pygame.init()

platform_surface = pygame.Surface((screen_width, screen_height))
character_turned_left_surface = pygame.Surface((screen_width, screen_height)) 
character_turned_right_surface = pygame.Surface((screen_width, screen_height))
background_surface = pygame.Surface((screen_width, screen_height))

BROWN = (73, 50, 36)
GREEN = (1, 77, 3)
GREEN_TEA = (208, 240, 192)
YELLOW = (255, 195, 11)


def platform(COLOR, platform_pos_x, platform_pos_y, x, y, size):
    platform = Platform(type, x, y)
    rect(platform, BROWN, (platform_pos_x, platform_pos_y, platfom_width, platform_height))
    platform_surface.blit(platform, (x, y))

 
def background(x, y, size):
    rect (background_surface, GREEN_TEA, (x, y, size_width, size_height))
    
    
def character_turned_left(charecter_pos_x, charecter_pos_y, x, y, size):
    character_turned_left = Character()
    ellipse(character_turned_left, YELLOW, (charecter_pos_x, charecter_pos_y, size, size*3))
    ellipse(character_turned_left, YELLOW, (charecter_pos_x - int(size/2), charecter_pos_y + int(size/5), size, size))
    character_turned_left_surface.blit(character_turned_left, (x, y))
    
    
def character_turned_right(charecter_pos_x, charecter_pos_y, x, y, size):
    character_turned_right = Character()
    ellipse(character_turned_left, YELLOW, (charecter_pos_x, charecter_pos_y, size, size*3))
    ellipse(character_turned_left, YELLOW, (charecter_pos_x + size - int(size/2), charecter_pos_y + int(size/5), size, size))
    character_turned_right_surface.blit(character_turned_right, (x, y))
    