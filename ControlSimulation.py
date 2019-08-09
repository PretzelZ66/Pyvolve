import time
print('Loading')


def pause(number):
    time.sleep(number)


def line(string):
    print(string)
    pause(1)


gene_pool = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['C1', 'C2', 'C3'], ['D1', 'D2', 'D3'], ['E1', 'E2', 'E3']]
population1 = [['']]
population2 = [['']]
pause(1)
line('Loaded')
