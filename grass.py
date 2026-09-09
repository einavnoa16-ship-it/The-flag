import random

import consts
import pictures
import pygame
import os
from PIL import Image


image = Image.open('pictures/grass.png')
#image.show()

def random_bosh(field,rows,cols):
    list_p=[]
    mone=0
    while mone<20:
        r=random.randint(0,rows-1)
        c=random.randint(0,cols-1)
        if field[r][c]!="m" or field[r][c]!="f":
          field[r][c]="i"
          list_p.append(list([r,c]))
          mone+=1
        else:
            continue

    for i in range(consts.BOARD_ROWS):
        print(field[i],end="\n")

    return list_p
