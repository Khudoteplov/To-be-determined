from classes import *


def remove_passed_platforms(height: int, platforms: list):
    """
    Функция, удаляющая оставленные позади платформы

    Аргументы: **height** - высота, на которой находится персонаж
    **platforms** - список платформ
    """
    for p in range(len(platforms)):
        check = platforms[p][1] - height
        if check > 600:
            platforms.append([random.randint(0, 700), platforms[-1][1] - 50, 0])
            platforms.pop(p)


def generate_platforms(bottom_height: int, top_height: int) -> list:
    """
    Функция, генерирующая платформы на высоте от **bottom_height**
    до **top_height**

    Возвращает список сгенерированных платформ
    """
    h = top_height
    platforms = []
    while h > bottom_height:
        x = random.randint(0, 700)
        platforms.append([x, h, 0])
        h -= 50
        return platforms
