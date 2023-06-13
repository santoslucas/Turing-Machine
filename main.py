import json
import sys

def turing_machine(mt: list, word: str) -> str:    
    numTrails = mt[0]
    alfa_in = mt[2]
    head = mt[4]
    space = mt[5]
    trans = mt[6]
    init = mt[7]
    finals = mt[8]
    
    
    # verifica se palavra esta no alfabeto:
    for it in word:
        if it not in alfa_in:
            return 'Não'

    # inicializa as fitas
    
    num_cells = len(word) + 1
    tape = [[space for _ in range(num_cells)] for _ in range(numTrails)]
    
    # inicializa a primeira fita
    for i in range(num_cells):
        if i == 0:
            tape[0][i] = head
        else:
            tape[0][i] = word[i-1]
    
    if num_cells == 1:
        for it in tape:
            it.append(space)
            num_cells += 1
    
    # maquina estados, transicoes
    len_tr = len(trans[0])
    idx_st1 = 0
    idx_st2 = numTrails+1
    idx_tr1 = 1
    idx_tr2 = idx_st2+1
    idx_dir = len_tr-1
    
    current = init
    posit = 1
    
    while True:
        numTrans = len(trans)
        didTrans = False
        
        for i in range(numTrans):
            if trans[i][idx_st1] == current:
                if trans[i][idx_tr1:idx_st2] == [linha[posit] for linha in tape]:
                    didTrans = True
                    
                    for j in range(numTrails):
                        tape[j][posit] = trans[i][j+idx_tr2]
                    current = trans[i][idx_st2]
                    
                    if trans[i][idx_dir] == '>':
                        posit += 1
                    elif trans[i][idx_dir] == '<':
                        posit -= 1
                
                    # print(tape)
                    # print(current + ' ' + str(posit))
                    # print('----------------------------------')
                    break
        if posit < 0:
            break
        elif posit >= num_cells:
            for it in tape:
                it.append(space)
                num_cells += 1
                    
        if didTrans == False:
            if current in finals:
                return 'Sim'
            else:
                return 'Não'
    return 'Não'              

# if len(sys.argv) == 2 :
#     word = ''
#     json_file = sys.argv[1]

if len(sys.argv) == 3:  
    word = sys.argv[2]
    json_file = sys.argv[1]
else:
    print('Usar: ./mt [MT] [Word]')
    exit()
    
with open(json_file) as file:
    mt = json.load(file)
    
print(turing_machine(mt['mt'], word))
    
