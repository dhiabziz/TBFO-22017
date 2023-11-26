def PDA(state, input, stack, config):
    # Input sudah kosong
    if (len(input) == 0):
        # Cek State ada di Accepting States (Basis)
        if (state in config['accepting_state']):
            return True
        else: # Cek Transition function yang menerima epsilon
            for prod in config['productions']:
                if (prod[0] == state and prod[1] == '^' and prod[2] == stack[len(stack)-1]):
                    nextStack = stack.copy()
                    nextStack.pop()
                    if (len(prod[4]) == 2):
                        nextStack.append(prod[4][1])
                        nextStack.append(prod[4][0])
                    elif (prod[4] != '^'):
                        nextStack.append(prod[4])
                    
                    if (PDA(prod[3], input[1:], nextStack, config)):
                        return True
    else: # Input belum kosong
        for prod in config['productions']: # Cek tiap production yang memenuhi
            if (prod[0] == state and (prod[1] == input[0] or prod[1] == '^') and prod[2] == stack[len(stack)-1]):
                    nextStack = stack.copy()
                    nextStack.pop()
                    if (len(prod[4]) == 2):
                        nextStack.append(prod[4][1])
                        nextStack.append(prod[4][0])
                    elif (prod[4] != '^'):
                        nextStack.append(prod[4])
                    
                    if (prod[1] == input[0]):
                        nextInput = input[1:]
                    else: # Menerima input epsilon
                        nextInput = input[0:]
                    
                    if (PDA(prod[3], nextInput, nextStack, config)): # Cek next 
                        return True
    # Gagal
    return False