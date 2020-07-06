from move_person_right import move_person_right
from check_exit import check_exit

def test_moving_person_right():
    assert moving_person_right(1,'rrrr', [['F', 'X', 'F', 'F', 'F', 'X'],
                                  ['g1', 'F', 'F', 'F', 'F', 'e'],
                                  ['F', 'b', 'F', 'F', 'F', 'F'],
                                  ['X', 'F', 'g2', 'F', 'F', 'X'],
                                  ['F', 'X', 'F', 'F', 'F', 'F'],
                                  ['F', 'F', 'F', 'F', 'F', 'F']] ,
                               [[2, 1], [1, 0], [3, 2], [1, 5]])==[3,
                            'false', [['F', 'X', 'F', 'F', 'F', 'X'],
                                      ['F', 'F', 'F', 'F', 'g1', 'e'],
                                      ['F', 'F', 'F', 'F', 'F', 'b'],
                                      ['X', 'F', 'F', 'F', 'g2', 'X'],
                                      ['F', 'X', 'F', 'F', 'F', 'F'],
                                      ['F', 'F', 'F', 'F', 'F', 'F']], [[2, 5], [1, 4], [3, 4]]],"Invalid Right Moves"


def moving_person_right(count,input_sequence,board,current_positions):
    moves_count=0
    result=move_person_right('b',board,current_positions[0])
    b_win,b_lose,flag,board,current_positions[0]=result[0],result[1],result[2],result[3],result[4]
    moves_count=moves_count+flag
    result=move_person_right('g1',board,current_positions[1])
    win,g1_lose,flag,board,current_positions[1]=result[0],result[1],result[2],result[3],result[4]
    moves_count=moves_count+flag
    result=move_person_right('g2',board,current_positions[2])
    win,g2_lose,flag,board,current_positions[2]= result[0],result[1],result[2],result[3],result[4]
    moves_count=moves_count+flag
    winners_list=[g1_lose,g2_lose,b_lose,b_win]
    success=check_exit(winners_list,count,input_sequence,board)
    current_positions=[current_positions[0],current_positions[1],current_positions[2]]
    return [moves_count,success,board,current_positions]



if __name__=="__main__":
    test_moving_person_right()
