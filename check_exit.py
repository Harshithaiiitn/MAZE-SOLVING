
from display import display

def test_check_exit():
        assert check_exit(['false', 'false', 'false', 'false'],1,'rrr',
                     [['F', 'X', 'F', 'F', 'F', 'X'],
                      ['F', 'F', 'F', 'F', 'g1', 'e'],
                      ['F', 'F', 'F', 'F', 'F', 'b'],
                      ['X', 'F', 'F', 'F', 'g2', 'X'],
                      ['F', 'X', 'F', 'F', 'F', 'F'],
                      ['F', 'F', 'F', 'F', 'F', 'F']])=="false","Success value is not matching"

def check_exit(winners_list,count,input_sequence,board):
    success='false'
    if winners_list[0]=='true' or winners_list[1]=='true' or winners_list[2]=='true':
        print("lose:"+str(count)+" moves executed out of "+str(len(input_sequence)))
        print('Displaying board after moves:')
        board = display(board)
        success='fail'
    elif winners_list[3]=='true':
        print("win:"+str(count)+" moves executed out of "+str(len(input_sequence)))
        print('Displaying board after moves:')
        board = display(board)
        success='yes'
    return success


        
if __name__=="__main__":
    test_check_exit()
