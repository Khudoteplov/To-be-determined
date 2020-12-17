from classes import *
from math import *
import pygame
from constants import *


def move_hero_left(character: Character):
    """
    Функция поворота и движения налево

    Присваивает соответствующее значение
    аттрибуту vx объекта character из класса Character
    """
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        character.direction = 0  # Направление движения (0 - налево, 1 - направо)
    # vx изменяется в функции move_hero


def move_hero_right(character: Character):
    """
    Функция поворота и движения направо

    Присваивает соответствующее значение
    аттрибуту vx объекта character из класса Character
    """
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        character.direction = 1     # Направление движения (0 - налево, 1 - направо)
    # vx изменяется в функции move_hero


def move_hero(character: Character, dt: int):
    """
    Функция пересчитывает координаты и скорость персонажа

    Аргументы: **character** - персонаж, **dt** - промежуток времени
    """
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        if character.vx < 10:   # 10 - max скорость по оси х
            character.vx += 1
        character.direction = 1     # Направление движения (0 - налево, 1 - направо)

    elif key[pygame.K_LEFT]:
        if character.vx > -10:  # 10 - max скорость по оси y
            character.vx -= 1
        character.direction = 0     # Направление движения (0 - налево, 1 - направо)
    else:
        if character.vx > 0:
            character.vx -= 1
        elif character.vx < 0:
            character.vx += 1
    if character.x > screen_width + 50:   # Правый край + 50
        character.x = -50
    elif character.x < -50:
        character.x = screen_width + 50   # Правый край + 50
    character.x += character.vx
    character.y += character.vy
    character.vy -= 1  # Если увеличить число, будет падать быстрее (гравитация)
    if character.vy > 10:
        character.vy = 10


def check_bounce(character: Character, platform: Platform) -> bool:
    """
    Функция проверяет, не сталкивается ли персонаж с платформой

    Возвращает: **True**, если character столкнулся,
    **False** в противном случае
    """
    if character.vy < 0:
        if platform.y - platform_height <= character.y <= platform.y:
            if abs(platform.x - character.x) <= platform.width:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def bounce(character: Character, platform: Platform):
    """
    Отскок персонажа от платформы
    """
    if check_bounce(character, platform):
        character.vy = 10  # 10 - max скорость по оси y
