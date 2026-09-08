import random
import consts

#flag
flag_row = consts.BOARD_ROWS - consts.FLAG_ROWS
flag_col = consts.BOARD_COLS - consts.FLAG_COLS

def creat_field(rows,cols):#creating the field
    board=[]
    for i in range(consts.BOARD_ROWS):
        row=[]
        for j in range(consts.BOARD_COLS):
            row.append("")
        board.append(row)

    # for i in range(consts.BOARD_ROWS):#printing field without mines
    #
    #     print(board[i])
    #     print(end="\n")
    return board

def mine_in_random_places(mines_number,field,rows,cols):#puting mines in random places
    for mine in range(mines_number):
        row=random.randint(0,rows-1)
        col = random.randint(0, cols - 1)
        #while (row!=flag_row or row!=flag_row+1 or row!=flag_row+2 or row!=flag_row+3) and (col!= flag_col or col!=flag_col+1  or col!=flag_col+2  or col!=flag_col+3 ):
        while col+3<cols-1 :
            for i in range(3):

                field[row][col]="m"
                col+=1
    # for i in range(consts.BOARD_ROWS):#printing file with mines
    #     print(field[i])
    #     print(end="\n")

    return field




def creat_flag(field ,flag_size_row,flag_size_col,flag_row,flag_col):#flag place
    row=flag_row
    col=flag_col
    for i in range(flag_size_row):
        for j in range(flag_size_col):
            field[row][col]="f"
            col+=1
        col=flag_col
        row+=1
    for i in range(consts.BOARD_ROWS):
        print(field[i])
        print(end="\n")
    return field


#def get_soldier_place()








