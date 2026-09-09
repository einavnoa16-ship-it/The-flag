import pictures
import pygame
import os
from PIL import Image
import consts


image = Image.open('pictures/soldier.png')

#
# def soldier_movement(event,place):
#     key=pygame.key.get_pressed()
#     if event.type==pygame.KEYDOWN:
#         x=place[0]
#         y=place[1]
#         if event.key==pygame.K_LEFT:
#             x-=consts.CELL_SIZE
#         elif event.key==pygame.K_RIGHT:
#             x+=consts.CELL_SIZE
#         elif event.key == pygame.K_UP:
#             y += consts.CELL_SIZE
#         elif event.key == pygame.K_DOWN:
#             y -= consts.CELL_SIZE
#
#
def soldier_move(soldier_pos):
    run=False
    while not run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                x = soldier_pos[0]
                y = soldier_pos[1]
                if event.key == pygame.K_LEFT:
                    x -= 1
                    run=True
                elif event.key == pygame.K_RIGHT:
                    x += 1
                    run = True
                elif event.key == pygame.K_UP:
                    y -= 1
                    run = True
                elif event.key == pygame.K_DOWN:
                    y += 1
                    run = True
                soldier_pos = [x, y]

    return soldier_pos





#image.show()


