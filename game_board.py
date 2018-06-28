import cell
import random

class Board(object):
    def __init__(self, length, height):
        self._length = length
        self._height = height
        self._prev_state = 0
        self._prev_state_2 = 0
        self._board = [ [ cell.Cell() for _ in range(self._height)] \
                         for _ in range(self._length) ]
        
        for i, row in enumerate(self._board):
            for j, c in enumerate(row):
                c._i = i
                c._j = j


    def show_board(self, display):
        for i in range(self._length):
            for j in range(self._height):
                if self._board[i][j]._state == 1:
                    display.pixel(i, j, 64)
                else:
                    display.pixel(i, j, 0)
            

    def next_gen(self):
        for row in self._board:
            for c in row:
                self.advance(c)

        for row in self._board:
            for c in row:
                c._state = c._next_state


    def advance(self, c):
        neighbors_states = self.get_neighbor_states(c)
        sum_of_neighbor_states = sum(neighbors_states)
        if c._state == 1:
            if sum_of_neighbor_states in range(2,4):
                c._next_state = 1
            else:
                c._next_state = 0
        else:
            if sum_of_neighbor_states == 3:
                c._next_state = 1
            else:
                c._next_state = 0


    def get_neighbor_states(self, c):
        i, j = c._i, c._j
        neighbors_states = []
        for neighbor_i in range(i-1, i+2):
            for neighbor_j in range(j-1, j+2):
                if neighbor_i != i or neighbor_j != j:
                    neighbor = self._board[neighbor_i % self._length] \
                                          [neighbor_j % self._height]
                    neighbors_states.append(neighbor._state)
        return neighbors_states


    def check_dead_state(self):
        state_value = 0
        for i in range(self._length):
            for j in range(self._height):
                if self._board[i][j]._state == 1:
                    state_value += (i^j * j^i)
    
        if state_value in [self._prev_state, self._prev_state_2]:
            self.randomize()
            self._prev_state = 0
            self._prev_state_2 = 0
            return
    
        self._prev_state_2 = self._prev_state
        self._prev_state = state_value


    def randomize(self):
        for row in self._board:
            for c in row:
                c._state = random.randint(0,1)
