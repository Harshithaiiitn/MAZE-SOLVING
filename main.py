import sys
from file_parser import file_parser

if __name__=="__main__":
    input_file=sys.argv[1]
    input_sequence=input('Enter input sequence : ')
    file_parser(input_file,input_sequence)
    
