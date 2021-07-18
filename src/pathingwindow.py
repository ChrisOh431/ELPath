from dearpygui.core import *
from dearpygui.simple import *
from pathfindhost import PathfindingHost
import consts as cnsts
from random import randint
from time import sleep
from math import trunc


class PathingWindow:
    def __init__(self):
        self.pathing_host = PathfindingHost()
        self.window_size = 800
        self.side_cell_count = 20
        self.cell_size = self.window_size/self.side_cell_count
        #self.message = self.pathing_host.alg_name

    def initialize_grid(self):
        set_mouse_click_callback(self.get_clicked_cell)
        
        for i in range(self.side_cell_count):
            for j in range(self.side_cell_count):
                draw_rectangle("grid", [i*self.cell_size, j*self.cell_size], [(i+1)*self.cell_size, (j+1)*self.cell_size], [
                               34, 36, 37, 255], fill=[255, 255, 255, 255], rounding=2, thickness=1)
        #self.message = f"{self.pathing_host.alg_name}"


    def get_clicked_cell(self):
        pos = get_drawing_mouse_pos()
        left_bound_adjusted_x = pos[0]
        top_bound_adjusted_y = pos[1]

        min_x = 0
        min_y = 0
        max_x = 800
        max_y = 800

        within_x =  left_bound_adjusted_x >= min_x and left_bound_adjusted_x <= max_x
        within_y = top_bound_adjusted_y >= min_y and top_bound_adjusted_y <= max_y

        x_cell = trunc(pos[0]//self.cell_size)
        y_cell = trunc(pos[1]//self.cell_size)

        if (get_active_window() == "Simulation" and within_x and within_y):
            print(f"X: {x_cell}\nY: {y_cell}")


    def update(self, new_data):
        pass
        self.message = f"{self.pathing_host.alg_name} Step {self.pathing_host.step_counter}: {new_data['message']}"

    def next_step(self):
        value = self.pathing_host.next_step()
        self.update(value)
        return value

    def change_algorithm(self):
        self.clear_highlights()
        self.pathing_host.set_algorithm(get_value("algorithm_combobox"))
        self.original_data()
