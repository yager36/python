
def Check_slot(board,x):
    x=int(x)
    if board[x-1]=="x" or board[x-1]=="o":
        return 1
    else:
        return 0    


def fun_chack(a):
    if len(a)>1 or len(a)<1:
        return 1  
         
    if  ord(a) > 48 and  ord(a) <58:
        return 0
    else:
        return 1    


def print_board(board):   
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
          

def rule(board):

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

                #print(x,y,r)
                if (x==0 and y==4 and r==8)  or (x==2 and y==4 and r==6):

                    if  board[x]=="x" and board[y]=="x" and board[r]=="x":
                        return 1
                    elif board[x]=="o" and board[y]=="o" and board[r]=="o":
                        return 2    





def start_to_play(x,board,fp):
    x=int(x)

    if  'first player'== fp:
        board[x-1]="x"
    elif 'second player'==sp:
        board[x-1]="o"
           
def chack_game(a):
    if  rule(board)==1:
        print('first player won')  
        a=input("for mor game press y else press n  ")

    elif rule(board)==2:
        print('second player won')  
        a=input("for mor game press y else press n  ")  


  
    return a                 

print("Welcome to x and o game")
fp='first player'
sp='second player'

board=[1,2,3,4,5,6,7,8,9]
print_board(board)
a='y'
while a=='y':
    x=input('choose please location you want to mark first player:\n')
     
    while  fun_chack(x):
        x=input('wrong input choose please location you want to mark first player:\n')

    while Check_slot(board,x):
        x=input('Occupancy slot try again\n')

    start_to_play(x,board,fp)
    print_board(board)
    chack_game(a)   
  
    o=input('choose please location you want to mark second player:\n')
    while  fun_chack(o):
        o=input('wrong input choose please location you want to mark first player:\n')
    while Check_slot(board,o):
        o=input('Occupancy slot try again\n')    
        
    start_to_play(o,board,sp)
    print_board(board)
    a=chack_game(a)

    
else:
    print ("winer")
   
    


  

       


   
    



           
              

            
   
       
      
    






