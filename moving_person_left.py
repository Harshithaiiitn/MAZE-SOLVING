from move_person_left import move_person_left
from check_exit import check_exit

def test_moving_person_left():
    assert moving_person_left(1,'lluu', [['F', 'X', 'F', 'F', 'F', 'X'],
                                 ['g1', 'F', 'F', 'F', 'F', 'e'],
                                 ['F', 'b', 'F', 'F', 'F', 'F'],
                                 ['X', 'F', 'g2', 'F', 'F', 'X'],
                                 ['F', 'X', 'F', 'F', 'F', 'F'],
                                 ['F', 'F', 'F', 'F', 'F', 'F']],
                               [[2, 1], [1, 0], [3, 2], [1, 5]])==[2, 'false', [['F', 'X', 'F', 'F', 'F', 'X'],
                                                                ['g1', 'F', 'F', 'F', 'F', 'e'],
                                                                ['b', 'F', 'F', 'F', 'F', 'F'],
                                                                ['X', 'g2', 'F', 'F', 'F', 'X'],
                                                                ['F', 'X', 'F', 'F', 'F', 'F'],
                                                                ['F', 'F', 'F', 'F', 'F', 'F']],
                                                                [[2, 0], [1, 0], [3, 1]]],"Invalid left moves"


def moving_person_left(count,input_sequence,board,position_list):
    moves_count=0
    result=move_person_left('b',board,position_list[0])
    b_win,b_lose,flag,board,position_list[0]=result[0],result[1],result[2],result[3],result[4]
    moves_count=moves_count+flag
    result=move_person_left('g1',board,position_list[1])
    win,g1_lose,flag,board,position_list[1]=result[0],result[1],result[2],result[3],result[4]
    moves_count=moves_count+flag
    result=move_person_left('g2',board,position_list[2])
    win,g2_lose,flag,board,position_list[2]=result[0],result[1],result[2],result[3],result[4]
    moves_count=moves_count+flag
    winners_list=[g1_lose,g2_lose,b_lose,b_win]
    success=check_exit(winners_list,count,input_sequence,board)
    position_list=[position_list[0],position_list[1],position_list[2]]
    return [moves_count,success,board,position_list]




if __name__=="__main__":
    test_moving_person_left()
