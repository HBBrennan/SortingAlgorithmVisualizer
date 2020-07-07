import random
import pygame
import math
import time
import algorithms
import constants


def main():
    pygame.init()
    pygame.display.set_caption("Sorting Algorithm Visualizer")

    print("The width of every line should be: " + str(constants.line_width) + " pixels.")

    array = list(range(1, constants.array_size + 1))
    random.shuffle(array)
    print(array)

    run = True
    constants.win.fill((128, 128, 128))
    draw_circles(constants.win, constants.color_white, constants.circle_position, constants.algorithm,
                 constants.sorting_speed)
    draw_text(constants.win, constants.verdana24, constants.verdana16, constants.color_white)
    draw_lines(array, constants.win, constants.color_dark_blue, constants.line_width)
    pygame.display.update()
    while run:
        global mouse_x, mouse_y
        mouse_x, mouse_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.event.get()
                mark_circles(constants.array_size, constants.sorting_speed, constants.algorithm,
                             constants.circle_position)
                draw_circles(constants.win, constants.color_white, constants.circle_position, constants.algorithm,
                 constants.sorting_speed)
                if over_button(constants.button_position[1]):
                    refresh_lines(constants.win, array, constants.line_width)
                if over_button(constants.button_position[0]):
                    sort(constants.algorithm, array)

        draw_lines(array, constants.win, constants.color_dark_blue, constants.line_width)
        draw_text(constants.win, constants.verdana24, constants.verdana16, constants.color_white)
        draw_buttons(constants.win, constants.button_position, constants.color_dark_blue, constants.color_red,
                     constants.color_white, constants.verdana30)
        pygame.display.update()


def draw_lines(array, win, line_color, line_width):
    x = 2
    for line in array:
        height = int(line / len(array) * 555)
        pygame.draw.rect(win, line_color, (x, 720 - height, line_width, height))
        x += line_width + 5
    pygame.display.update()


def refresh_lines(win, array, line_width):
    pygame.draw.rect(win, (128, 128, 128), (0, 165, 1280, 720))
    array = list(range(1, constants.array_size + 1))
    random.shuffle(array)
    line_width = int(((1280 - (constants.array_size - 1) * 5 - 4) / constants.array_size))
    draw_lines()


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


def draw_buttons(win, button_position, active_color, inactive_color, text_color, text_font):
    for button in button_position:
        color = inactive_color
        if over_button(button):
            color = active_color

        pygame.draw.rect(win, color, button)

    win.blit(text_font.render('Sort', False, text_color), (610, 26))
    win.blit(text_font.render('Reset', False, text_color), (600, 106))


def draw_circles(win, color, circle_position, algorithm, sorting_speed):
    for num in range(len(circle_position)):
        pygame.draw.circle(win, color, circle_position[num], 12, 3)
        pygame.draw.circle(win, (128, 128, 128), circle_position[num], 7)

    pygame.draw.circle(win, color, (circle_position[algorithm][0], circle_position[algorithm][1]), 5)

    pygame.draw.circle(win, color, (circle_position[sorting_speed + 6][0],
                                    circle_position[sorting_speed + 6][1]), 5)

    if constants.array_size == 80:
        pygame.draw.circle(win, color, (circle_position[9][0], circle_position[9][1]), 5)
    elif constants.array_size == 40:
        pygame.draw.circle(win, color, (circle_position[10][0], circle_position[10][1]), 5)
    elif constants.array_size == 20:
        pygame.draw.circle(win, color, (circle_position[11][0], circle_position[11][1]), 5)


    pygame.display.update()


def check_distance(x, y, x2, y2):
    return math.sqrt((x - x2) ** 2 + (y - y2) ** 2)


def mark_circles(array_size, sorting_speed, algorithm, circle_position):
    for num in range(3):  # speed buttons
        if check_distance(mouse_x, mouse_y, int(circle_position[num + 6][0]), int(circle_position[num + 6][1])) < 8:
            if num + 6 == 6:
                sorting_speed = 0
            if num + 6 == 7:
                sorting_speed = 1
            if num + 6 == 8:
                sorting_speed = 2
    for num in range(3):  # size buttons
        if check_distance(mouse_x, mouse_y, int(circle_position[num + 9][0]), int(circle_position[num + 9][1])) < 8:
            if num + 9 == 9:
                array_size = 80
            if num + 9 == 10:
                array_size = 40
            if num + 9 == 11:
                array_size = 20
    for num in range(6):  # algorithm buttons
        if check_distance(mouse_x, mouse_y, int(circle_position[num][0]), int(circle_position[num][1])) < 8:
            algorithm = num



def over_button(button_pos):
    return button_pos[0] < mouse_x < button_pos[0] + button_pos[2] and \
           button_pos[1] < mouse_y < button_pos[1] + button_pos[3]


def sort(algorithm, array):
    if algorithm == 0:
        bubble_sort(constants.win, constants.color_dark_blue, constants.color_white,
                    constants.color_white, array)


def bubble_sort(win, inactive_color, active_color, finished_color, array):
    for i in range(len(array) - 1):
        for j in range(0, len(array) - i - 1):
            pygame.event.get()
            set_line_color(constants.win, constants.line_width, j, active_color, int(array[j] / len(array) * 555))
            set_line_color(constants.win, constants.line_width, j + 1, active_color, int(array[j + 1] / len(array) * 555))
            slow_down(constants.sorting_speed)
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)
                pygame.draw.rect(win, (128, 128, 128), (0, 165, 1280, 720))
                draw_lines(array, constants.win, constants.color_dark_blue, constants.line_width)
            set_line_color(constants.win, constants.line_width, j, inactive_color, int(array[j] / len(array) * 555))
            set_line_color(constants.win, constants.line_width, j + 1, inactive_color, int(array[j + 1] / len(array) * 555))
        set_line_color(constants.win, constants.line_width, i, finished_color, int(i / len(array) * 555))


def slow_down(sorting_speed):
    if sorting_speed == 0:
        pygame.time.delay(5)
    if sorting_speed == 1:
        pygame.time.delay(20)
    if sorting_speed == 2:
        pygame.time.delay(100)


def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]


def set_line_color(win, line_width, index, color, height):
    x = 2 + index * (5 + line_width)
    pygame.draw.rect(win, color, (x, 720 - height, line_width, height))
    pygame.display.update()


if __name__ == "__main__":
    # execute only if run as a script
    main()



