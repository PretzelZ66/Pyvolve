import time
print('Loading')


def pause(number):
    time.sleep(number)


def line(string):
    print(string)
    pause(1)

M = 1
R = 2
T = 10
D = 1
A = 3
S = 1
B = 1
age = 0
population = [[M, R, T, D, A ,S, B, age], [M, R, T, D, A ,S, B, age], [M, R, T, D, A ,S, B, age],
              [M, R, T, D, A ,S, B, age], [M, R, T, D, A ,S, B, age], [M, R, T, D, A ,S, B, age],
              [M, R, T, D, A ,S, B, age], [M, R, T, D, A ,S, B, age], [M, R, T, D, A ,S, B, age],
              [M, R, T, D, A ,S, B, age]]
offspring = []
pause(1)
line('Loaded')
