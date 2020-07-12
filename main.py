import random
import pygame
import math
import time
import constants
from settings import Settings
from algorithms import *
from ui import *


def main():
    pygame.init()
    pygame.display.set_caption("Sorting Algorithm Visualizer")

    settings = Settings()
    line_width = int(((1280 - (settings.array_size.value - 1) * 5 - 4) / settings.array_size.value))
    print("The width of every line should be: " + str(line_width) + " pixels.")
    array = list(range(1, int(settings.array_size.value) + 1))
    random.shuffle(array)
    print(array)

    run = True
    constants.WIN.fill((128, 128, 128))
    draw_circles(constants.WIN, constants.COLOR_WHITE, constants.CIRCLE_POSITIONS, settings.algorithm,
                 settings.sorting_speed.value, settings.array_size.value)
    draw_text(constants.WIN, constants.VERDANA_24, constants.VERDANA_16, constants.COLOR_WHITE)
    draw_lines(array, constants.WIN, constants.COLOR_DARK_BLUE, line_width)
    pygame.display.update()
    while run:
        mouse_x, mouse_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.event.get()
                settings = mark_circles(mouse_x, mouse_y, settings.array_size, settings.sorting_speed,
                                        settings.algorithm, constants.CIRCLE_POSITIONS)
                draw_circles(constants.WIN, constants.COLOR_WHITE, constants.CIRCLE_POSITIONS, settings.algorithm,
                             settings.sorting_speed.value, settings.array_size.value)
                if over_button(constants.BUTTON_POSITIONS[1], mouse_x, mouse_y):
                    array, line_width = refresh_lines(constants.WIN, array, line_width, settings.array_size.value)
                if over_button(constants.BUTTON_POSITIONS[0], mouse_x, mouse_y):
                    sort(settings.algorithm, array, settings.sorting_speed.value, line_width)

        draw_lines(array, constants.WIN, constants.COLOR_DARK_BLUE, line_width)
        draw_text(constants.WIN, constants.VERDANA_24, constants.VERDANA_16, constants.COLOR_WHITE)
        draw_buttons(constants.WIN, constants.BUTTON_POSITIONS, constants.COLOR_DARK_BLUE, constants.COLOR_RED,
                     constants.COLOR_WHITE, constants.VERDANA_30, mouse_x, mouse_y)
        pygame.display.update()



def sort(algorithm, array, sorting_speed, line_width):
    if algorithm.value == 0:
        bubble_sort(constants.WIN, constants.COLOR_DARK_BLUE, constants.COLOR_RED,
                    constants.COLOR_WHITE, array, sorting_speed, line_width)
    if algorithm.value == 1:
        selection_sort(constants.WIN, constants.COLOR_DARK_BLUE, constants.COLOR_RED,
                       constants.COLOR_WHITE, array, sorting_speed, line_width)
    if algorithm.value == 2:
        insertion_sort(constants.WIN, constants.COLOR_DARK_BLUE, constants.COLOR_RED,
                       constants.COLOR_WHITE, array, sorting_speed, line_width)
    if algorithm.value == 3:
        bucket_sort(constants.WIN, constants.COLOR_DARK_BLUE, constants.COLOR_RED,
                    constants.COLOR_WHITE, array, sorting_speed, line_width)



if __name__ == "__main__":
    # execute only if run as a script
    main()



