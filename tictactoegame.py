from boardx import drawboard, pieces
from tictacwin import winorlose
from cmovemod import choice

def game():
    sims = 0
    sim = input('Would you like an easy, medium, or hard game?')
    if sim == 'easy':
        sims = 10
    if sim == 'medium':
        sims = 100
    if sim == 'hard':
        sims = 5000

    drawboard(pieces)

    while True:
        def playermove(x):
            while True:
                pmove = int(input('it is your turn: '))
                if x[pmove - 1] == ' ':
                    if pmove == 1:
                        x[0] = 'X'
                        return x
                    if pmove == 2:
                        x[1] = 'X'
                        return x
                    if pmove == 3:
                        x[2] = 'X'
                        return x
                    if pmove == 4:
                        x[3] = 'X'
                        return x
                    if pmove == 5:
                        x[4] = 'X'
                        return x
                    if pmove == 6:
                        x[5] = 'X'
                        return x
                    if pmove == 7:
                        x[6] = 'X'
                        return x
                    if pmove == 8:
                        x[7] = 'X'
                        return x
                    if pmove == 9:
                        x[8] = 'X'
                        return x
                else:
                    print('That space has already been filled')
            
        P1 = playermove(pieces)
        drawboard(P1)
        
        

        if winorlose(pieces) == 1:
            print('Player wins')
            break

        if ' ' not in pieces:
            print("It's a draw")
            break



            
        def compmove(y):
            while True:
                cmove = choice(y,sims)

                if y[cmove] == ' ':

                    #print(cmove)
                    
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
                break
                
                
        C1 = compmove(pieces)
        print('Computer plays: ')
        drawboard(C1)

        

        if winorlose(pieces) == 2:
            print('Computer wins')
            break

    
while True:
    pieces = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    game()
    
    


    
   
    
    







