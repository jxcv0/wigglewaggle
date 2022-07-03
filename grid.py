import os

class Grid:
    def __init__(self, width, height):
        self.height = height;
        self.width = width
        self.entities = list()
        self.update()
    
    def draw(self):
        os.system("clear")
        self.update()
        for x in self.grid:
            for y in x:
                print(y, end = "")
            print()

    def update(self):
        self.grid = [[None for w in range(self.width)] for h in range(self.height)]
        for h in range(self.height):
            for w in range(self.width):
                if h == 0 or w == 0:
                    self.grid[h][w] = '#'
                    continue
                elif h == self.height - 1 or w == self.width - 1:
                    self.grid[h][w] = '#'
                    continue
                else:
                    self.grid[h][w] = ' '
        for e in self.entities:
            if e.y_pos < 1:
                e.y_pos = 1
            if e.y_pos > self.height - 2:
                e.y_pos = self.height - 2
            if e.x_pos < 1:
                e.x_pos = 1
            if e.x_pos > self.width - 2:
                e.x_pos = self.width - 2
            self.grid[e.y_pos][e.x_pos] = e.char

    def add_entity(self, entity):
        self.entities.append(entity)
