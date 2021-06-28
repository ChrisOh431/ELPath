from algorithms import bubble, insertion
from random import randint
from time import sleep

class AlgorithmHost:
    def __init__(self, data_set=[]):
        self.data_set_size = 30

        self.step_counter = 0

        self.data_x = [i for i in range(self.data_set_size)]
        self.data_y = []

        self.alg_name = "Bubble Sort"
        self.alg_list = {
            "Bubble Sort": (lambda dataset: bubble(self.data_y)),
            "Insertion Sort": (lambda dataset: insertion(self.data_y)),
        }

        self.current_algorithm = self.alg_list["Bubble Sort"]

        if not data_set:
            self.set_random_data()

    def set_algorithm(self, name):
        self.alg_name = name
        self.step_counter = 0
        self.current_algorithm = self.alg_list[name](self.data_y)

    def set_random_data(self):
        self.step_counter = 0
        self.data_y = [randint(1, self.data_set_size) for i in range(self.data_set_size)]
        self.current_algorithm = self.alg_list[self.alg_name](self.data_y)

    def next_step(self):
        try:
            self.step_counter += 1
            return next(self.current_algorithm)
        except StopIteration:
            return False