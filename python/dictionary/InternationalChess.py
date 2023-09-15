name = 'bking'
name = name[1:len((name))]
print(name)


def checkIfTrue(cells):
    #   'pawn' * 8、'knight' * 2、'bishop' * 2、'rook' * 2、'queen'或'king'
    #   检测棋盘是否在8*8的格子内
    #   检测左右双方最多16个棋子，最多8个小兵
    chessPiece = {'pawn': 8, 'knight': 2, 'bishop': 2, 'rook': 2, 'queen': 1, 'king': 1}
    if len(cells) != 8:
        return False
    for value in cells.values():
        if (len(value) != 8):
            return False

    blackChessPiece = {}
    whiteChessPiece = {}

    for values in cells.values():
        for value in values:
            if value.startswith('b'):
                blackChessPiece.setdefault(value[1:len(value)], 0)
                blackChessPiece[value] = blackChessPiece[value] + 1
            elif value.startswith('w'):
                whiteChessPiece.setdefault(value[1:len(value)], 0)
                whiteChessPiece[value] = whiteChessPiece[value] + 1


    for key,value in blackChessPiece.items():
        if key not in chessPiece.keys():
            return False

        num = chessPiece.get(key)

        if value > num:
            return False


    for key,value in whiteChessPiece.items():
        if key not in chessPiece.keys():
            return False

        num = chessPiece.get(key)

        if value > num:
            return False
