import sys
from PDA import PDA
from htmlReader import readHTML
from configPDA import readConfig

def main():
    if (len(sys.argv) != 3):
        print("Error: Argumen Program tidak valid!")
        print("Format Command: python main.py (FileConfig).txt (FileHTML).html")
    else:
        word = readHTML("../../test/"+sys.argv[2])
        config = readConfig("../config/"+sys.argv[1])
        startState = config['starting_state']
        startStack = [config['starting_stack']]
        if PDA(startState, word, startStack, config):
            print("Accepted")
        else:
            print("Syntax Error")
    

if __name__ == "__main__":
    main()