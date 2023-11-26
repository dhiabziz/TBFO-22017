import os

def readConfig(path):
    if(os.path.isfile(path)):
        try:
            with open(path) as file:
                lines = []
                for line in file:
                    lines.append(line.rstrip())
        except IOError as e:
            print("File tidak berhasil dibuka!")
            exit()
    else:
        print(path, "Tidak ditemukan! Cek nama file")
        exit()
    
    productionLines = lines[6:]
    productions = []
    for production in productionLines:
        productions.append(production.rstrip().split())
    
    config = {
        'total_states' : lines[0].split(),
        'input_symbols' : lines[1].split(),
        'stack_symbols' : lines[2].split(),
        'starting_state' : lines[3][0],
        'starting_stack' : lines[4][0],
        'accepting_state' : lines[5].split(),
        'productions' : productions
    }
    return config
