tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):
    width = len(table[0])
    height = len(table)
    colWidths = [0] * len(tableData)


    for row,values in enumerate(tableData):
        maxLen = 0
        for value in values:
            length = len(value)
            if maxLen < length:
                maxLen = length

        colWidths[row] = maxLen

    for x in range(width):
        for y in range(height):
            length = colWidths[y]
            print(table[y][x].rjust(length),end=' ')
        print()


printTable(tableData)
