DIR_UP = "u"
DIR_DOWN = "d"
DIR_LEFT = "l"
DIR_RIGHT = "r"
BLANK_PIECE = "Z"
board_size = (4, 4)

def make_move(board, position, direction):
    row = position[0]
    column = position[1]

    # execute the move first
    # swap the two cells
    piece = board[row][column][:]
    if direction == DIR_UP:
        board[row][column] = board[row - 1][column]
        board[row - 1][column] = piece
    if direction == DIR_DOWN:
        board[row][column] = board[row + 1][column]
        board[row + 1][column] = piece
    if direction == DIR_LEFT:
        board[row][column] = board[row][column - 1]
        board[row][column - 1] = piece
    if direction == DIR_RIGHT:
        board[row][column] = board[row][column + 1]
        board[row][column + 1] = piece
    # move finish

    # check if there are 2*2 square with same colour
    # down to up, left to right as required
    # excluding the last row and column
    elimination = False
    for rows in range(len(board) - 1, -1, -1):
        for cols in range(len(board[0]) - 1):
            if (board[rows][cols] == board[rows - 1][cols]
                    == board[rows][cols + 1]
                    == board[rows - 1][cols + 1]
                    and board[rows][cols] != BLANK_PIECE):
                # Eliminate the square
                board[rows][cols] = BLANK_PIECE
                board[rows - 1][cols] = BLANK_PIECE
                board[rows][cols + 1] = BLANK_PIECE
                board[rows - 1][cols + 1] = BLANK_PIECE
                elimination = True

    if elimination:
        # search for squares from down to up, left to right
        for row1 in range(len(board) - 1, -1, -1):
            for col1 in range(len(board[0]) - 1):
                # check for blanks square
                if (board[row1][col1] == BLANK_PIECE
                        and board[row1 - 1][col1] == BLANK_PIECE
                        and board[row1][col1 + 1] == BLANK_PIECE
                        and board[row1 - 1][col1 + 1] == BLANK_PIECE):

                    # move the square down
                    # the name row1, col1 are just row and col
                    # but to avoid use the same name again
                    down = False
                    if row1 == len(board) - 1:
                        down = True
                    else:
                        temp = board[row1][col1][:]
                        board[row1][col1] = board[row1 + 1][col1]
                        board[row1 + 1][col1] = temp

                        temp = board[row1][col1 + 1][:]
                        board[row1][col1 + 1] = board[row1 + 1][col1 + 1]
                        board[row1 + 1][col1 + 1] = temp

                        temp = board[row1 - 1][col1 + 1][:]
                        board[row1 - 1][col1 + 1] \
                            = board[row1][col1 + 1]
                        board[row1 - 1][col1 + 1] = temp

                        temp = board[row1 - 1][col1][:]
                        board[row1 - 1][col1] = board[row1][col1]
                        board[row1][col1] = temp
                        # now the square is at the bottom row

                        # move the square to the right
                    if down:
                        for row1 in range(len(board), -2, -1):
                            for col1 in range(len(board) - 2):
                                temp = board[row1 - 1][col1 + 1][:]
                                board[row1 - 1][col1 + 1] \
                                    = board[row1 - 1][col1 + 2]
                                board[row1 - 1][col1 + 2] = temp

                                temp = board[row1][col1 + 1][:]
                                board[row1][col1 + 1] \
                                    = board[row1][col1 + 2]
                                board[row1][col1 + 2] = temp

                                temp = board[row1][col1][:]
                                board[row1][col1] \
                                    = board[row1][col1 + 1]
                                board[row1][col1 + 1] = temp

                                temp = board[row1 - 1][col1][:]
                                board[row1 - 1][col1] \
                                    = board[row1 - 1][col1]
                                board[row1 - 1][col1] = temp
                                # now the square is at
                                # the bottom right

                    return board

print(make_move([["C", "A", "B", "C"], ["A", "B", "C", "A"], ["A", "B", "B", "C"], ["A", "A", "A", "A"]],
                              (0, 2), "d"))
print(make_move([["C", "A", "B", "C"], ["A", "B", "C", "A"], ["A", "B", "B", "A"], ["A", "C", "A", "A"]], (0, 2), "d"))