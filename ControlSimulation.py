import time
print('Loading')


def pause(number):
    time.sleep(number)


def line(string):
    print(string)
    pause(1)


population = [['M', 'R', 'T', 'D', 'A', 'S'], ['M', 'R', 'T', 'D', 'A', 'S'], ['M', 'R', 'T', 'D', 'A', 'S'],
              ['M', 'R', 'T', 'D', 'A', 'S'], ['M', 'R', 'T', 'D', 'A', 'S'], ['M', 'R', 'T', 'D', 'A', 'S'],
              ['M', 'R', 'T', 'D', 'A', 'S'], ['M', 'R', 'T', 'D', 'A', 'S'], ['M', 'R', 'T', 'D', 'A', 'S'], 
              ['M', 'R', 'T', 'D', 'A', 'S']]
offspring = [['']]
pause(1)
line('Loaded')
