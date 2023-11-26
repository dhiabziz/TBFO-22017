import sys
from PDABONUS import PDABONUS
from htmlReader import readHTML
from configPDA import readConfig

tokenTag = {
    '1': 'html', 
    '2': 'head', 
    '3': 'body', 
    '4': 'title', 
    '5': 'script', 
    '6': 'link', 
    '7': 'h1', 
    '8': 'h2', 
    '9': 'h3', 
    'a': 'h4', 
    'b': 'h5', 
    'c': 'h6', 
    'd': 'p', 
    'e': 'br', 
    'f': 'em', 
    'g': 'b', 
    'h': 'abbr', 
    'i': 'strong', 
    'j': 'small', 
    'k': 'hr', 
    'l': 'div', 
    'm': 'a', 
    'n': 'img', 
    'o': 'button', 
    'p': 'form', 
    'q': 'input', 
    'r': 'table', 
    's': 'tr', 
    't': 'th', 
    'u': 'td'
}

tokenAttribut = {
    'A': 'id', 
    'B': 'class', 
    'C': 'style', 
    'D': 'rel', 
    'E': 'href', 
    'F': 'src', 
    'G': 'alt', 
    'H': 'type', 
    'I': 'action', 
    'J': 'method'
}

tokenNilaiAttribut = {
    'K': 'submit', 
    'L': 'reset', 
    'M': 'button', 
    'N': 'GET', 
    'O': 'POST', 
    'P': 'text', 
    'Q': 'password', 
    'R': 'email', 
    'S': 'number', 
    'T': 'checkbox'
}

def main():
    if (len(sys.argv) != 3):
        print("Error: Argumen Program tidak valid!")
        print("Format Command: python main.py (FileConfig).txt (FileHTML).html")
    else:
        config = readConfig("./"+sys.argv[1])
        word = readHTML("../../test/"+sys.argv[2])
        startState = config['starting_state']
        startStack = [config['starting_stack']]

        error = (len(word), startState, word, [])
        result = PDABONUS(startState, word, startStack, config, error)
        if result[0]:
            print("Accepted")
        else:
            print("Syntax Error: ")
            print(result[1])
            print("  ", end='')
            state = result[1][1]
            input = result[1][2]
            stack = result[1][3]
            top = stack[-1]
            if (top == '*'): # Error Attribute
                if (result[1][3][-2] in tokenTag):
                    print(f'Attribut pada Tag <{tokenTag[result[1][3][-2]]}> tidak valid.')
                else:
                    print("Error Attribute.")
            elif (state == '3' and top == '1'): # Error Tag Body
                print("Tag <body> wajib ada setelah <head>.")
            elif (state == '1' and top == '1'): # Tag Head belum ada
                if (input[0] in tokenTag):
                    print("Tag <head> wajib ada setelah <html>.")
                elif (input[0] == '/'):
                    print("Tag <head> wajib ada setelah <html>.")
                else:
                    print("Error di tag <html>.")
            elif (top == '/'): # Error Closing Tag
                if ((state in tokenTag) and (input[0] in tokenTag)):
                    print(f'Tag <{tokenTag[state]}> tidak bisa ditutup oleh Closing Tag </{tokenTag[input[0]]}>.')
                elif (state in tokenTag) and (input[0] == '!'):
                    print(f'Tag <{tokenTag[state]}> tidak bisa ditutup karena Closing Tag tidak valid.')
                else:
                    print("Error Closing Tag.")
            elif (input[0] == '/'): # Error Closing Tag
                if ((state in tokenTag) and (input[1] in tokenTag)):
                    print(f'Tag <{tokenTag[state]}> tidak bisa ditutup oleh Closing Tag </{tokenTag[input[1]]}>.')
                elif (state in tokenTag) and (input[1] == '!'):
                    print(f'Tag <{tokenTag[state]}> tidak bisa ditutup karena Closing Tag tidak valid.')
                else:
                    print("Error Closing Tag.")
            elif (top in tokenTag): # Error Tag
                print(f'Kesalahan di Tag: <{tokenTag[top]}>.')
            elif (top in tokenAttribut): # Error Attribute
                print(f'Kesalahan di Attribute: "{tokenAttribut[top]}".')
            elif (top in tokenNilaiAttribut): # Error Attribute Value
                print(f'Kesalahan di Attribute Value: "{tokenNilaiAttribut[top]}".')
            else:
                print("Error belum di handle.")

if __name__ == "__main__":
    main()