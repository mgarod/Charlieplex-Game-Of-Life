# Charlieplex-Game-Of-Life
An implementation of Conway's Game of Life on an Adafruit Feather Express M0 and a 15x7 Charlieplex matrix using CircuitPython

This repository takes a very old pure python implementation of Conway's Game of Life that I did, and adapted it to work on an [Adafruit Feather Express M0](https://www.adafruit.com/product/3403) with an attached [Adafruit 15x7 CharliePlex LED Matrix Display FeatherWing - Blue](https://www.adafruit.com/product/3137) and written with CircuitPython.

I randomize the board after 50 generations (which takes about 30 seconds) to prevent a deadlock state of the cells, or to refresh when the entire board has died.

Right now, the transition animation between generations is visibly slow, which is to say if the board is full you can see a wave overtake the cells from left to right. I would like to make this near instantaneous, but I doubt this can be done due to the hardware constraints of the board.

Theoretically, this code could be adapted to just about any led matrix that compatible with CircuitPython. You'd simply have to change the `display` object, the size of the objects, and the way the display object manipulates pixels.
