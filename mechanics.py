from classes import *
from math import *


def move_hero_left(character: Character):
    """
    Функция поворота и движения налево

    Присваивает соответствующее значение
    аттрибуту vx объекта character из класса Character
    """
    key = pygame.key.get_pressed()
    if key[K_LEFT]:
        character.direction = 0     # Направление движения (0 - налево, 1 - направо)
    # vx изменяется в функции move_hero


def move_hero_right(character: Character):
    """
    Функция поворота и движения направо

    Присваивает соответствующее значение
    аттрибуту vx объекта character из класса Character
    """
    key = pygame.key.get_pressed()
    if key[K_RIGHT]:
        character.direction = 1     # Направление движения (0 - налево, 1 - направо)
    # vx изменяется в функции move_hero


def move_hero(character: Character):
    """
    Функция пересчитывает координаты и скорость персонажа
    """
    key = pygame.key.get_pressed()
    if key[K_RIGHT]:
        if character.vx < 10:   # 10 - max скорость по оси х
            character.vx += 1
        character.direction = 1     # Направление движения (0 - налево, 1 - направо)

    elif key[K_LEFT]:
        if character.vx > -10:  # 10 - max скорость по оси y
            character.vx -= 1
        character.direction = 0     # Направление движения (0 - налево, 1 - направо)
    else:
        if character.vx > 0:
            character.vx -= 1
        elif character.vx < 0:
            character.vx += 1
    if character.x > 850:   # Правый край + 50
        character.x = -50
    elif character.x < -50:
        character.x = 850   # Правый край + 50
    character.x += character.vx
    character.y += character.vy


def check_bounce(character: Character, platform: Platform) -> bool:
    """
    Функция проверяет, не сталкивается ли персонаж с платформой

    Возвращает: **True**, если character столкнулся,
    **False** в противном случае
    """
    for v in platform:
        if v[1] == character.y:
            if (character.x - 15) <= v[0] <= (character.x + 15):    # 15 - ширина платформы пополам
                return True
            else:
                return False
        else:
            return False


def bounce(character: Character, platform: Platform):
    """
    Отскок персонажа от платформы
    """
    if not check_bounce(character, platform):
        character.vy -= 1   # Если увеличить число, будет падать быстрее (гравитация)
    else:
        if abs(character.vy) < 10:  # 10 - max скорость по оси y
            character.vy = 10  # 10 - max скорость по оси y
        else:
            character.vy = abs(character.vy)    # упругое столкновение
