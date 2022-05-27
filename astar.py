import math
from settings import *

class Astar:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self.open_list = []
        self.closed_list = []
        self.current = None
        self.path = []
        self.init()

    def init(self):
        self.start.set_f(0)
        self.start.set_g(0)
        self.start.set_h(self.heuristic(self.start, self.end))
        self.open_list.append(self.start)

    def heuristic(self, current, goal) -> int:
        c_x = current.get_x()
        c_y = current.get_y()
        g_x = goal.get_x()
        g_y = goal.get_y()

        # return math.sqrt(pow(c_x - g_x, 2) + pow(c_y- g_y, 2))
        return abs(c_x - g_x) + abs(c_y - g_y)
    
    def calculate_path(self) -> bool:
        if len(self.open_list) > 0:
            lowest = 0
            for i in range(len(self.open_list)):
                if self.open_list[i].get_f() < self.open_list[lowest].get_f():
                    lowest = i
            
            self.current = self.open_list[lowest]

            if self.current == self.end:
                temp = self.current

                self.path.append(temp)
                temp.set_color(BLUE)
                while temp.get_previous():
                    temp = temp.get_previous()
                    temp.set_color(BLUE)
                    self.path.append(temp)
                return True
            
            self.open_list.remove(self.current)
            self.closed_list.append(self.current)

            neighbors = self.current.get_neighbors()

            for i in range(len(neighbors)):
                current_neighbor = neighbors[i]

                if not current_neighbor in self.closed_list and not current_neighbor.get_wall():
                    if current_neighbor in self.open_list:
                        if (self.current.get_f() < current_neighbor.get_f()):
                            current_neighbor.set_g(self.current.get_g() + self.heuristic(current_neighbor, self.current))
                            current_neighbor.set_h(self.heuristic(current_neighbor, self.end))
                            current_neighbor.set_f(current_neighbor.get_g() + current_neighbor.get_h())
                    else:
                        current_neighbor.add_previous(self.current)
                        self.open_list.append(current_neighbor)

            for i in range(len(self.open_list)):
                self.open_list[i].set_color(GREEN)

            for i in range(len(self.closed_list)):
                self.closed_list[i].set_color(RED)
                
        return False