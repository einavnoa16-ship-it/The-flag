import consts
import soldier
import pygame
import pictures

#screen of the game
pygame.init()
size=(consts.WINDOW_WIDTH,consts.WINDOW_HEIGHT)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("game")

#background color of the screen
img=pygame.image.load()
screen.blit(img,(0,0))
pygame.display.flip()

# screen.fill(consts.BACK_GROUND_COLOR_GREEN)
# pygame.display.flip()

#the infinite loop
finish =False
while not finish:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            finish=True




pygame.quit()

