import pygame
pygame.font.init()

verdana16 = pygame.font.SysFont('Verdana', 16)
verdana24 = pygame.font.SysFont('Verdana', 24)
verdana30 = pygame.font.SysFont('Verdana', 30)

color_dark_blue = (0, 0, 255)
color_light_blue = (105, 152, 255)
color_white = (250, 250, 250)
color_red = (229, 42, 60)

circle_position = [
    (850, 88),  # Sorting algorithm buttons
    (850, 118),
    (850, 148),
    (1050, 88),
    (1050, 118),
    (1050, 148),

    (90, 88),  # Speed buttons
    (90, 118),
    (90, 148),

    (290, 88),
    (290, 119),
    (290, 148)  # Size buttons

]
button_position = [
    (520, 10, 240, 70),
    (520, 90, 240, 70)
]

array_size = 80  # default, 80 = large, 40 = Medium, 20 = small
algorithm = 0
sorting_speed = 0  # 0 = fast, 1 = Medium, 2 = slow

line_width = int(((1280 - (array_size - 1) * 5 - 4) / array_size))