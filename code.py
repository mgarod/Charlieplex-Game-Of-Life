import game_board

import board
import busio as io
import adafruit_is31fl3731

from time import sleep

if __name__ == "__main__":
    i2c = io.I2C(board.SCL, board.SDA)
    display = adafruit_is31fl3731.CharlieWing(i2c)

    game = game_board.Board(15, 7)
    counter = 0
    while True:
        game.show_board(display)
        game.next_gen()
        sleep(0.05)
        game.check_dead_state()
