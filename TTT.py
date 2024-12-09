import random

def cpu_chance(board, user):
    if isAvailable(board):
        choice_row_cpu = random.randint(0, 2)
        choice_col_cpu = random.randint(0, 2)

        while board[choice_row_cpu][choice_col_cpu]!="_":
            choice_row_cpu = random.randint(0, 2)
            choice_col_cpu = random.randint(0, 2)

        if user == "X":
            board[choice_row_cpu][choice_col_cpu] = "O"
        else:
            board[choice_row_cpu][choice_col_cpu] = "X"

        print_board(board)
    return 0

def print_board(board):
    for row in range(0, 3):
        for col in range(0, 3):
            print(board[row][col], end = " ")
        print(" ")

def row_win(board, user):
    for index in range(0, 3):
        if board[index][0]!="_":
            if board[index][0]==board[index][1] and board[index][1]==board[index][2]:
                if board[index][0]==user:
                    return 1
                else:
                    return 2
            
    return 0

def col_win(board, user):
    for col in range(0, 3):
        if board[0][col]!="_":
            if board[0][col]==board[1][col] and board[1][col]==board[2][col] and board[0][col]==user:
                return 1
            if board[0][col]==board[1][col] and board[1][col]==board[2][col] and board[0][col]!=user:
                return 2
            
    return 0

def diagonal_win(board, user):
    if board[1][1]!="_":
        if board[0][0]==board[1][1] and board[1][1]==board[2][2]:
            if board[0][0]==user:
                return 1
            else:
                return 2
  
        if board[0][2]==board[1][1] and board[1][1]==board[2][0]:
            if board[0][2]==user:
                return 1
            else:
                return 2
        
    return 0

def isAvailable(board):
    for row in range(0, 3):
        for col in range(0, 3):
            if board[row][col]=="_":
                return True
    return False

def isValid(board, response_row, response_col):
    if response_row < 3 and response_row >= 0 and response_col < 3 and response_col >= 0:
        if board[response_row][response_col] == "_":
            return True
    return False

board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

print("Welcome!")
user = input("What would you choose to play with? Press 'X' for \"X\" and 'O' for \"O\": ")
while user!="X" and user!="O":
    print("Please Enter a valid choice")
    user = input("Press 'X' for \"X\" and 'O' for \"O\": ")

print("\n\nTic Tac Toe Game Started! You start first")
print("\n")

print("Board - ")
print_board(board)

print("\nEnter the cell address. Upper left is (0,0). Right and down increase")

while not(row_win(board, user)) and not(col_win(board, user)) and not(diagonal_win(board, user)) and isAvailable(board):
    print("\n\nYour Chance - ")
    response_row = int(input("Enter your choice of row: "))
    response_col = int(input("Enter your choice of column: "))

    while not(isValid(board, response_row, response_col)):
        print("Invalid choice of row and/or col. Please try again")
        response_row = int(input("Enter your choice of row: "))
        response_col = int(input("Enter your choice of column: "))

    board[response_row][response_col] = user
    print("\nBoard - ")
    print_board(board)
    if isAvailable(board):
        print("\nBoard after CPU chance - ")
        cpu_chance(board, user)

if row_win(board)==1 or col_win(board)==1 or diagonal_win(board)==1:
    print("\n\nYou Win! :)")
elif row_win(board)==2 or col_win(board)==2 or diagonal_win(board)==2:
    print("\n\nYou Lose! CPU Wins :(")
else:
    print("\n\nDraw ._.")