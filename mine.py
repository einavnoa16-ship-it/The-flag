import consts
import game_field
import pictures
import pygame
import os
from PIL import Image
import random

image = Image.open('pictures/mine.png')


# image.show()
list_mine=[]

def mine_in_random_places(mines_number, field, rows,
                          cols):  # puting mines in random places
    for mine in range(mines_number):
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        # while (row!=flag_row or row!=flag_row+1 or row!=flag_row+2 or row!=flag_row+3) and (col!= flag_col or col!=flag_col+1  or col!=flag_col+2  or col!=flag_col+3 ):
        while col + 3 < cols - 1:
            for i in range(3):
                field[row][col] = "m"
                col += 1

    for i in range(len(field)):
         for j in range(len(field[i])):
            if field[i][j] == "m":
                list_mine.append(list([i,j]))


    # for i in range(len(list_mine)):
    #     print(list_mine[i])
    # print(end="\n")
    #printing file with mines


    return list_mine

# board=game_field.
# def list_of_mines_places(field):
#     l_mines_places=[]
#     mone=0
#
#     while mone< 20:
#         for r in range(len(field)):
#             for c in range(len(field[r])):
#                 if field[r][c]=="m":
#                     l_mines_places.append(list([r,c]))
#                     mone+=1
#
#         # for  i in range(consts.BOARD_ROWS):
#         #     print(field[i],end="\n")
#     return l_mines_places
