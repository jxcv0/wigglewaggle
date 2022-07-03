class Grid:
    def __init__(self, width, height):
        self.grid = [[None for w in range(width)] for h in range(height)]
        for h in range(height):
            for w in range(width):
                if h == 0 or w == 0:
                    self.grid[h][w] = '#'
                    continue
                elif h == height - 1 or w == width - 1:
                    self.grid[h][w] = '#'
                    continue
                else:
                    self.grid[h][w] = ' '
    
    def draw(self):
        for x in self.grid:
            for y in x:
                print(y, end = "")
            print()
