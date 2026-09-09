import consts
import pygame
import soldier
from PIL import Image

# screen of the game
pygame.init()
size = (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("game")

# background color of the screen
background_night= pygame.image.load('pictures/bbbbbb.png')
screen.blit(background_night,(0,0))
# screen.fill(consts.BACK_GROUND_COLOR_GREEN)
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



run=False
while not run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =True
        elif event.type == pygame.KEYDOWN:
            x = soldier_pos[0]
            y = soldier_pos[1]
            if event.key == pygame.K_LEFT:
                if x == 0:
                    x = 0
                else:
                    x -= 1
            elif event.key == pygame.K_RIGHT:
                if x == 50:
                    x = 50
                else:
                    x += 1
            elif event.key == pygame.K_UP:
                if y == 0:
                    y = 0
                else:
                    y -= 1
            elif event.key == pygame.K_DOWN:
                if y == 25:
                    y = 25
                else:
                    y += 1
            # elif event.key==pygame.K_KP_ENTER:

            soldier_pos = [x, y]

    # soldier movement
    soldier_place = [soldier_pos[0] * consts.CELL_SIZE,
                     soldier_pos[1] * consts.CELL_SIZE]
    background_night = pygame.image.load('pictures/bbbbbb.png')
    screen.blit(background_night, (0, 0))
    # screen.fill(consts.BACK_GROUND_COLOR_GREEN)
    screen.blit(soldier_player, soldier_place)

    pygame.display.flip()
    pygame.display.update()
    clock.tick(consts.REFRESH_RATE)


