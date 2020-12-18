import pygame


class Button:

    def __init__(self, x, y, width, height, text='',
                 color=(255, 255, 255), text_color=(0, 0, 0)):
        self.x  = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.text_color = text_color
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill(self.color)
        self.surface.blit(self.font.render(self.text, True, self.text_color),
                          (0,0))

    def pressed(self, mouse):
        if ((mouse[0] > self.x) and
                (mouse[1] > self.y) and
                (mouse[0] < (self.x + self.width)) and
                (mouse[1] < (self.y + self.height))):
            return True
        else:
            return False


class InputBox:
    active_color = (250, 250, 0)
    inactive_color = (255, 255, 255)

    def __init__(self, x, y, w, h,
                 text='', color=inactive_color, text_color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.text_surface = self.font.render(self.text, True, self.text_color)
        self.active = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def handle(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:

            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            if self.active:
                self.color = InputBox.active_color
            else:
                self.color = InputBox.inactive_color
        if (event.type == pygame.KEYDOWN) and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                self.active = False
                self.color = InputBox.inactive_color
            else:
                if len(self.text) < 7:
                    self.text += event.unicode

            self.text_surface = self.font.render(self.text,
                                                 True, self.text_color)

    def draw_input_box(self, screen):
        """
        Рисует на экране **screen**
        """
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text_surface, (self.x + 5, self.y + 5))


