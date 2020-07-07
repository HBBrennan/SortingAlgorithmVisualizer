import random
import pygame
import math
import time
import algorithms
def main():
    pygame.init()

    win = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Sorting Algorithm Visualizer")


    print("The width of every line should be: " + str(line_width) + " pixels.")

    array = list(range(1, array_size + 1))
    random.shuffle(array)
    print(array)

    run = True
    win.fill((128, 128, 128))
    draw_circles()
    draw_text()
    draw_lines()
    pygame.display.update()
    while run:
        global mouse_x, mouse_y
        mouse_x, mouse_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.event.get()
                mark_circles()
                draw_circles()
                if over_button(button_position[1]):
                    refresh_lines()
                if over_button(button_position[0]):
                    sort()

        draw_lines()
        draw_text()
        draw_buttons()
        pygame.display.update()

def draw_lines():
    x = 2
    for line in array:
        height = int(line / len(array) * 555)
        pygame.draw.rect(win, color_dark_blue, (x, 720 - height, line_width, height))
        x += line_width + 5
    pygame.display.update()


def refresh_lines():
    pygame.draw.rect(win, (128, 128, 128), (0, 165, 1280, 720))
    global array, line_width
    array = list(range(1, array_size + 1))
    random.shuffle(array)
    line_width = int(((1280 - (array_size - 1) * 5 - 4) / array_size))
    draw_lines()


def draw_text():
    win.blit(verdana24.render('Algorithm', False, color_white), (950, 20))
    win.blit(verdana16.render('Bubble Sort', False, color_white), (870, 76))
    win.blit(verdana16.render('Selection Sort', False, color_white), (870, 106))
    win.blit(verdana16.render('Insertion Sort', False, color_white), (870, 136))
    win.blit(verdana16.render('Bucket Sort', False, color_white), (1070, 76))
    win.blit(verdana16.render('Merge Sort', False, color_white), (1070, 106))
    win.blit(verdana16.render('Quick Sort', False, color_white), (1070, 136))

    win.blit(verdana24.render('Speed', False, color_white), (55, 26))
    win.blit(verdana16.render('Fast', False, color_white), (110, 77))
    win.blit(verdana16.render('Medium', False, color_white), (110, 107))
    win.blit(verdana16.render('Slow', False, color_white), (110, 137))

    win.blit(verdana24.render('Size', False, color_white), (265, 26))
    win.blit(verdana16.render('Large', False, color_white), (310, 77))
    win.blit(verdana16.render('Medium', False, color_white), (310, 107))
    win.blit(verdana16.render('Small', False, color_white), (310, 137))


def draw_buttons():
    for button in button_position:
        color = color_dark_blue
        if over_button(button):
            color = color_light_blue

        pygame.draw.rect(win, color, button)

    win.blit(verdana30.render('Sort', False, color_white), (610, 26))
    win.blit(verdana30.render('Reset', False, color_white), (600, 106))


def draw_circles():
    for num in range(len(circle_position)):
        pygame.draw.circle(win, color_white, circle_position[num], 12, 3)
        pygame.draw.circle(win, (128, 128, 128), circle_position[num], 7)

    pygame.draw.circle(win, color_white, (circle_position[algorithm][0], circle_position[algorithm][1]), 5)

    pygame.draw.circle(win, color_white, (circle_position[sorting_speed + 6][0],
                                          circle_position[sorting_speed + 6][1]), 5)

    if array_size == 80:
        pygame.draw.circle(win, color_white, (circle_position[9][0], circle_position[9][1]), 5)
    elif array_size == 40:
        pygame.draw.circle(win, color_white, (circle_position[10][0], circle_position[10][1]), 5)
    elif array_size == 20:
        pygame.draw.circle(win, color_white, (circle_position[11][0], circle_position[11][1]), 5)


    pygame.display.update()


def check_distance(x, y, x2, y2):
    return math.sqrt((x - x2) ** 2 + (y - y2) ** 2)


def mark_circles():
    global array_size, sorting_speed, algorithm
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


def sort():
    if algorithm == 0:
        bubble_sort()


def bubble_sort():
    for i in range(len(array) - 1):
        for j in range(0, len(array) - i - 1):
            pygame.event.get()
            set_line_color(j, color_red, int(array[j] / len(array) * 555))
            set_line_color(j + 1, color_red, int(array[j + 1] / len(array) * 555))
            slow_down()
            if array[j] > array[j + 1]:
                swap(j, j + 1)
                pygame.draw.rect(win, (128, 128, 128), (0, 165, 1280, 720))
                draw_lines()
            set_line_color(j, color_dark_blue, int(array[j] / len(array) * 555))
            set_line_color(j + 1, color_dark_blue, int(array[j + 1] / len(array) * 555))
        set_line_color(i, color_white, int(i / len(array) * 555))


def slow_down():
    if sorting_speed == 0:
        pygame.time.delay(5)
    if sorting_speed == 1:
        pygame.time.delay(20)
    if sorting_speed == 2:
        pygame.time.delay(100)


def swap(index1, index2):
    global array
    array[index1], array[index2] = array[index2], array[index1]


def set_line_color(index, color, height):
    x = 2 + index * (5 + line_width)
    pygame.draw.rect(win, color, (x, 720 - height, line_width, height))
    pygame.display.update()


if __name__ == "__main__":
    # execute only if run as a script
    main()



