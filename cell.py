import pygame
from settings import *

class Cell:
    def __init__(self, i, j, size) -> None:
        self.i = i
        self.j = j
        self.size = size
        self.x = i * size
        self.y = j * size
        self.color = WHITE 
        self.f = 100
        self.g = 100
        self.h = 100
        self.wall = False

        self.neighbors = []
        self.previous = None

    def add_neighbor(self, neighbor) -> None:
        self.neighbors.append(neighbor)
    
    def add_previous(self, prev) -> None:
        self.previous = prev
    
    def get_neighbors(self) -> list:
        return self.neighbors
    
    def get_previous(self):
        return self.previous
    
    def set_wall(self) -> None:
        self.wall = not self.wall
    
    def get_wall(self) -> bool:
        return self.wall
    
    def set_color(self, color) -> None:
        self.color = color
    
    def set_f(self, f) -> None:
        self.f = f

    def set_g(self, g) -> None:
        self.g = g

    def set_h(self, h) -> None:
        self.h = h
    
    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def get_f(self) -> int:
        return self.f

    def get_g(self) -> int:
        return self.g

    def get_h(self) -> int:
        return self.h
    
    def draw(self, win) -> None:
        if self.wall:
            pygame.draw.rect(win, BLACK, (self.x, self.y, self.size - 1, self.size - 1))
        else:
            pygame.draw.rect(win, self.color, (self.x, self.y, self.size - 1, self.size - 1))