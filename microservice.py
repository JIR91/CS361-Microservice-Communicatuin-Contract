from random import shuffle
from time import sleep


def microsrv_combo():
    clean = False

    while clean is False:
        with open('micro_pipe.txt', 'r') as r_file:
            lst = [line.rstrip() for line in r_file]
            if lst != []:
                shuffle(lst)
                with open('micro_pipe.txt', 'w') as w_file:
                    w_file.writelines(f'{i}\n' for i in lst)
                    clean = True
                if clean is True:
                    sleep(0.5)
                    with open('micro_pipe.txt', 'w') as clean_up:
                        clean_up.truncate(0)
                clean = False


if __name__ == '__main__':
    microsrv_combo()
