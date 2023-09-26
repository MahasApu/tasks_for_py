import numpy as np

from time import time


class Cell:
    def __init__(self, size, flag=1):
        self.size = size
        self.field = np.random.randint(low=0, high=2, size=(size, size))
        if flag == 2:
            self.field = self.field.tolist()

    def get_cell_neighbour(self, ind_i, ind_j):
        nb_sum = 0
        try:
            nb_sum = self.field[ind_i + 1][ind_j + 1] + self.field[ind_i + 1][ind_j - 1] + self.field[ind_i - 1][ind_j + 1] \
                     + self.field[ind_i - 1][ind_j - 1]
        except IndexError:
            pass
        return nb_sum

    def next_cell(self):
        field_to_step = self.field

        for ind_i in range(self.size):
            for ind_j in range(self.size):

                nb_sum = self.get_cell_neighbour(ind_i, ind_j)

                if not self.field[ind_i][ind_j] and nb_sum == 3:
                    field_to_step[ind_i][ind_j] = 1

                elif self.field[ind_i][ind_j] and nb_sum not in (2, 3):
                    field_to_step[ind_i][ind_j] = 0
        self.field = field_to_step


def Conway_game(size, flag, iteration):
    start = time()
    life = Cell(size, flag)
    for i in range(iteration):
        life.next_cell()
    end = time()
    print(end - start)


print("Taken time for numpy array")
Conway_game(1024, 1, 128)

print("Taken time for python list")
Conway_game(1024, 2, 128)

# Taken time for numpy array
# 174.46523785591125
# Taken time for python list
# 74.85257983207703

