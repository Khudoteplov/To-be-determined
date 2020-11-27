import pygame

pygame.init()

pygame.display.init()

screen = pygame.display.set_mode((400, 500))

finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()