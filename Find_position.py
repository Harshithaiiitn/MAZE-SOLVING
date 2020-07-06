
def test_find_position():
    assert find_position('b', [['F', 'X', 'F', 'F', 'F', 'X'],
                            ['g1', 'F', 'F', 'F', 'F', 'e'],
                            ['F', 'b', 'F', 'F', 'F', 'F'],
                            ['X', 'F', 'g2', 'F', 'F', 'X'],
                            ['F', 'X', 'F', 'F', 'F', 'F'],
                            ['F', 'F', 'F', 'F', 'F', 'F']]) == [2, 1],"Not showing exact position in the board"


def find_position(person,board):
    for row in range(0,len(board)):
        for col in range(0,len(board)):
            if board[row][col]==person:
                position_row,position_column=row,col
    positions=[position_row,position_column]
    return positions


    
if __name__=="__main__":

    test_find_position()
