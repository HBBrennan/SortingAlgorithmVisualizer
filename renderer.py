import pygame
import random
from constants import COLOR_DARK_BLUE, COLOR_WHITE, COLOR_RED


class Renderer():
    def __init__(self, array_size):
        self.line_width = int(((1280 - (array_size - 1) * 5 - 4) / array_size))

    active_color = COLOR_RED
    inactive_color = COLOR_DARK_BLUE
    finished_color = COLOR_WHITE
    array = []

    def set_line_width(self, array_size):
        line_width = int(((1280 - (array_size - 1) * 5 - 4) / array_size))

    def draw_lines(self, win, line_color):
        x = 2
        for line in self.array:
            height = int(line / len(self.array) * 555)
            pygame.draw.rect(win, line_color, (x, 720 - height, self.line_width, height))
            x += self.line_width + 5
        pygame.display.update()

    def refresh_lines(self, win, array_size):
        pygame.draw.rect(win, (128, 128, 128), (0, 165, 1280, 720))
        self.array = list(range(1, array_size + 1))
        random.shuffle(self.array)
        self.line_width = int(((1280 - (array_size - 1) * 5 - 4) / array_size))
        self.draw_lines(win, self.inactive_color)
