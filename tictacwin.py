a = [1,2,3,4,5,6,7,8,9]

def winorlose(x):
    if x[0] == x[1] == x[2]:
        if x[0] == 'X':
            #print('Player wins!')
            return 1
        if x[0] == 'O':
            #print('Computer wins')
            return 2
    if x[0] == x[4] == x[8]:
        if x[0] == 'X':
            #print('Player wins!')
            return 1
        if x[0] == 'O':
            #print('Computer wins')
            return 2
    if x[0] == x[3] == x[6]:
        if x[0] == 'X':
            #print('Player wins!')
            return 1
        if x[0] == 'O':
            #print('Computer wins')
            return 2
    if x[1] == x[4] == x[7]:
        if x[1] == 'X':
            #print('Player wins!')
            return 1
        if x[1] == 'O':
            #print('Computer wins')
            return 2
    if x[2] == x[4] == x[6]:
        if x[2] == 'X':
            #print('Player wins!')
            return 1
        if x[2] == 'O':
            #print('Computer wins')
            return 2
    if x[2] == x[5] == x[8]:
        if x[2] == 'X':
            #print('Player wins!')
            return 1
        if x[2] == 'O':
            #print('Computer wins')
            return 2
    if x[3] == x[4] == x[5]:
        if x[3] == 'X':
            #print('Player wins!')
            return 1
        if x[3] == 'O':
            #print('Computer wins')
            return 2
    if x[6] == x[7] == x[8]:
        if x[6] == 'X':
            #print('Player wins!')
            return 1
        if x[6] == 'O':
            #print('Computer wins')
            return 2



    
        

