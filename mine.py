import consts
import game_field
import pictures
import pygame
import os
from PIL import Image


image = Image.open('pictures/mine.png')
#image.show()

def list_of_mines_places(field):
    l_mines_places=[]
    mone=0
    mine_width=0
    while mone< 20:
        for r in range(len(field)):
            for c in range(len(field[r])):
                if field[r][c]=="m" and mine_width==0:
                    l_mines_places.append(list([r,c]))
                    mone+=1
                    mine_width+=1
                elif field[r][c]=="m" and mine_width!=0 and mine_width<3:
                    mine_width+=1
                elif field[r][c]!="m" and mine_width==3:
                    mine_width=0


        # for  i in range(consts.BOARD_ROWS):
        #     print(field[i],end="\n")
    return l_mines_places

