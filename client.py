from time import sleep

def get_rand_combo(lst):
    new_lst = ''
    kill_switch = True

    while kill_switch is True:
        with open('micro_pipe.txt', 'w') as rf:
            rf.writelines(f'{i}\n' for i in lst)
        sleep(0.5)
        with open('micro_pipe.txt', 'r') as f:
            new_lst = [line.rstrip() for line in f]
        if new_lst != lst: return new_lst

def main():
    lst = ['a','b','c','d','f']
    print(f'{lst}\n\n')
    a = get_rand_combo(lst)
    print(f'{a}')


if __name__ == '__main__':
    main()