import keyboard
from grid import Grid
from player import Player

if __name__ == "__main__":
    grid = Grid(20, 10)
    player = Player(15, 8)
    grid.add_entity(player)
    grid.draw()
