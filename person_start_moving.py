from get_person_position import get_person_position
from moving_person_up import moving_person_up
from moving_person_left import moving_person_left
from moving_person_right import moving_person_right
from moving_person_down import moving_person_down
from display import display
import io
import sys

def test_person_start_moving():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    person_start_moving([['F', 'X', 'F', 'F', 'F', 'X'],
                  ['g1', 'F', 'F', 'F', 'F', 'e'],
                  ['F', 'b', 'F', 'F', 'F', 'F'],
                  ['X', 'F', 'g2', 'F', 'F', 'X'],
                  ['F', 'X', 'F', 'F', 'F', 'F'],
                  ['F', 'F', 'F', 'F', 'F', 'F']],
                 'uruuu')
    sys.stdout = sys.__stdout__
    print('Captured',capturedOutput.getvalue())


def person_start_moving(board,input_sequence):
    positions=get_person_position('g1',board)
    guard1_row,guard1_column=positions[0],positions[1]
    positions=get_person_position('g2',board)
    guard2_row,guard2_column=positions[0],positions[1]
    positions=get_person_position('b',board)
    brnjolf_row,brnjolf_column=positions[0],positions[1]
    positions=get_person_position('e',board)
    exit_row,exit_column=positions[0],positions[1]
    positions_list=[[brnjolf_row,brnjolf_column],[guard1_row,guard1_column],[guard2_row,guard2_column],[exit_row,exit_column]]
    count=0
    for direction in range(0,len(input_sequence)):
        count=count+1
        moves_count=0
        if input_sequence[direction] =='l':
            result= moving_person_left(count,input_sequence,board,positions_list)
            moves,success,board,positions_list=result[0],result[1],result[2],result[3]
            moves_count=moves_count+moves
            if success=='yes' or success=='fail':
                break 
        elif input_sequence[direction] == 'r':
            result=moving_person_right(count,input_sequence,board,positions_list)
            moves,success,board,positions_list=result[0],result[1],result[2],result[3]
            moves_count=moves_count+moves
            if success=='yes' or success=='fail':
                break

        elif input_sequence[direction] == 'u':
            result=moving_person_up(count,input_sequence,board,positions_list)
            moves,success,board,positions_list=result[0],result[1],result[2],result[3]
            moves_count=moves_count+moves
            if success=='yes' or success=='fail':
                break

        elif input_sequence[direction] == 'd':
            result=moving_person_down(count,input_sequence,board,positions_list)
            moves,success,board,positions_list=result[0],result[1],result[2],result[3]
            moves_count=moves_count+moves
            if success=='yes' or success=='fail':
                break
        if moves_count==0 and direction>=3:
            print("undecidable : "+str(direction+1)+" moves executed out of "+str(len(input_sequence)))
            print('Displaying board after moves:')
            board=display(board)
            break
        else:
            continue



if __name__=="__main__":

    test_person_start_moving()
