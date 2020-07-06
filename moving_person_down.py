from move_person_down import move_person_down
from check_exit import check_exit

def test_MovingDown():
    assert moving_person_down(1,'dddd', [['F', 'X', 'F', 'F', 'F', 'X'],
                                 ['g1', 'F', 'F', 'F', 'F', 'e'],
                                 ['F', 'b', 'F', 'F', 'F', 'F'],
                                 ['X', 'F', 'g2', 'F', 'F', 'X'],
                                 ['F', 'X', 'F', 'F', 'F', 'F'],
                                 ['F', 'F', 'F', 'F', 'F', 'F']],
                      [[2, 1], [1, 0], [3, 2], [1, 5]])==[3, 'false', [['F', 'X', 'F', 'F', 'F', 'X'],
                                                                        ['F', 'F', 'F', 'F', 'F', 'e'],
                                                                        ['g1', 'F', 'F', 'F', 'F', 'F'],
                                                                       ['X', 'b', 'F', 'F', 'F', 'X'],
                                                                       ['F', 'X', 'F', 'F', 'F', 'F'],
                                                                       ['F', 'F', 'g2', 'F', 'F', 'F']],
                                                           [[3, 1], [2, 0], [5, 2]]],"Not performing valid Down moves"



def moving_person_down(count,input_sequence,board,current_positions):
    moves_count=0
    result=move_person_down('b',board,current_positions[0])
    b_win,b_lose,flag,board,current_positions[0]=result[0],result[1],result[2],result[3],result[4]
    moves_count=moves_count+flag
    result=move_person_down('g1',board,current_positions[1])
    win,g1_lose,flag,board,current_positions[1]=result[0],result[1],result[2],result[3],result[4]
    moves_count=moves_count+flag
    result=move_person_down('g2',board,current_positions[2])
    win,g2_lose,flag,board,current_positions[2]=result[0],result[1],result[2],result[3],result[4]
    moves_count=moves_count+flag
    winning_list=[g1_lose,g2_lose,b_lose,b_win]
    success=check_exit(winning_list,count,input_sequence,board)
    current_positions=[current_positions[0],current_positions[1],current_positions[2]]
    return [moves_count,success,board,current_positions]



if __name__=="__main__":
    test_MovingDown()
