def test_move_person_down():
    assert move_person_down('b',[['F', 'X', 'F', 'F', 'F', 'X'],
                         ['g1', 'F', 'F', 'F', 'F', 'e'],
                         ['F', 'b', 'F', 'F', 'F', 'F'],
                         ['X', 'F', 'g2', 'F', 'F', 'X'],
                         ['F', 'X', 'F', 'F', 'F', 'F'],
                         ['F', 'F', 'F', 'F', 'F', 'F']],
                    [2,1])==['false', 'false',1, [['F', 'X', 'F', 'F', 'F', 'X'],
                                                  ['g1', 'F', 'F', 'F', 'F', 'e'],
                                                  ['F', 'F', 'F', 'F', 'F', 'F'],
                                                  ['X', 'b', 'g2', 'F', 'F', 'X'],
                                                  ['F', 'X', 'F', 'F', 'F', 'F'],
                                                  ['F', 'F', 'F', 'F', 'F', 'F']], [3, 1]], "Not performing Down move perfectly"


def move_person_down(person,board,current_position):
    row=current_position[0]
    current_row=current_position[0]+1
    win='false'
    lose='false'
    flag=0
    while(current_row<len(board)):
        if board[current_row][current_position[1]]=='F':
            board[current_row][current_position[1]]=person
            board[current_row-1][current_position[1]]='F'
            row=current_row
            current_row=current_row+1
            flag=1
        elif (board[current_row][current_position[1]]=='e' and (person=='g1' or person=='g2'))or board[current_row][current_position[1]]=='X':
            break
        elif (board[current_row][current_position[1]]=='g1' or board[current_row][current_position[1]]=='g2') and person=='b':
            board[current_row][current_position[1]]=board[current_row][current_position[1]]
            lose='true'
            break
        elif (person=='g1' or person=='g2') and board[current_row][current_position[1]]=='b':
            board[current_row][current_position[1]]=person
            board[current_row-1][current_position[1]]='F'
            lose='true'
            break

        elif board[current_row][current_position[1]]=='e' and person=='b':
            board[current_row-1][current_position[1]]='F'
            win='true'
            break
    current_position=[row,current_position[1]]
    return [win,lose,flag,board,current_position]


if __name__=="__main__":
    test_move_person_down()
