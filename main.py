import consts
import game_field
import grass
import soldier
import pygame
import pictures

# screen of the game


# ------------------------------
pygame.init()
size = (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("game")
# ------------------------------------

# background color of the screen


# --------------------
screen.fill(consts.BACK_GROUND_COLOR_GREEN)
pygame.display.flip()
# ---------------------------
soldier_player = pygame.image.load('pictures/soldier.png').convert()
screen.blit(soldier_player, [0, 0])
pygame.display.flip()
# -------------------------
# #soldier place
# my_matrix=[['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','','']]
# for i in range(my_matrix):
#     for j in range(my_matrix[i]):
#         if soldier.place[0]==i and soldier.place[1]==j:
#
#

# the infinite loop
# -----------------------
finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

pygame.quit()
# -------------------------
if __name__ == "__main__":
    board = game_field.creat_field(consts.BOARD_ROWS, consts.BOARD_COLS)
    game_field.mine_in_random_places(consts.MINES_COUNT, board,
                                     consts.BOARD_ROWS, consts.BOARD_COLS)
    game_field.creat_flag(board, consts.FLAG_ROWS, consts.FLAG_COLS,
                          game_field.flag_row, game_field.flag_col)
    grass.random_bosh(board, consts.BOARD_ROWS, consts.BOARD_COLS)


