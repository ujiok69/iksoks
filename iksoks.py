import pygame

def printBoard(a):
    print(a[0], a[1], a[2])
    print(a[3], a[4], a[5])
    print(a[6], a[7], a[8])

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
printBoard(board)
nerešeno = False
i = 0
while i < 9:
    if i % 2 == 0:
        x = int(input("x na potezu, unesi željeno polje:"))
        
    else:
        x = int(input("o na potezu, unesi željeno polje:"))
    
    if board[x-1] != "-":
        print("Polje je zauzeto")
        i = i - 1
        
    else:
        if i % 2 == 0:
            board[x-1] = "x"
            printBoard(board)
        
        else:
            board[x-1] = "o"
            printBoard(board)
            
    if board[0] == board[1] == board[2] == "x" or board[3] == board[4] == board[5] == "x" or board[6] == board[7] == board[8] == "x" or board[0] == board[3] == board[6] == "x" or board[1] == board[4] == board[7] == "x" or board[2] == board[5] == board[8] == "x" or board[0] == board[4] == board[8] == "x" or board[2] == board[4] == board[6] == "x" or board[0] == board[1] == board[2] == "o" or board[3] == board[4] == board[5] == "o" or board[6] == board[7] == board[8] == "o" or board[0] == board[3] == board[6] == "o" or board[1] == board[4] == board[7] == "o" or board[2] == board[5] == board[8] == "o" or board[0] == board[4] == board[8] == "o" or board[2] == board[4] == board[6] == "o":
        if i % 2 == 0:
            print("x je pobednik")

        else:
            print("o je pobednik")
            
        break
    elif i == 8:
        nerešeno = True

    i += 1

if nerešeno == True:
    print("nerešeno")
    
    

