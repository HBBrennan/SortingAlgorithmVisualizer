import pygame
from ui import set_line_color, slow_down
from constants import WIN

def bubble_sort(win,  renderer, sorting_speed):
    #finished = 0
    for i in range(len(renderer.array) - 1):
        for j in range(len(renderer.array) - i - 1):
            pygame.event.get()
            set_line_color(WIN, renderer.line_width, j, renderer.active_color,
                           int(renderer.array[j] / len(renderer.array) * 555))
            set_line_color(WIN, renderer.line_width, j + 1, renderer.active_color,
                           int(renderer.array[j + 1] / len(renderer.array) * 555))
            slow_down(sorting_speed)
            if renderer.array[j] > renderer.array[j + 1]:
                swap(renderer.array, j, j + 1)
                pygame.draw.rect(win, (128, 128, 128), (0, 165, 1280, 720))
                renderer.draw_lines(WIN, renderer.inactive_color)
                #set_line_color(constants.win, line_width, len(array) - 1 - finished, finished_color,
                               #int(array[len(array) - 1 - finished] / len(array) * 555))
            set_line_color(WIN, renderer.line_width, j, renderer.inactive_color,
                           int(renderer.array[j] / len(renderer.array) * 555))
            set_line_color(WIN, renderer.line_width, j + 1, renderer.inactive_color,
                           int(renderer.array[j + 1] / len(renderer.array) * 555))
        #finished = i
        set_line_color(WIN, renderer.line_width, len(renderer.array) - 1 - i, renderer.finished_color,
                       int(renderer.array[len(renderer.array) - 1 - i] / len(renderer.array) * 555))


def selection_sort(win,  renderer, sorting_speed):
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
    for i in range(len(renderer.array) - 1):
        max_idx = i
        for j in range(i + 1, len(renderer.array) - 1):
            pygame.event.get()
            set_line_color(win, renderer.line_width, j, renderer.active_color, int(renderer.array[j] / len(renderer.array) * 555))
            slow_down(sorting_speed)
            if renderer.array[j] < renderer.array[max_idx]:
                set_line_color(win, renderer.line_width, max_idx, renderer.inactive_color, int(renderer.array[max_idx] / len(renderer.array) * 555))
                max_idx = j
                set_line_color(win, renderer.line_width, max_idx, renderer.active_color, int(renderer.array[max_idx] / len(renderer.array)))
            else:
                set_line_color(win, renderer.line_width, j, renderer.inactive_color, int(renderer.array[j] / len(renderer.array) * 555))
            set_line_color(win, renderer.line_width, max_idx, renderer.inactive_color, int(renderer.array[j] / len(renderer.array) * 555))
            renderer.array[i], renderer.array[max_idx] = renderer.array[max_idx], renderer.array[i]
            set_line_color(win, renderer.line_width, i, renderer.finished_color, int(renderer.array[i] / len(renderer.array) * 555))
            pygame.draw.rect(win, (128, 128, 128), (0, 165, 1280, 720))
            renderer.draw_lines(win, renderer.inactive_color)


def insertion_sort(win,  renderer, sorting_speed):
    for i in range(1, len(renderer.array)):
        key = renderer.array[i]
        j = i - 1
        while j >= 0 and key < renderer.array[j]:
            set_line_color(win, renderer.line_width, i, renderer.finished_color, int(renderer.array[i] / len(renderer.array) * 555))
            set_line_color(win, renderer.line_width, j + 1, renderer.active_color, int(renderer.array[j + 1] / len(renderer.array) * 555))
            set_line_color(win, renderer.line_width, j, renderer.active_color, int(renderer.array[j] / len(renderer.array) * 555))
            renderer.array[j + 1] = renderer.array[j]
            slow_down(sorting_speed)
            pygame.draw.rect(win, (128, 128, 128), (0, 165, 1280, 720))
            renderer.draw_lines(win, renderer.inactive_color)
            j -= 1
        renderer.array[j + 1] = key
        slow_down(sorting_speed)
        pygame.draw.rect(win, (128, 128, 128), (0, 165, 1280, 720))
        renderer.draw_lines(win, renderer.inactive_color)


def bucket_sort(win, inactive_color, active_color, finished_color, array, sorting_speed, line_width):
    bucket = []


def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]

