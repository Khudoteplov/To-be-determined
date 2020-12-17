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
        if check > 600:
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
        new_platform = Platform(type=None, x=x, y=h)
        platforms.append(new_platform)
        h -= 50
    return platforms
