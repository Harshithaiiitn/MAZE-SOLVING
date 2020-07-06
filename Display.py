import io
import sys


def test_display():
   capturedOutput = io.StringIO()
   sys.stdout = capturedOutput
   display([['F', 'X', 'F', 'F', 'F', 'X'],
                    ['g1', 'F', 'F', 'F', 'F', 'e'],
                    ['F', 'b', 'F', 'F', 'F', 'F'],
                    ['X', 'F', 'g2', 'F', 'F', 'X'],
                    ['F', 'X', 'F', 'F', 'F', 'F'],
                    ['F', 'F', 'F', 'F', 'F', 'F']])
   sys.stdout = sys.__stdout__
   print('Captured',capturedOutput.getvalue())

def display(board):
    board_size=len(board)
    for row in range(0,board_size):
        for col in range(0,board_size):
            print("%-2s"%(board[row][col]),end='  ')
        print()
    return board

if __name__=="__main__":

    test_display()
