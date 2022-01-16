"""Ticatactoe game for CSE210 Week 2 assignment
Author: Matías Adrian Barriga"""




def main():
    playturn = next_turn("")
    grid = draw_grid()
    while not (win(grid) or no_win(grid)):
        show_board(grid)
        your_turn(playturn, grid)
        playturn = next_turn(playturn)
    show_board(grid)
    print("Good game. Thanks for playing!")

def draw_grid():
    #This function creates a 
    grid = []
    for place in range(9):
        grid.append(place + 1)
    return grid


def show_board(grid):
    
    print()
    print('~-~-~')
    print(f"{grid[0]}|{grid[1]}|{grid[2]}")
    print('~-~-~')
    print(f"{grid[3]}|{grid[4]}|{grid[5]}")
    print('~-~-~')
    print(f"{grid[6]}|{grid[7]}|{grid[8]}")
    print('~-~-~')
    print()

def win(grid):
    
    return (grid[0] == grid[1] == grid[2] or
            grid[3] == grid[4] == grid[5] or
            grid[6] == grid[7] == grid[8] or
            grid[0] == grid[3] == grid[6] or
            grid[1] == grid[4] == grid[7] or
            grid[2] == grid[5] == grid[8] or
            grid[0] == grid[4] == grid[8] or
            grid[2] == grid[4] == grid[6])

def no_win(grid):
    
    for place in range(9):
        if grid[place] != 'o' or grid[place] != 'x':
            return False
    return True    

def your_turn(user, board):
    place = int(input(f"{user}'s turn to choose a square (1-9): "))
    board[place - 1] = user

def next_turn(actual):
    if actual == "" or actual == "o":
        return "x"
    elif actual == "x":
        return "o"


if __name__ == "__main__":
    main()