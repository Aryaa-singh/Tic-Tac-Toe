def sum(a, b, c ):
    return a + b + c

def printBoard(Player1, Player2):
    zero = 'X' if Player1[0] else ('O' if Player2[0] else 0)
    one = 'X' if Player1[1] else ('O' if Player2[1] else 1)
    two = 'X' if Player1[2] else ('O' if Player2[2] else 2)
    three = 'X' if Player1[3] else ('O' if Player2[3] else 3)
    four = 'X' if Player1[4] else ('O' if Player2[4] else 4)
    five = 'X' if Player1[5] else ('O' if Player2[5] else 5)
    six = 'X' if Player1[6] else ('O' if Player2[6] else 6)
    seven = 'X' if Player1[7] else ('O' if Player2[7] else 7)
    eight = 'X' if Player1[8] else ('O' if Player2[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ") 

def checkWin(Player1, Player2):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(Player1[win[0]], Player1[win[1]], Player1[win[2]]) == 3):
            print("X Won the match")
            return 1
        if(sum(Player2[win[0]], Player2[win[1]], Player2[win[2]]) == 3):
            print("O Won the match")
            return 0
    return -1
    
if __name__ == "__main__":
    Player1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    Player2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for X and 0 for O
    print("Tic-Tac-Toe Begins")
    while(True):
        printBoard(Player1, Player2)
        if(turn == 1):
            print("X's Chance")
            position = int(input("Choose position : "))
            Player1[position] = 1
        else:
            print("O's Chance")
            position = int(input("Please enter a position: "))
            Player2[position] = 1
        cwin = checkWin(Player1, Player2)
        if(cwin != -1):
            print("Match over")
            break
        
        turn = 1 - turn