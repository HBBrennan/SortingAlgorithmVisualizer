import pygame
from ui import set_line_color, slow_down, draw_lines
from constants import WIN

def bubble_sort(win, inactive_color, active_color, finished_color, array, sorting_speed, line_width):
    #finished = 0
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            pygame.event.get()
            set_line_color(WIN, line_width, j, active_color, int(array[j] / len(array) * 555))
            set_line_color(WIN, line_width, j + 1, active_color, int(array[j + 1] / len(array) * 555))
            slow_down(sorting_speed)
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)
                pygame.draw.rect(win, (128, 128, 128), (0, 165, 1280, 720))
                draw_lines(array, WIN, inactive_color, line_width)
                #set_line_color(constants.win, line_width, len(array) - 1 - finished, finished_color,
                               #int(array[len(array) - 1 - finished] / len(array) * 555))
            set_line_color(WIN, line_width, j, inactive_color, int(array[j] / len(array) * 555))
            set_line_color(WIN, line_width, j + 1, inactive_color, int(array[j + 1] / len(array) * 555))
        #finished = i
        set_line_color(WIN, line_width, len(array) - 1 - i, finished_color, int(array[len(array) - 1 - i] / len(array) * 555))


def selection_sort(win, inactive_color, active_color, finished_color, array, sorting_speed, line_width):
    # for i in range(len(array)):
    #     min_idx = i
    #     set_line_color(win, line_width, i, active_color, int(array[i] / len(array) * 555))
    #     slow_down(sorting_speed)
    #     for j in range(i + 1, len(array)):
    #         set_line_color(win, line_width, j, active_color, int(array[j] / len(array) * 555))
    #         if array[min_idx] > array[j]:
    #             set_line_color(win, line_width, min_idx, inactive_color, int(array[j] / len(array) * 555))
    #             min_idx = j
    #             set_line_color(win, line_width, min_idx, active_color, int(array[j] / len(array) * 555))
    #
    #     array[i], array[min_idx] = array[min_idx], array[i]
    for i in range(len(array) - 1):
        max_idx = i
        for j in range(i + 1, len(array) - 1):
            pygame.event.get()
            set_line_color(win, line_width, j, active_color, int(array[j] / len(array) * 555))
            slow_down(sorting_speed)
            if array[j] < array[max_idx]:
                set_line_color(win, line_width, max_idx, inactive_color, int(array[max_idx] / len(array) * 555))
                max_idx = j
                set_line_color(win, line_width, max_idx, active_color, int(array[max_idx] / len(array)))
            else:
                set_line_color(win, line_width, j, inactive_color, int(array[j] / len(array) * 555))
            set_line_color(win, line_width, max_idx, inactive_color, int(array[j] / len(array) * 555))
            array[i], array[max_idx] = array[max_idx], array[i]
            set_line_color(win, line_width, i, finished_color, int(array[i] / len(array) * 555))
            pygame.draw.rect(win, (128, 128, 128), (0, 165, 1280, 720))
            draw_lines(array, win, inactive_color, line_width)


def insertion_sort(win, inactive_color, active_color, finished_color, array, sorting_speed, line_width):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            set_line_color(win, line_width, i, finished_color, int(array[i] / len(array) * 555))
            set_line_color(win, line_width, j + 1, active_color, int(array[j + 1] / len(array) * 555))
            set_line_color(win, line_width, j, active_color, int(array[j] / len(array) * 555))
            array[j + 1] = array[j]
            slow_down(sorting_speed)
            pygame.draw.rect(win, (128, 128, 128), (0, 165, 1280, 720))
            draw_lines(array, win, inactive_color, line_width)
            j -= 1
        array[j + 1] = key
        slow_down(sorting_speed)
        pygame.draw.rect(win, (128, 128, 128), (0, 165, 1280, 720))
        draw_lines(array, win, inactive_color, line_width)


def bucket_sort(win, inactive_color, active_color, finished_color, array, sorting_speed, line_width):
    bucket = []


def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]

