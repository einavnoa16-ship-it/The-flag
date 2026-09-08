import consts
import soldier
import pygame
import pictures
from PIL import Image

# screen of the game
pygame.init()
size = (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("game")

# background color of the screen
screen.fill(consts.BACK_GROUND_COLOR_GREEN)
pygame.display.flip()

#soldier place
background=(255,35,240)
soldier_size=(consts.CELL_SIZE*consts.SOLDIER_ROWS,consts.CELL_SIZE*consts.SOLDIER_COLS)
soldier_place=[100,200]#game_field.get_soldier_place()
soldier_img=Image.open('pictures/soldier.png')
soldier_img.thumbnail(soldier_size)
soldier_img.save('pictures/soldier.png')
soldier_player = pygame.image.load('pictures/soldier.png').convert()
soldier_player.set_colorkey(background)
screen.blit(soldier_player, soldier_place)
pygame.display.flip()


#flag place
flag=pygame.image.load('pictures/flag.png')
screen.blit(flag,[consts.WINDOW_WIDTH-100,consts.WINDOW_HEIGHT-100])
pygame.display.flip()


# #soldier place
# my_matrix=[['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','','']]
# for i in range(my_matrix):
#     for j in range(my_matrix[i]):
#         if soldier.place[0]==i and soldier.place[1]==j:
#
#

# the infinite loop
finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

pygame.quit()



