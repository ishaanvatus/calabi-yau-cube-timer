#implementation of the virtual cube
import random
cube = {
    'U': ['U0', 'U1', 'U2', 'U3', 'U4', 'U5', 'U6', 'U7', 'U8'], 
    'R': ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8'], 
    'F': ['F0', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8'], 
    'D': ['D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8'], 
    'L': ['L0', 'L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8'], 
    'B': ['B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8']
    }

U_clr = (255,255,255)
R_clr = (255, 0, 0)
F_clr = (0, 255, 0)
D_clr = (255, 255, 0)
L_clr = (255,140,0)
B_clr = (0, 0, 255)

def move_U():
    global cube
    U0 = cube['U'][0]
    U1 = cube['U'][1]
    U2 = cube['U'][2]
    U3 = cube['U'][3]
    U4 = cube['U'][4]
    U5 = cube['U'][5]
    U6 = cube['U'][6]
    U7 = cube['U'][7]
    U8 = cube['U'][8]

    R0 = cube['R'][0]
    R1 = cube['R'][1]
    R2 = cube['R'][2]

    F0 = cube['F'][0]
    F1 = cube['F'][1]
    F2 = cube['F'][2]

    L0 = cube['L'][0]
    L1 = cube['L'][1]
    L2 = cube['L'][2]

    B0 = cube['B'][0]
    B1 = cube['B'][1]
    B2 = cube['B'][2]

    cube['U'][0] = U6
    cube['U'][1] = U3
    cube['U'][2] = U0
    cube['U'][3] = U7
    cube['U'][4] = U4
    cube['U'][5] = U1
    cube['U'][6] = U8
    cube['U'][7] = U5
    cube['U'][8] = U2

    cube['R'][0] = B0
    cube['R'][1] = B1
    cube['R'][2] = B2

    cube['F'][0] = R0
    cube['F'][1] = R1
    cube['F'][2] = R2

    cube['L'][0] = F0
    cube['L'][1] = F1
    cube['L'][2] = F2

    cube['B'][0] = L0
    cube['B'][1] = L1
    cube['B'][2] = L2

def move_R():
    global cube
    R0 = cube['R'][0]
    R1 = cube['R'][1]
    R2 = cube['R'][2]
    R3 = cube['R'][3]
    R4 = cube['R'][4]
    R5 = cube['R'][5]
    R6 = cube['R'][6]
    R7 = cube['R'][7]
    R8 = cube['R'][8]

    U2 = cube['U'][2]
    U5 = cube['U'][5]
    U8 = cube['U'][8]

    F2 = cube['F'][2]
    F5 = cube['F'][5]
    F8 = cube['F'][8]

    D2 = cube['D'][2]
    D5 = cube['D'][5]
    D8 = cube['D'][8]

    B0 = cube['B'][0]
    B3 = cube['B'][3]
    B6 = cube['B'][6]

    cube['R'][0] = R6
    cube['R'][1] = R3
    cube['R'][2] = R0
    cube['R'][3] = R7
    cube['R'][4] = R4
    cube['R'][5] = R1
    cube['R'][6] = R8
    cube['R'][7] = R5
    cube['R'][8] = R2

    cube['U'][2] = F2
    cube['U'][5] = F5
    cube['U'][8] = F8

    cube['F'][2] = D2
    cube['F'][5] = D5
    cube['F'][8] = D8

    cube['D'][2] = B6
    cube['D'][5] = B3
    cube['D'][8] = B0

    cube['B'][0] = U8
    cube['B'][3] = U5
    cube['B'][6] = U2

def move_F():
    global cube
    F0 = cube['F'][0]
    F1 = cube['F'][1]
    F2 = cube['F'][2]
    F3 = cube['F'][3]
    F4 = cube['F'][4]
    F5 = cube['F'][5]
    F6 = cube['F'][6]
    F7 = cube['F'][7]
    F8 = cube['F'][8]

    U6 = cube['U'][6]
    U7 = cube['U'][7]
    U8 = cube['U'][8]

    R0 = cube['R'][0]
    R3 = cube['R'][3]
    R6 = cube['R'][6]

    D0 = cube['D'][0]
    D1 = cube['D'][1]
    D2 = cube['D'][2]

    L2 = cube['L'][2]
    L5 = cube['L'][5]
    L8 = cube['L'][8]

    cube['F'][0] = F6
    cube['F'][1] = F3
    cube['F'][2] = F0
    cube['F'][3] = F7
    cube['F'][4] = F4
    cube['F'][5] = F1
    cube['F'][6] = F8
    cube['F'][7] = F5
    cube['F'][8] = F2

    cube['U'][6] = L8
    cube['U'][7] = L5
    cube['U'][8] = L2

    cube['R'][0] = U6
    cube['R'][3] = U7
    cube['R'][6] = U8

    cube['D'][0] = R6
    cube['D'][1] = R3
    cube['D'][2] = R0

    cube['L'][2] = D0
    cube['L'][5] = D1
    cube['L'][8] = D2

def move_D():
    global cube
    D0 = cube['D'][0]
    D1 = cube['D'][1]
    D2 = cube['D'][2]
    D3 = cube['D'][3]
    D4 = cube['D'][4]
    D5 = cube['D'][5]
    D6 = cube['D'][6]
    D7 = cube['D'][7]
    D8 = cube['D'][8]

    R6 = cube['R'][6]
    R7 = cube['R'][7]
    R8 = cube['R'][8]

    F6 = cube['F'][6]
    F7 = cube['F'][7]
    F8 = cube['F'][8]

    L6 = cube['L'][6]
    L7 = cube['L'][7]
    L8 = cube['L'][8]
    
    B6 = cube['B'][6]
    B7 = cube['B'][7]
    B8 = cube['B'][8]

    cube['D'][0] = D6
    cube['D'][1] = D3
    cube['D'][2] = D0
    cube['D'][3] = D7
    cube['D'][4] = D4
    cube['D'][5] = D1
    cube['D'][6] = D8
    cube['D'][7] = D5
    cube['D'][8] = D2

    cube['R'][6] = F6
    cube['R'][7] = F7
    cube['R'][8] = F8

    cube['F'][6] = L6
    cube['F'][7] = L7
    cube['F'][8] = L8

    cube['L'][6] = B6
    cube['L'][7] = B7
    cube['L'][8] = B8

    cube['B'][6] = R6
    cube['B'][7] = R7
    cube['B'][8] = R8

def move_L():
    global cube
    L0 = cube['L'][0]
    L1 = cube['L'][1]
    L2 = cube['L'][2]
    L3 = cube['L'][3]
    L4 = cube['L'][4]
    L5 = cube['L'][5]
    L6 = cube['L'][6]
    L7 = cube['L'][7]
    L8 = cube['L'][8]

    U0 = cube['U'][0]
    U3 = cube['U'][3]
    U6 = cube['U'][6]

    F0 = cube['F'][0]
    F3 = cube['F'][3]
    F6 = cube['F'][6]

    D0 = cube['D'][0]
    D3 = cube['D'][3]
    D6 = cube['D'][6]
    
    B2 = cube['B'][2]
    B5 = cube['B'][5]
    B8 = cube['B'][8]

    cube['L'][0] = L6
    cube['L'][1] = L3
    cube['L'][2] = L0
    cube['L'][3] = L7
    cube['L'][4] = L4
    cube['L'][5] = L1
    cube['L'][6] = L8
    cube['L'][7] = L5
    cube['L'][8] = L2

    cube['U'][0] = B8
    cube['U'][3] = B5
    cube['U'][6] = B2

    cube['F'][0] = U0
    cube['F'][3] = U3
    cube['F'][6] = U6

    cube['D'][0] = F0
    cube['D'][3] = F3
    cube['D'][6] = F6
   
    cube['B'][2] = D6
    cube['B'][5] = D3
    cube['B'][8] = D0

def move_B():
    global cube
    B0 = cube['B'][0]
    B1 = cube['B'][1]
    B2 = cube['B'][2]
    B3 = cube['B'][3]
    B4 = cube['B'][4]
    B5 = cube['B'][5]
    B6 = cube['B'][6]
    B7 = cube['B'][7]
    B8 = cube['B'][8]

    U0 = cube['U'][0]
    U1 = cube['U'][1]
    U2 = cube['U'][2]

    R2 = cube['R'][2]
    R5 = cube['R'][5]
    R8 = cube['R'][8]

    D6 = cube['D'][6]
    D7 = cube['D'][7]
    D8 = cube['D'][8]

    L0 = cube['L'][0]
    L3 = cube['L'][3]
    L6 = cube['L'][6]

    cube['B'][0] = B6
    cube['B'][1] = B3
    cube['B'][2] = B0
    cube['B'][3] = B7
    cube['B'][4] = B4
    cube['B'][5] = B1
    cube['B'][6] = B8
    cube['B'][7] = B5
    cube['B'][8] = B2

    cube['U'][0] = R2
    cube['U'][1] = R5
    cube['U'][2] = R8

    cube['R'][2] = D8
    cube['R'][5] = D7
    cube['R'][8] = D6

    cube['D'][6] = L0
    cube['D'][7] = L3
    cube['D'][8] = L6

    cube['L'][0] = U2
    cube['L'][3] = U1
    cube['L'][6] = U0

def reset_cube():
    global cube
    cube = {
    'U': ['U0', 'U1', 'U2', 'U3', 'U4', 'U5', 'U6', 'U7', 'U8'], 
    'R': ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8'], 
    'F': ['F0', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8'], 
    'D': ['D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8'], 
    'L': ['L0', 'L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8'], 
    'B': ['B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8']
    }

def show_cube():
    global cube
    for key in cube:
        print(key)
        i = 0
        for elem in cube[key]:
            if i == 3 or i == 6:
                print()
                print(elem, end = ' ')
            else:
                print(elem, end = ' ')
            i += 1
        print()

def algorithm(scramble):
    global cube
    for ch in scramble:
        if ch == 'U':
            move_U()
        elif ch == 'R':
            move_R()
        elif ch == 'F':
            move_F()
        elif ch == 'D':
            move_D()
        elif ch == 'L':
            move_L()
        elif ch == 'B':
            move_B()
        else:
            print("Error")

def pow(move):
    if len(move) == 1:
        return 1
    elif move[1] == '2':
        return 2
    elif move[1] == "'":
        return 3
    return -1

def parse_standard_notation(scramble):
    arr = []
    moveset = scramble.split(' ')
    for move in moveset:
        arr.append(move[0]*pow(move))
    return "".join(arr)

def random_move_scramble(n):
    scramble = ""
    pows = ["", "2", "'"]
    moves = ['U', 'R', 'F', 'D', 'L', 'B']
    k = random.randint(0, 5)
    prev_k = k
    for i in range(n):
        while k == prev_k:
            k = random.randint(0, 5)
        prev_k = k
        j = random.randint(0, 2)
        scramble += moves[k] + pows[j] + " "
    return scramble.rstrip()

def get_colors(face):
    global U_clr, R_clr, F_clr, D_clr, L_clr, B_clr
    arr = []
    for sticker in face:
        if sticker[0] == 'U':
            arr.append(U_clr)
        elif sticker[0] == 'R':
            arr.append(R_clr)
        elif sticker[0] == 'F':
            arr.append(F_clr)
        elif sticker[0] == 'D':
            arr.append(D_clr)
        elif sticker[0] == 'L':
            arr.append(L_clr)
        elif sticker[0] == 'B':
            arr.append(B_clr)
    return arr