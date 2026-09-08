# This is a sample Python script.
from socket import create_server

import consts
import game_field

if __name__ == '__main__':
    board=game_field.creat_field(consts.BOARD_ROWS,consts.BOARD_COLS)  #check if creat game field
    game_field.mine_in_random_places(consts.MINES_COUNT,board,consts.BOARD_ROWS,consts.BOARD_COLS)
    game_field.creat_flag(board,consts.FLAG_ROWS,consts.FLAG_COLS,game_field.flag_row,game_field.flag_col)

