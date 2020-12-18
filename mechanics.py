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
        if character.vx < max_vy_speed:   # 10 - max скорость по оси х
            character.vx += 1
        character.direction = 1     # Направление движения (0 - налево, 1 - направо)

    elif key[pygame.K_LEFT]:
        if character.vx > -max_vy_speed:  # 10 - max скорость по оси y
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
    if character.vy > max_vy_speed:
        character.vy -= 1


def check_bounce(character: Character, platform: Platform) -> bool:
    """
    Функция проверяет, не сталкивается ли персонаж с платформой

    Возвращает: **True**, если character столкнулся,
    **False** в противном случае
    """
    if character.vy//2 <= character.y - platform.y <= -character.vy//2:
        if (platform.x - platform.width / 2) <= character.x <= (platform.x + platform.width / 2):
            return True
        else:
            return False
    else:
        return False


def bounce(character: Character, platform: Platform):
    """
    Отскок персонажа от платформы
    """
    if check_bounce(character, platform):
        character.vy = max_vy_speed  # 10 - max скорость по оси y


def sticking(character: Character, platform: Platform):
    """
    Прилипание персонажа к липким платформам
    """
    if check_bounce(character, platform):
        if platform.type == 1:
            character.vy = 0


def destroy(character: Character, platform: Platform):
    """
    Разрушение платформ
    """
    if check_bounce(character, platform):
        if platform.type == 2:
            character.vy *= -1
            delete(platform)


def delete(platform: Platform):
    # Не уверен, что так можно сделать
    pygame.delete(platform)


def check_spring(character: Character, spring: Spring) -> bool:
    """
    Функция проверяет, не сталкивается ли персонаж с пружиной
    Возвращает: **True**, если character столкнулся,
    **False** в противном случае
    """
    if character.vy//2 <= character.y - spring.y <= -character.vy//2:
        if (spring.x - spring.width / 2) <= character.x <= (spring.x + spring.width / 2):
            return True
        else:
            return False
    else:
        return False


def bounce_on_spring(character: Character, spring: Spring):
    """
    Отскок персонажа от пружины
    """
    if check_spring(character, spring):
        character.vy = 2 * max_vy_speed  # 10 - max скорость по оси y
