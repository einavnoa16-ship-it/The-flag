import main


def if_loos(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            if main.soldier_pos==field[i][j]:
                if field[i][j]=="m":
                    return False

    return True

def if_touch_flag(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            if main.soldier_pos==field[i][j]:
                if field[i][j]=="f":
                    return True
    return False


