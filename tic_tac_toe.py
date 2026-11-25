
import random

board = [" " for _ in range(9)]

def print_board():
    print(f"\n {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}\n")

def check_win(board, player):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in wins:
        if board[a]==board[b]==board[c]==player:
            return True
    return False

def comp_move_smart(board):
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_win(board, "O"):
                return i
            board[i] = " "
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_win(board, "X"):
                board[i] = " "
                return i
            board[i] = " "
    empty = [i for i, x in enumerate(board) if x == " "]
    return random.choice(empty)

print("Tic Tac Toe - You (X) vs Computer (O)")

while True:
    print_board()
    try:
        move = int(input("Your turn 1-9: ")) - 1
        if board[move] != " ":
            print("Taken! Try again")
            continue
    except:
        print("Enter 1-9 only!")
        continue
    board[move] = "X"
    if check_win(board, "X"):
        print_board()
        print("YOU WIN!")
        break
    if " " not in board:
        print_board()
        print("Draw!")
        break
    comp_move = comp_move_smart(board)
    board[comp_move] = "O"
    print(f"Computer played at {comp_move+1}")
    if check_win(board, "O"):
        print_board()
        print("Computer Wins! Try again!")
        break
    if " " not in board:
        print_board()
        print("Draw!")
        break    
  
