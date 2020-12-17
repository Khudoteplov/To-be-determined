import pygame
from classes import *
from mechanics import *
from graphics import *
from constants import *
from platform_generator import *
scroll_speed = 20


def update_screen(screen1: pygame.Surface,
                  height1, view_height1, character1, platforms1):
    """
    Функция обновляет картинку на экране

    Аргумеенты: **screen1** - поверхность экрана
    **height1** - высота, до которой дошел игрок
    **view_height1** - выстота наблюдателя
    **character1** - персонаж
    **platforms1** - список объектов класса Platform
    """
    screen1.blit(background_surface, (0, 0))  # отрисовка фона
    for platform1 in platforms1:
        screen1.blit(platform_surface,
                     (platform1.x - platform1.width // 2,
                      -platform1.y + view_height1 + screen_height))
    screen.blit(character_turned_right_surface,
                (character1.x - 25,
                 -character.y + view_height1 + screen_height - 50))
    if view_height1 < height:
        view_height1 = min(view_height1 + scroll_speed, height1)

    return view_height1


pygame.init()

pygame.display.init()

screen = pygame.display.set_mode((screen_width, screen_height))

finished = False

character = Character()

clock = pygame.time.Clock()

height = 0
point_of_view_height = 0
platforms = []
top_generated_level = 10 * screen_height
platforms += generate_platforms(0, 10 * screen_height)

while not finished:
    move_hero(character, 1)
    for platform in platforms:
        if check_bounce(character, platform):
            bounce(character, platform)
            height = platform.y
            if (top_generated_level - height) < screen_height:
                generate_platforms(top_generated_level,
                                   top_generated_level + 5 * screen_height)
                top_generated_level += 5 * screen_height
            break
    remove_passed_platforms(point_of_view_height, platforms)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_hero_left(character)
            elif event.key == pygame.K_RIGHT:
                move_hero_right(character)
    point_of_view_height = update_screen(screen, height, point_of_view_height,
                                         character, platforms)
    clock.tick(FPS)

pygame.quit()
