import time
import random
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
breedable = []
bred = []
pause(1)
line('Loaded')

while True:
    #Deaths
    death_check = -1
    while len(population) != death_check:
        death_check += 1
        if population[death_check][7] == population[death_check][4]:
            del population[death_check]
    
    #generation of offspring
    maturation_check = -1
    while len(population) != maturation check:
        maturation_check += 1
        if population[maturation_check][7] == population[maturation_check][6]:
            breedable.append(population[maturation_check])
        
    if len(breedable) % 2 == 1:
        del population[0]
    
    #aging of population
    
    #offspring added to population
