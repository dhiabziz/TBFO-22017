import configPDA
from PDA import PDA
from htmlReader import readHTML

# path = "../../test/" + input("File html: ")
# config = configPDA.readConfig(path)
# word = input("Input: ")
# startState = config['starting_state']
# startStack = [config['starting_stack']]
# for i in config:
#     print(config[i])
# if PDA(startState, word, startStack, config):
#     print("Accepted")
# else:
#     print("Syntax Error")

# print(readHTML(path))

from re import search

attr = 'src'
text = '<img src=”./welcome.jpeg”>'
if search(f'{attr}=("(.*)"|\'(.*)\'|”(.*)”)', text):
    print("Acc")
else:
    print("reject")