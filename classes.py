from constants import *

class Character:
    def __init__(self):
        self.x = screen_width//2
        self.y = 0
        self.vx = 0
        self.vy = max_vy_speed
        self.direction = None


class Platform:
    def __init__(self, type, x, y, width=platform_width,
                 height=platform_height, appearance=None):
        self.type = type
        self.x = x
        self.y = y
        self.width = width
        self.height = height
