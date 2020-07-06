from person_start_moving import person_start_moving
from display import display
import sys
import io

def test_file_parser():
   capturedOutput = io.StringIO()
   sys.stdout = capturedOutput
   file_parser('board.txt','uruu')
   sys.stdout = sys.__stdout__
   print('Captured',capturedOutput.getvalue())

def file_parser(input_file,input_sequence):
        try:
            board = open(input_file).read()
            print('File readed successfully!!')
            board=[item.split() for item in board.split('\n')]
            display(board)
            person_start_moving(board,input_sequence)
        except:
            print('File not found')


if __name__=='__main__':

    test_file_parser()

