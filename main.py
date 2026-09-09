import consts
import game_field
import grass
import mine
import soldier
import pygame
import pictures
# import mines_screen
from PIL import Image
import time

# screen of the game
pygame.init()
size = (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("game")

# background color of the screen
screen.fill(consts.BACK_GROUND_COLOR_GREEN)
pygame.display.flip()
background_begin=pygame.image.load('pictures/flagStartimg.png')
screen.blit(background_begin,(90, 50))
pygame.display.flip()


#clock refresh the screen
clock=pygame.time.Clock()


#soldier place
background=(255,35,240)
#s_place=
soldier_size=(consts.CELL_SIZE*consts.SOLDIER_ROWS,consts.CELL_SIZE*consts.SOLDIER_COLS)
soldier_pos=[0,0]#soldier.soldier_movement(pygame.event,s_place)#game_field.get_soldier_place()
soldier_new_pos=soldier.soldier_move(soldier_pos)
soldier_img=Image.open('pictures/soldier.png')
soldier_img.thumbnail(soldier_size)
soldier_img.save('pictures/soldier.png')
soldier_player = pygame.image.load('pictures/soldier.png').convert()
soldier_player.set_colorkey(background)
soldier_place=[soldier_new_pos[0]*consts.CELL_SIZE,soldier_new_pos[1]*consts.CELL_SIZE]


#night soldier
night_soldier=pygame.image.load('pictures/soldier_night.png')
night_soldier_img=Image.open('pictures/soldier_night.png')
night_soldier_img.thumbnail(soldier_size)
night_soldier_img.save('pictures/soldier_night.png')
night_soldier_player = pygame.image.load('pictures/soldier_night.png').convert()
night_soldier_player.set_colorkey(background)


#flag place
flag_size=(consts.CELL_SIZE*consts.SOLDIER_ROWS,consts.CELL_SIZE*consts.SOLDIER_COLS)
flag=pygame.image.load('pictures/flag.png')
flag_place=[consts.WINDOW_WIDTH-40,consts.WINDOW_HEIGHT-40]
flag_img=Image.open('pictures/flag.png')
flag_img.thumbnail(flag_size)
flag_img.save('pictures/flag.png')
screen.blit(flag,flag_place)
pygame.display.flip()

# screen_night=pygame.Surface.copy(screen)
# pygame.display.flip()
#-------------for loop on bush places
board=game_field.creat_field(consts.BOARD_ROWS,consts.BOARD_COLS)


list_b_p=grass.random_bosh(board,consts.BOARD_ROWS,consts.BOARD_COLS)
grass_image=pygame.image.load('pictures/grass.png')
grass_size=(consts.CELL_SIZE*consts.SOLDIER_ROWS-1,consts.CELL_SIZE*consts.SOLDIER_COLS+1)
grass_place=[0,0]
grass_img=Image.open('pictures/grass.png')
grass_img.thumbnail(grass_size)
grass_img.save('pictures/grass.png')

#mine
list_m_p=mine.mine_in_random_places(20,board,consts.BOARD_ROWS, consts.SOLDIER_COLS)
mine_image=pygame.image.load('pictures/mine.png')
mine_size=(consts.CELL_SIZE*consts.SOLDIER_ROWS-1,(consts.CELL_SIZE*consts.SOLDIER_COLS*3)+1)
mine_place=[0,0]
mine_img=Image.open('pictures/mine.png')
mine_img.thumbnail(mine_size)
mine_img.save('pictures/mine.png')


background_night=pygame.image.load('pictures/bbbbbb.png')

# for r in range(len(list_b_p)):




# the infinite loop
finish = False
while not finish:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.KEYDOWN:
            x = soldier_pos[0]
            y = soldier_pos[1]
            if event.key == pygame.K_LEFT:
                if x==0:
                    x=0
                else:
                    x -= 1

            elif event.key == pygame.K_RIGHT:
                if x == 50:
                    x = 50
                else:
                    x += 1
            elif event.key == pygame.K_UP:
                if y==0:
                    y=0
                else:
                    y -= 1
            elif event.key == pygame.K_DOWN:
                if y==25:
                    y=25
                else:
                    y += 1
            # elif event.key==pygame.K_DELETE:
            #     for i in range(1):
            #
            #         screen.blit(background_night,(0,0))
            #         pygame.display.flip()
            #         time.sleep(3)

            soldier_pos = [x, y]
            ###3entering night screen when press delete
            if event.key == pygame.K_DELETE:
                for i in range(1):
                    screen.blit(background_night, (0, 0))
                    pygame.display.flip()
                    soldier_place = [soldier_pos[0] * consts.CELL_SIZE,
                                     soldier_pos[1] * consts.CELL_SIZE]
                    screen.blit(night_soldier, soldier_place)
                    # pygame.display.flip()
                    for r in range(len(list_m_p)):
                        mine_place = (
                            (list_m_p[r][0]) * consts.CELL_SIZE + 150,
                            (list_m_p[r][1]) * consts.CELL_SIZE * 0.500)
                        screen.blit(mine_image, mine_place)

                    pygame.display.flip()
                    time.sleep(2)


        #soldier movement
            soldier_place=[soldier_pos[0]*consts.CELL_SIZE,soldier_pos[1]*consts.CELL_SIZE]
            screen.fill(consts.BACK_GROUND_COLOR_GREEN)
            screen.blit(soldier_player, soldier_place)
            #flag placing
            screen.blit(flag,flag_place)
            #grass placing
            for r in range(len(list_b_p)):
                grass_place = ((list_b_p[r][0]) * consts.CELL_SIZE + 150,
                               (list_b_p[r][1]) * consts.CELL_SIZE * 0.500)
                screen.blit(grass_image, grass_place)


            pygame.display.flip()
            pygame.display.update()
            clock.tick(consts.REFRESH_RATE)





pygame.quit()


#+150#*0.500
