# error --> (lenMin, state, input, stack)
# return --> (True/False, error)

def PDABonus(state, input, stack, config, error):
    # Input sudah kosong
    if (len(input) == 0):
        # Cek State ada di Accepting States (Basis)
        if (state in config['accepting_state']):
            return (True, error)
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
                    
                    res = PDABonus(prod[3], input[1:], nextStack, config, error)
                    if (res[1][0] < error[0]):
                        error = res[1]
                    if (res[0]):
                        return (True, error)
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
                    
                    res = PDABonus(prod[3], nextInput, nextStack, config, error)
                    if (res[1][0] < error[0]):
                        error = res[1]
                    if (res[0]): # Cek next 
                        return (True, error)
    # Gagal
    if (len(input) < error[0]):
        error = (len(input), state, input, stack)
    return (False, error)