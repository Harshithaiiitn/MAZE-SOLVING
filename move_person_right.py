def test_move_person_right():
    assert move_person_right('b',[['F', 'X', 'F', 'F', 'F', 'X'],
                          ['g1', 'F', 'F', 'F', 'F', 'e'],
                         ['F', 'b', 'F', 'F', 'F', 'F'],
                          ['X', 'F', 'g2', 'F', 'F', 'X'],
                         ['F', 'X', 'F', 'F', 'F', 'F'],
                          ['F', 'F', 'F', 'F', 'F', 'F']],
                    [2,1])==['false', 'false', 1, [['F', 'X', 'F', 'F', 'F', 'X'],
                                                   ['g1', 'F', 'F', 'F', 'F', 'e'],
                                                   ['F', 'F', 'F', 'F', 'F', 'b'],
                                                   ['X', 'F', 'g2', 'F', 'F', 'X'],
                                                   ['F', 'X', 'F', 'F', 'F', 'F'],
                                                   ['F', 'F', 'F', 'F', 'F', 'F']],
                             [2, 5]], "Not a valid Right move"


def move_person_right(person,board,current_positions):
    column=current_positions[1]
    current_column=current_positions[1]+1
    win='false'
    lose='false'
    flag=0
    while(current_column<len(board)):
        if board[current_positions[0]][current_column]=='F':
            board[current_positions[0]][current_column]=person
            board[current_positions[0]][current_column-1]='F'
            column=current_column
            current_column=current_column+1
            flag=1
        elif (board[current_positions[0]][current_column]=='e' and (person=='g1' or person=='g2')) or board[current_positions[0]][current_column]=='X':
            break
        elif board[current_positions[0]][current_column]=='g1'  and person=='b':
            board[current_positions[0]][current_column]='g1'
            board[current_positions[0]][current_column-1]='F'
            lose='true'
            break
        elif  board[current_positions[0]][current_column]=='g2' and person=='b':
            board[current_positions[0]][current_column]='g2'
            board[current_positions[0]][current_column-1]='F'
            lose='true'
            break
        elif (person=='g1' or person=='g2') and board[current_positions[0]][current_column]=='b':
            board[current_positions[0]][current_column]=person
            board[current_positions[0]][current_column-1]='F'
            lose='true'
            break

        elif board[current_positions[0]][current_column]=='e' and person=='b':
            board[current_positions[0]][current_column-1]='F'
            win='true'
            break
    current_positions=[current_positions[0],column]
    return [win,lose,flag,board,current_positions]


if __name__=="__main__":
    test_move_person_right()
