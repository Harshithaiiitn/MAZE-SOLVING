def test_move_person_up():
    assert move_person_up('b',[['F', 'X', 'F', 'F', 'F', 'X'],
                       ['g1', 'F', 'F', 'F', 'F', 'e'],
                       ['F', 'b', 'F', 'F', 'F', 'F'],
                       ['X', 'F', 'g2', 'F', 'F', 'X'],
                       ['F', 'X', 'F', 'F', 'F', 'F'],
                       ['F', 'F', 'F', 'F', 'F', 'F']],
                    [2,1])==['false', 'false', 1, [['F', 'X', 'F', 'F', 'F', 'X'],
                                                   ['g1', 'b', 'F', 'F', 'F', 'e'],
                                                   ['F', 'F', 'F', 'F', 'F', 'F'],
                                                   ['X', 'F', 'g2', 'F', 'F', 'X'],
                                                   ['F', 'X', 'F', 'F', 'F', 'F'],
                                                   ['F', 'F', 'F', 'F', 'F', 'F']],
                             [1, 1]], "Not a valid Up move"


def move_person_up(person,board,current_positions):
    row=current_positions[0]
    current_row=current_positions[0]-1
    win='false'
    lose='false'
    flag=0
    while(current_row>=0):
        if board[current_row][current_positions[1]]=='F':
            board[current_row][current_positions[1]]=person
            board[current_row+1][current_positions[1]]='F'
            row=current_row
            current_row=current_row-1
            flag=1
        elif (board[current_row][current_positions[1]]=='e' and (person=='g1' or person=='g2')) or board[current_row][current_positions[1]]=='X':
            break
        elif (board[current_row][current_positions[1]]=='g1' or board[current_row][current_positions[1]]=='g2') and person=='b':
            board[current_row][current_positions[1]]=board[current_row][current_positions[1]]
            board[current_row+1][current_positions[1]]='F'
            lose='true'
            break
        elif (person=='g1' or person=='g2') and board[current_row][current_positions[1]]=='b':
            board[current_row][current_positions[1]]=person
            board[current_row+1][current_positions[1]]='F'
            lose='true'
            break

        elif board[current_row][current_positions[1]]=='e' and person=='b':
            board[current_row+1][current_positions[1]]='F'
            win='true'
            break
    current_positions=[row,current_positions[1]]
    return [win,lose,flag,board,current_positions]



if __name__=="__main__":
    test_move_person_up()
