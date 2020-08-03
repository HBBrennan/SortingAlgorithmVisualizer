import pygame
import math
import random
from constants import *
from settings import Settings

def draw_text(win, header_text, small_text, color):
    win.blit(header_text.render('Algorithm', False, color), (950, 20))
    win.blit(small_text.render('Bubble Sort', False, color), (870, 76))
    win.blit(small_text.render('Selection Sort', False, color), (870, 106))
    win.blit(small_text.render('Insertion Sort', False, color), (870, 136))
    win.blit(small_text.render('Bucket Sort', False, color), (1070, 76))
    win.blit(small_text.render('Merge Sort', False, color), (1070, 106))
    win.blit(small_text.render('Quick Sort', False, color), (1070, 136))

    win.blit(header_text.render('Speed', False, color), (55, 26))
    win.blit(small_text.render('Fast', False, color), (110, 77))
    win.blit(small_text.render('Medium', False, color), (110, 107))
    win.blit(small_text.render('Slow', False, color), (110, 137))

    win.blit(header_text.render('Size', False, color), (265, 26))
    win.blit(small_text.render('Large', False, color), (310, 77))
    win.blit(small_text.render('Medium', False, color), (310, 107))
    win.blit(small_text.render('Small', False, color), (310, 137))


def draw_buttons(win, button_position, active_color, inactive_color, text_color, text_font, mouse_x, mouse_y):
    for button in button_position:
        color = inactive_color
        if over_button(button, mouse_x, mouse_y):
            color = active_color

        pygame.draw.rect(win, color, button)

    win.blit(text_font.render('Sort', False, text_color), (610, 26))
    win.blit(text_font.render('Reset', False, text_color), (600, 106))


def draw_circles(win, color, circle_position, settings):
    for num in range(len(circle_position)):
        pygame.draw.circle(win, color, circle_position[num], 12, 3)
        pygame.draw.circle(win, (128, 128, 128), circle_position[num], 7)

    pygame.draw.circle(win, color, (circle_position[settings.algorithm.value][0], circle_position[settings.algorithm.value][1]), 5)

    pygame.draw.circle(win, color, (circle_position[settings.sorting_speed.value + 6][0],
                                    circle_position[settings.sorting_speed.value + 6][1]), 5)

    if settings.array_size.value == 80:
        pygame.draw.circle(win, color, (circle_position[9][0], circle_position[9][1]), 5)
    elif settings.array_size.value == 40:
        pygame.draw.circle(win, color, (circle_position[10][0], circle_position[10][1]), 5)
    elif settings.array_size.value == 20:
        pygame.draw.circle(win, color, (circle_position[11][0], circle_position[11][1]), 5)

    pygame.display.update()


def mark_circles(mouse_x, mouse_y, settings, circle_position):
    for num in range(3):  # speed buttons
        if check_distance(mouse_x, mouse_y, int(circle_position[num + 6][0]), int(circle_position[num + 6][1])) < 8:
            if num + 6 == 6:
                settings.sorting_speed = SortingSpeed.FAST
            if num + 6 == 7:
                settings.sorting_speed = SortingSpeed.MEDIUM
            if num + 6 == 8:
                settings.sorting_speed = SortingSpeed.SLOW
    for num in range(3):  # size buttons
        if check_distance(mouse_x, mouse_y, int(circle_position[num + 9][0]), int(circle_position[num + 9][1])) < 8:
            if num + 9 == 9:
                settings.array_size = ArraySize.LARGE
            if num + 9 == 10:
                settings.array_size = ArraySize.MEDIUM
            if num + 9 == 11:
                settings.array_size = ArraySize.SMALL
    for num in range(6):  # algorithm buttons
        if check_distance(mouse_x, mouse_y, int(circle_position[num][0]), int(circle_position[num][1])) < 8:
            if num == 0:
                settings.algorithm = Algorithms.BUBBLE_SORT
            if num == 1:
                settings.algorithm = Algorithms.SELECTION_SORT
            if num == 2:
                settings.algorithm = Algorithms.INSERTION_SORT
            if num == 3:
                settings.algorithm = Algorithms.BUCKET_SORT
            if num == 4:
                settings.algorithm = Algorithms.MERGE_SORT
            if num == 5:
                settings.algorithm = Algorithms.QUICK_SORTs


def over_button(button_pos, mouse_x, mouse_y):
    return button_pos[0] < mouse_x < button_pos[0] + button_pos[2] and \
           button_pos[1] < mouse_y < button_pos[1] + button_pos[3]


def slow_down(sorting_speed):
    if sorting_speed == 0:
        pygame.time.delay(5)
    if sorting_speed == 1:
        pygame.time.delay(20)
    if sorting_speed == 2:
        pygame.time.delay(100)


def set_line_color(win, line_width, index, color, height):
    x = 2 + index * (5 + line_width)
    pygame.draw.rect(win, color, (x, 720 - height, line_width, height))
    pygame.display.update()


def check_distance(x, y, x2, y2):
    return math.sqrt((x - x2) ** 2 + (y - y2) ** 2)
