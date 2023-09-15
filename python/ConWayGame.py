import copy
import random
import time

WIDTH = 60
HEIGHT = 20

# Create a list of list for the cells:
nextCells = []

for y in range(HEIGHT):
    columns = []
    for x in range(WIDTH):
        randNum = random.randint(0, 1)
        if randNum == 0:
            columns.append(' ')
        else:
            columns.append('#')
    nextCells.append(columns)

def printMapCell(cells):
    for x in range(HEIGHT):
        for y in range(WIDTH):
            print(cells[x][y],end='')
        print('')


def nextMapCell(cells):
    newCells = copy.deepcopy(cells)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            up = (y - 1) % HEIGHT
            down = (y + 1) % HEIGHT

            if left < 0:
                left = WIDTH - 1

            if up < 0:
                up = HEIGHT - 1

            aliveNum = 0

            if cells[y][left] == '#':
                aliveNum += 1

            if cells[up][left] == '#':
                aliveNum += 1

            if cells[down][left] == '#':
                aliveNum += 1

            if cells[y][right] == '#':
                aliveNum += 1

            if cells[up][right] == '#':
                aliveNum += 1

            if cells[down][right] == '#':
                aliveNum += 1

            if cells[up][x] == '#':
                aliveNum += 1

            if cells[down][x] == '#':
                aliveNum += 1

            if cells[y][x] == ' ' and aliveNum == 3:
                newCells[y][x] = '#'
            elif cells[y][x] == '#' and (aliveNum == 3 or aliveNum == 2):
                newCells[y][x] = ' '
            else:
                newCells[y][x] = ' '
    time.sleep(1)
    print('{')
    printMapCell(newCells)
    print('}')
    nextMapCell(newCells)



printMapCell(nextCells)
nextMapCell(nextCells)
