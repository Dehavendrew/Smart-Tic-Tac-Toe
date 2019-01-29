import random
import tictacwin
#import boardx

from tictacwin import winorlose
#from boardx import drawboard


a = ['X',' ',' ',' ','O',' ',' ',' ',' ']

#drawboard(a)




def simplayermove(x):
        while True:
            pmove = random.randint(0,8)
            if x[pmove] == ' ':
                if pmove == 0:
                    x[0] = 'X'
                    return x
                if pmove == 1:
                    x[1] = 'X'
                    return x
                if pmove == 2:
                    x[2] = 'X'
                    return x
                if pmove == 3:
                    x[3] = 'X'
                    return x
                if pmove == 4:
                    x[4] = 'X'
                    return x
                if pmove == 5:
                    x[5] = 'X'
                    return x
                if pmove == 6:
                    x[6] = 'X'
                    return x
                if pmove == 7:
                    x[7] = 'X'
                    return x
                if pmove == 8:
                    x[8] = 'X'
                    return x
                break

def simcompmove(y):
        while True:
            cmove = random.randint(0,8)
            if y[cmove] == ' ':
                if cmove == 0:
                    y[0] = 'O'
                    return y
                if cmove == 1:
                    y[1] = 'O'
                    return y
                if cmove == 2:
                    y[2] = 'O'
                    return y
                if cmove == 3:
                    y[3] = 'O'
                    return y
                if cmove == 4:
                    y[4] = 'O'
                    return y
                if cmove == 5:
                    y[5] = 'O'
                    return y
                if cmove == 6:
                    y[6] = 'O'
                    return y
                if cmove == 7:
                    y[7] = 'O'
                    return y
                if cmove == 8:
                    y[8] = 'O'
                    return y
                else:
                    return y
                break
            

def simgame(b):
    win = 0
    num = [0,1,2,3,4,5,6,7,8]
    nextmove = 0 
    
    x1 = tuple(b)
    
    simcompmove(b)
    #print(b)

    for spot in num:
            if b[spot] != x1[spot]:
                    move = spot
    if winorlose(b) == 2:
            win += 2
            nextmove += 1
            
        
    while nextmove == 0:
        
        if ' ' not in b:
            #print('Draw')
            break
        
        simplayermove(b)
        if winorlose(b) == 1:
            win += 1
            break
        #print(b)

        if ' ' not in b:
            #print('Draw')
            break

        simcompmove(b)
        if winorlose(b) == 2:
            win += 2
            break
        #print(b)

        if ' ' not in b:
            #print('Draw')
            break

    
    for spot in num:
        if b[spot] != x1[spot]:
                b[spot] = x1[spot]
    
    return b, win , move


#print(simgame(a))


def choice(x,z):
        count = 0
        playerwin = 0
        compwin = 0
        draw = 0

        spot = [0,0,0,0,0,0,0,0,0]
        total = [0,0,0,0,0,0,0,0,0]



        
        while count < z:
            y = simgame(x)
            total[y[2]] += 1
            
            if y[0:2] == (x,2):
                compwin += 1
                spot[y[2]] += 1
            if y[0:2] == (x,1):
                playerwin += 1
            if y[0:2] == (x,0):
                draw += 1
            count += 1
        

        num = [0,1,2,3,4,5,6,7,8]

        avg = [0,0,0,0,0,0,0,0,0]


        for numb in num:
                if total[numb] == 0:
                        continue
                else:
                        avg[numb] = (100*spot[numb]) / (total[numb])

        print(avg)

        
        
        if 100 not in avg:

                if x[0] == x[4] == 'X' and x[8] == ' ':
                        return 8
                if x[1] == x[4] == 'X' and x[7] == ' ':
                        return 7
                if x[2] == x[4] == 'X' and x[6] == ' ':
                        return 6
                if x[3] == x[4] == 'X' and x[5] == ' ':
                        return 5
                if x[5] == x[4] == 'X' and x[3] == ' ':
                        return 3
                if x[6] == x[4] == 'X' and x[2] == ' ':
                        return 2
                if x[7] == x[4] == 'X' and x[1] == ' ':
                        return 1
                if x[8] == x[4] == 'X' and x[0] == ' ':
                        return 0

                if x[0] == x[1] == 'X' and x[2] == ' ':
                        return 2
                if x[1] == x[2] == 'X' and x[0] == ' ':
                        return 0
                if x[2] == x[5] == 'X' and x[8] == ' ':
                        return 8
                if x[5] == x[8] == 'X' and x[2] == ' ':
                        return 2
                if x[8] == x[7] == 'X' and x[6] == ' ':
                        return 6
                if x[6] == x[7] == 'X' and x[8] == ' ':
                        return 8
                if x[6] == x[3] == 'X' and x[0] == ' ':
                        return 0
                if x[3] == x[0] == 'X' and x[6] == ' ':
                        return 6

                if x[0] == x[6] == 'X' and x[3] == ' ':
                        return 3
                if x[0] == x[2] == 'X' and x[1] == ' ':
                        return 1
                if x[0] == x[8] == 'X' and x[4] == ' ':
                        return 4
                if x[2] == x[6] == 'X' and x[4] == ' ':
                        return 4
                if x[2] == x[8] == 'X' and x[5] == ' ':
                        return 5
                if x[6] == x[8] == 'X' and x[7] == ' ':
                        return 7

                
        if max(avg) == 0:
                return x.index(' ')
       

        
        return(avg.index(max(avg)))
            

#print(choice(a,500))




