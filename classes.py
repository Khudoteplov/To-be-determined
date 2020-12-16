class Character:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0


class Platform:
    def __init__(self, type, x, y,
                 platform_width=50, platform_height=5, appearance=None):
        self.type = type
        self.x = x
        self.y = y
        self.width = platform_width
        self.height = platform_height
