import pygame


class Board:
    # создание поля
    def __init__(self, width, height, figures):
        self.figures = figures
        self.width = width
        self.height = height
        self.left = 20
        self.top = 20
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        pass


class Figure:
    def __init__(self, color, coor):
        self.color = color  # "white"/"black"
        self.coor = coor  # x, y

    def return_data(self):
        return self.color, self.coor


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Checkers")
    size = width, height = 700, 700
