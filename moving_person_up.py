from move_person_up import move_person_up
from check_exit import check_exit

def test_moving_person_up():
    assert moving_person_up(1,'uruu', [['F', 'X', 'F', 'F', 'F', 'X'],
                               ['g1', 'F', 'F', 'F', 'F', 'e'],
                               ['F', 'b', 'F', 'F', 'F', 'F'],
                               ['X', 'F', 'g2', 'F', 'F', 'X'],
                               ['F', 'X', 'F', 'F', 'F', 'F'],
                               ['F', 'F', 'F', 'F', 'F', 'F']],
                    [[2, 1], [1, 0], [3, 2], [1, 5]])==[3, 'false', [['g1', 'X', 'g2', 'F', 'F', 'X'],
                                                                    ['F', 'b', 'F', 'F', 'F', 'e'],
                                                                     ['F', 'F', 'F', 'F', 'F', 'F'],
                                                                    ['X', 'F', 'F', 'F', 'F', 'X'],
                                                                     ['F', 'X', 'F', 'F', 'F', 'F'],
                                                                     ['F', 'F', 'F', 'F', 'F', 'F']],
                                         [[1, 1], [0, 0], [0, 2]]],"Invalid Up moves"



def moving_person_up(count,input_sequence,board,current_positions):
    moves_count=0
    result=move_person_up('b',board,current_positions[0])
    b_win,b_lose,flag,board,current_positions[0]=result[0],result[1],result[2],result[3],result[4]
    moves_count=moves_count+flag
    result=move_person_up('g1',board,current_positions[1])
    win,g1_lose,flag,board,current_positions[1]=result[0],result[1],result[2],result[3],result[4]
    moves_count=moves_count+flag
    result=move_person_up('g2',board,current_positions[2])
    win,g2_lose,flag,board,current_positions[2]=result[0],result[1],result[2],result[3],result[4]
    moves_count=moves_count+flag
    winners_list=[g1_lose,g2_lose,b_lose,b_win]
    success=check_exit(winners_list,count,input_sequence,board)
    current_positions=[current_positions[0],current_positions[1],current_positions[2]]
    return [moves_count,success,board,current_positions]


if __name__=="__main__":
    test_moving_person_up()
