from dearpygui.core import *
from dearpygui.simple import *
from pathfindhost import PathfindingHost
import consts as cnsts
from random import randint
from time import sleep
from math import trunc


class PathingWindow:
    def __init__(self):
        self.window_size = 800
        self.side_cell_count = 40
        self.cell_size = self.window_size/self.side_cell_count

        self.min_x = 0
        self.min_y = 0
        self.max_x = 800
        self.max_y = 800

        self.pathing_host = PathfindingHost(
            self.side_cell_count, lambda node: self.update_node(node))
        self.colors = {
            "EMPTY": [255, 255, 255],
            "START": [127, 255, 0],
            "END": [255, 0, 0],
            "OPEN": [255, 255, 0],
            "CLOSE": [0, 191, 255],
            "PATH": [138, 43, 226],
            "BARR": [54, 54, 54]
        }
        #self.message = self.pathing_host.alg_name

    def draw_node(self, node):
        itag = f"{node.x:02d}"
        jtag = f"{node.y:02d}"
        draw_rectangle("grid", [node.x*self.cell_size, node.y*self.cell_size], [(node.x+1)*self.cell_size, (node.y+1)*self.cell_size], [
            34, 36, 37, 255],  fill=self.colors[node.state], rounding=2, thickness=1, tag=f"{itag}{jtag}")

    def update_node(self, node):
        itag = f"{node.x:02d}"
        jtag = f"{node.y:02d}"
        if node.state == node.altstate:
            modify_draw_command(
                "grid", f"{itag}{jtag}", fill=self.colors[node.state])
        else:
            modify_draw_command(
                "grid", f"{itag}{jtag}", fill=self.colors[node.altstate])

    def initialize_grid(self):
        add_drawing("grid", parent="Simulation",
                    width=800, height=800, show=True)
        set_mouse_down_callback(self.cell_clicked)
        for row in self.pathing_host.grid:
            for node in row:
                self.draw_node(node)

    def cell_clicked(self):
        # Preventing click detection when outside of window
        genpos = get_mouse_pos()
        genpos[1] += 30  # account for window padding
        if (genpos[1] > self.max_y or genpos[1] < self.min_y or genpos[0] < 0 or genpos[0] > self.max_x or get_active_window() != "Simulation"):
            return

        pos = get_drawing_mouse_pos()

        within_x = pos[0] >= self.min_x and pos[0] <= self.max_x
        within_y = pos[1] >= self.min_y and pos[1] <= self.max_y

        x_cell = trunc(pos[0]//self.cell_size)
        y_cell = trunc(pos[1]//self.cell_size)

        clearing = True if (is_mouse_button_down(
            1)) else False  # True if right clicking

        if (within_x and within_y):
            node = self.pathing_host.node_from_pos((x_cell, y_cell))
            tempstate = node.get_state()
            if clearing:
                if (tempstate == "BARR"):
                    node.set_state_empty()
                if (tempstate == "START"):
                    self.pathing_host.remove_start()
                if (tempstate == "END"):
                    self.pathing_host.remove_end()

            else:
                if (tempstate == "EMPTY"):
                    node.set_state_barrier()
                    if (self.pathing_host.start_point is None):
                        self.pathing_host.add_start(node)
                    elif (self.pathing_host.end_point is None):
                        self.pathing_host.add_end(node)

            self.update_node(node)

    def next_step(self):
        if not self.pathing_host.initialized:
            self.pathing_host.initialize_neighbors()
        return self.pathing_host.next_step()

    def reset(self):
        pass

    def unmount(self):
        delete_item("grid", children_only=False)
        self.pathing_host = PathfindingHost(
            self.side_cell_count, lambda node: self.draw_node(node))
