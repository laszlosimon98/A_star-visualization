import pygame
import random

from settings import *
from cell import Cell
from astar import Astar
pygame.init()

class A_star_visualization:
    board = None
    astar = None
    def __init__(self) -> None:
        self.w = WIDTH
        self.h = WIDTH
        self.size = SIZE
        self.c = COL 
        self.win = pygame.display.set_mode((self.w, self.h))
        self.title = pygame.display.set_caption("A* visualization")
        self.run = True
        self.clock = pygame.time.Clock()

    def create_board(self) -> list[list[Cell]]:
        arr = []
        for i in range(self.c):
            arr.append([])
            for j in range(self.c):
                arr[i].append(Cell(i, j, self.size))
        return arr
    
    def random_walls(self) -> None:
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if random.random() < 0.3:
                    self.board[i][j].set_wall()
    
    def init(self) -> None:
        self.board = self.create_board()
        start = self.board[0][0]
        end = self.board[self.c - 1][self.c - 1]
        start.set_color((0, 255, 0, 255))
        end.set_color((0, 0, 255, 255))

        self.random_walls()
        if start.get_wall():
            start.set_wall()

        if end.get_wall():
            end.set_wall()

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if i < self.c - 1:
                    self.board[i][j].add_neighbor(self.board[i + 1][j])

                if i > 0:
                    self.board[i][j].add_neighbor(self.board[i - 1][j])

                if j < self.c - 1:
                    self.board[i][j].add_neighbor(self.board[i][j + 1])

                if j > 0:
                    self.board[i][j].add_neighbor(self.board[i][j - 1])

        self.astar = Astar(start, end)

    def draw(self, win) -> None:
        win.fill(BLACK)
        self.clock.tick(30)

        for i, _ in enumerate(self.board):
            for j, _ in enumerate(self.board[i]):
                self.board[i][j].draw(win)
            
        self.astar.calculate_path()

        pygame.display.update()

    def update(self) -> None:
        self.init()
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                
            self.draw(self.win)

if __name__ == "__main__":
    a_star = A_star_visualization()
    a_star.update()