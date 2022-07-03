import keyboard
# from array import *

class Grid:
    def __init__(self, width, height):
        self.grid = [[None for w in range(width)] for h in range(height)]
        for h in range(height):
            for w in range(width):
                self.grid[h][w] = '#'
    
    def draw(self):
        for x in self.grid:
            for y in x:
                print(y, end = "")
            print()

if __name__ == "__main__":
    grid = Grid(20, 10)
    grid.draw()
