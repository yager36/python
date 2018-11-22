
import random

obj={                                # object of counting
  "cut":0,
  "cut1":0,
  "cut_equal":0
}                                    
def print_win():                     # function which declares the number of victories
    print("Number of victories first player:",obj["cut"])
    print("Number of victories second player:",obj["cut1"])
def Check_slot(board,x):            
    x=int(x)
    if board[x-1]=="x" or board[x-1]=="o":
        return 1
    else:
        return 0    
def fun_chack(a):                    # function checks if the conditions, only number and no mor than 1 digit
    if len(a)>1 or len(a)<1:
        return 1          
    if  ord(a) > 48 and  ord(a) <58:
        return 0
    else:
        return 1    
def print_board(board):              # function print the board game
    cut=1

    print('-----------------')
    for k in board:
        print ('|',end=" ")
        print (k,end=" ")
        print ('|',end=" ")
        cut=cut+1
        if cut>3:               
            print()
            print('-----------------')
            cut=1   
def rule(board):                    # function that checks the game moves "tic-tac-toe" and cheking the  winner

    for x in range(0,9):
        for y in range(0,9):
            for r in range(0,9):         
                if (x==0 and y==1 and r==2)  or (x==3 and y==4 and r==5) or (x==6 and y==7 and r==8):
                    if  board[x]=="x" and board[y]=="x" and board[r]=="x":
                        return 1
                    elif board[x]=="o" and board[y]=="o" and board[r]=="o":
                        return 2
                if (x==0 and y==3 and r==6)  or (x==1 and y==4 and r==7) or (x==2 and y==5 and r==8):              
                    
                    if  board[x]=="x" and board[y]=="x" and board[r]=="x":                   
                        return 1
                    elif board[x]=="o" and board[y]=="o" and board[r]=="o":
                        return 2     
               
                if (x==0 and y==4 and r==8)  or (x==2 and y==4 and r==6):

                    if  board[x]=="x" and board[y]=="x" and board[r]=="x":
                        return 1
                    elif board[x]=="o" and board[y]=="o" and board[r]=="o":
                        return 2
         
def equal(board):       # function that checks the result of equality
    for x in range(0,9):        
        if  board[x]=="x" or board[x]=="o":
            obj["cut_equal"]=obj["cut_equal"]+1

        if  obj["cut_equal"]==9:
            return 3

def start_to_play(x,board,fp):  # function enters str,"x", or "o" to the game board/summed up the number of victories/Activates the functions, equal
    x=int(x)                    # /lets_play_again/ print_board
    if  'first player'== fp:
        board[x-1]="x"
    elif 'second player'==sp:
        board[x-1]="o"         
def chack_game(board,p):
    obj["cut_equal"]=0
    if  rule(board)==1:
        print('first player won')  
        print_board(board)
        p=lets_play_again(p)
        obj["cut"]=obj["cut"]+1
    elif rule(board)==2:
        print('second player won')
        print_board(board)
        obj["cut1"]=obj["cut1"]+1
        p=lets_play_again(p)
    elif equal(board)==3: 
        print('A draw between two players')
        print_board(board)
        p=lets_play_again(p)
    else:
        obj["cut_equal"]=0      
    return p    
def lets_play_again(p): #At the end of the game the function asks the user to "play again or end a game
    i=1
    p=input("For play again press 'y' for exit press 'n':\n")
    while(p!='y' and p!='n'):
        p=input("worng input please try again For play again press 'y' for exit press 'n'")
    return p

    
print("Welcome to x and o game")
fp='first player'
sp='second player'
board=[1,2,3,4,5,6,7,8,9]
lulaa=100
p=" " 
cup=input("to play with agains compuer press 1\nto play 2 player press 2:  ")
print_board(board)

while lulaa: # start the game loop

    x=input('choose please location you want to mark first player:\n')   
    while  fun_chack(x):
        x=input('wrong input choose please location you want to mark first player:\n')
    while Check_slot(board,x):
        x=input('Occupancy slot try again\n')
    start_to_play(x,board,fp)
    p=chack_game(board,p) 
    print_board(board) 
    if p=='n':
        print_win()
        break
    elif p=='y':
        board=[1,2,3,4,5,6,7,8,9]
        print_board(board)
        p=" " 
        print_win()
        continue
    if cup=='1':
        o=str(random.randint(0, 8))
    elif cup=='2':
        o=input('choose please location you want to mark second player:\n')    
    while  fun_chack(o):
        if cup=='1':
            o=str(random.randint(0, 8))
        elif cup=='2':    
             o=input('wrong input choose please location you want to mark first player:\n')
    while Check_slot(board,o):
        if cup=='1':
            o=str(random.randint(0, 8))    
        elif cup=='2':      
            o=input('Occupancy slot try again\n')   
    start_to_play(o,board,sp) 
    print_board(board)
    p=chack_game(board,p)
    if p=='n':
        print_win()
        break
    elif p=='y':
        board=[1,2,3,6,5,9,7,8,9] #Reset the array
        print_board(board)
        p=" " 
        print_win()
        continue 


        


