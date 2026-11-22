board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]
def show_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("---------")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("---------")
    print(board[6] + "|" + board[7] + "|" + board[8])

def check_win():
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4,7], [2, 5, 8], [0, 4, 8], [2, 4, 6]
    ]
    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] != " ":
            return board[w[0]]
    return None
          

print("Welcome to X and O")  
show_board()

player = "X"

for turn in range(9):
    print("\nPlayer" + player + ", your turn !")
    pos = int(input("Pick a spot 1-9: ")) - 1

    if board[pos] == " ":
        board[pos] = player
        show_board()

        winner = check_win()
        if winner:
            print("\n*** " + winner + " WINS! ***")
            break

        if player == "X":
            player = "O"
        else:
            player = "X"
    else:
        print("That spot is taken ! Try again!")
else:
    print("\nIt's a DRAW!")

print("\nGame Over!")

    
  
