from classes import *
import random


def remove_passed_platforms(height: int, platforms: list):
    """
    Функция, удаляющая оставленные позади платформы

    Аргументы: **height** - высота, на которой находится персонаж
    **platforms** - список платформ
    """
    for platform in platforms:
        check = platform.y - height
        if check < - screen_height:
            platforms.remove(platform)


def generate_platforms(bottom_height: int, top_height: int) -> list:
    """
    Функция, генерирующая платформы на высоте от **bottom_height**
    до **top_height**

    Возвращает список сгенерированных платформ
    """
    h = top_height
    platforms = []
    while h > bottom_height:
        x = random.randint(0, screen_width)
        p = random.randint(0, 100)
        if p <= 800:
            typ = 0    # Обычная платформа
        elif p <= 900:
            typ = 1    # Липкая платформа
        else:
            typ = 2    # Разрушающаяся платформа
        new_platform = Platform(type=typ, x=x, y=h)
        platforms.append(new_platform)
        h -= 50
    return platforms


def generate_springs(platform: Platform) -> list:
    p = random.randint(0, 100)
    springs = []
    if p <= 5:
        x = random.randint(platform.x - platform_width//2, platform.x + platform_width//2)
        y = platform.y
        new_spring = Spring(x, y)
        springs.append(new_spring)
    return springs
