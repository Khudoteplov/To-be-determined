import pygame
from classes import *
from mechanics import *
from graphics import *
from constants import *
from platform_generator import *
from buttons_textboxes import *


pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)  # шрифт


def update_screen(screen1: pygame.Surface,
                  height1, view_height1, character1, platforms1, springs1):
    """
    Функция обновляет картинку на экране

    Аргумеенты: **screen1** - поверхность экрана
    **height1** - высота, до которой дошел игрок
    **view_height1** - выстота наблюдателя
    **character1** - персонаж
    **platforms1** - список объектов класса Platform

    Возвращает высоту наблюдателя
    """
    screen1.fill((255, 255, 255))
    screen1.blit(background_surface, (0, 0))  # отрисовка фона

    for platform1 in platforms1:
        screen1.blit(platform_surface,
                     (platform1.x - platform1.width // 2,
                      -platform1.y + view_height1 + screen_height))
    for spring1 in springs1:

        screen.blit(spring_coiled_surface, (spring1.x - 25,
                    -spring1.y + view_height1 + screen_height - 50))

    if character1.direction == 0:
        screen.blit(character_turned_left_surface,
                    (character1.x - 25,
                     -character1.y + view_height1 + screen_height - 50))
    else:
        screen.blit(character_turned_right_surface,
                    (character1.x - 25,
                     -character1.y + view_height1 + screen_height - 50))

    if view_height1 < height1:
        view_height1 = min(view_height1 + scroll_speed, height1 - 10)
    return view_height1


def display_score(score):
    score_font = pygame.font.SysFont('Comic Sans MS', 20)
    score_text_surface = score_font.render('Score: ' + str(score), True, (200, 0, 0))
    screen.blit(score_text_surface, (0, 0))


def view_leaderboard(screen1):
    screen.blit(menu_background_surface, (0, 0))
    leaderboard = open('leaderboard.txt', 'r')
    results = []
    fnt = pygame.font.SysFont('Comic Sans MS', 30)
    for line in leaderboard:
        if len(line) > 2:
            results.append(line.split(' '))

    y = 50
    for i in range(min(len(results), 5)):
        txt_surface = fnt.render(results[i][0] + '  ' + results[i][1], True, (0, 0, 0))
        screen1.blit(txt_surface, (100, y))
        y += 100
    leaderboard.close()
    menu_button = Button(screen_width // 2 - 40, screen_height - 100,
                         80, 50, text='Menu')
    screen1.blit(menu_button.surface, (menu_button.x, menu_button.y))
    pygame.display.update()
    finished = False

    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'QUIT'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if menu_button.pressed(event.pos):
                    return 0

    pygame.display.update()


def submit_result(name, result):
    leaderboard = open('leaderboard.txt', 'r')
    results = []
    fnt = pygame.font.SysFont('Comic Sans MS', 30)
    for line in leaderboard:
        if len(line) > 2:
            results.append(line.split(' '))
    leaderboard.close()

    new_leaderboard = open('leaderboard.txt', 'w')
    printed = False
    for result1 in results:
        if (int(result1[1]) >= result) or printed:
            print('{} {}'.format(result1[0], result1[1]), file=new_leaderboard)
        elif not printed:
            print('{} {}'.format(name, str(result)), file=new_leaderboard)
            printed = True
            print('{} {}'.format(result1[0], result1[1]), file=new_leaderboard)
    new_leaderboard.close()





def menu(controller):
    pygame.init()
    if controller == 'QUIT':
        pygame.quit()
    else:
        screen.blit(menu_background_surface, (0, 0))
        new_game_button = Button(screen_width//2 - 75, screen_height//2 - 100,
                                 150, 50, text='New game')

        quit_button = Button(screen_width//2 -50, screen_height//2,
                             100, 50, 'QUIT')

        leaderboard_button = Button(screen_width//2 - 90,
                                    screen_height//2 + 100, 180, 50,
                                    'Leaderboard')
        screen.blit(new_game_button.surface,
                    (new_game_button.x, new_game_button.y))
        screen.blit(quit_button.surface, (quit_button.x, quit_button.y))
        screen.blit(leaderboard_button.surface,
                    (leaderboard_button.x, leaderboard_button.y))
        pygame.display.update()

        finished1 = False
        pygame.init()
        while not finished1:
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if new_game_button.pressed(event.pos):
                        menu(game_over(game()))
                        return 0
                    elif quit_button.pressed(event.pos):
                        menu('QUIT')
                        return 'QUIT'
                    elif leaderboard_button.pressed(event.pos):
                        menu(view_leaderboard(screen))
                        return 0
                if event.type == pygame.QUIT:
                    menu('QUIT')
                    return 'QUIT'


def game_over(score):
    if score == 'QUIT':
        return 'QUIT'
    else:
        screen.blit(menu_background_surface, (0, 0))
        text_surface = my_font.render('Game over!',
                                      True, (200, 0, 0))
        screen.blit(text_surface,
                    (screen_width//2 - 70, screen_height//2 - 80))
        text_surface = my_font.render('Your score: ' + str(score),
                                      True, (200, 0, 0))
        screen.blit(text_surface, (screen_width//2 - 120, screen_height//2))

        menu_button = Button(screen_width // 2 - 40, screen_height // 2 + 100,
                             80, 50, text='Menu')

        submit = Button(screen_width//2 + 75, screen_height//2 + 200,
                        100, 50, text='Submit')
        screen.blit(submit.surface, (submit.x, submit.y))
        screen.blit(menu_button.surface, (menu_button.x, menu_button.y))
        name_input_box = InputBox(screen_width//2 - 150, screen_height//2 + 200,
                                  200, 50, text='Name')
        name_input_box.draw_input_box(screen)
        pygame.display.update()

        finished2 = False
        while not finished2:
            for event in pygame.event.get():
                name_input_box.handle(event)
                if event.type == pygame.QUIT:
                    return 'QUIT'
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if menu_button.pressed(event.pos):
                        return 0
                    elif submit.pressed(event.pos):
                        submit_result(name=name_input_box.text, result=score)

            name_input_box.draw_input_box(screen)
            pygame.display.update()


pygame.init()

pygame.display.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


def game():
    """
    Функция, запускающая игру, возвращает достигнутую высоту
    """
    finished = False
    character = Character()
    height = 0
    point_of_view_height = -10
    platforms = []
    springs = []
    bottom_platform = Platform(None, screen_width // 2, 0, screen_width * 2)
    platforms.append(bottom_platform)
    top_generated_level = 2 * screen_height
    platforms.extend(generate_platforms(0, 2 * screen_height))
    update_screen(screen, height, point_of_view_height,
                  character, platforms, springs)

    while not finished:
        point_of_view_height = update_screen(screen, height,
                                             point_of_view_height,
                                             character, platforms, springs)
        display_score(height)
        pygame.display.update()
        clock.tick(FPS)
        move_hero(character, 1)
        for spring in springs:
            if check_spring(character, spring):
                bounce_on_spring(character, spring)
                height = spring.y
        for platform in platforms:
            if check_bounce(character, platform):
                bounce(character, platform)
                height = platform.y
                if (top_generated_level - height) < 2 * screen_height:
                    new_platforms = generate_platforms(top_generated_level,
                                                       top_generated_level +
                                                        5 * screen_height)
                    for platform1 in new_platforms:
                        springs.extend(generate_springs(platform1))
                    platforms.extend(new_platforms)
                    top_generated_level += 5 * screen_height
                break
        remove_passed_platforms(point_of_view_height, platforms)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'QUIT'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_hero_left(character)
                elif event.key == pygame.K_RIGHT:
                    move_hero_right(character)
        if character.y < point_of_view_height:
            return height
    return height


menu(game_over(game()))

pygame.quit()