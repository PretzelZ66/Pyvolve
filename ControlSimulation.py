import time
from random import *
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
population = [[M, R, T, D, A, S, B, age], [M, R, T, D, A, S, B, age], [M, R, T, D, A, S, B, age], 
              [M, R, T, D, A, S, B, age], [M, R, T, D, A, S, B, age], [M, R, T, D, A, S, B, age],
              [M, R, T, D, A, S, B, age], [M, R, T, D, A, S, B, age], [M, R, T, D, A, S, B, age],
              [M, R, T, D, A, S, B, age]]
offspring = []
breedable = []
shuffled_breed = []

#facts
number_of_genarations = 0
deaths = 0
births = 0

pause(1)
line('Loaded')

while number_of_genarations != 100:
    #Deaths
    death_check = 0
    while len(population) != death_check:
        if population[death_check][7] == population[death_check][4]:
            del population[death_check]
            deaths += 1
        death_check += 1
    
    #generation of offspring
    maturation_check = 0
    while len(population) != maturation_check:
        if population[maturation_check][7] >= population[maturation_check][6]:
            breedable.append(population[maturation_check])
        maturation_check += 1
    
    while len(breedable) != 0:
        delt = randint(0, (len(breedable) - 1))
        shuffled_breed.append(breedable[delt])
        del breedable[delt]
    breedable = shuffled_breed
    
    if len(breedable) % 2 == 1:
        del breedable[0]
    
    while len(breedable) != 0:
        litter_cap = randint(breedable[0][1], breedable[1][1])
        litter = 0
        while litter != litter_cap:
            baby = []
            inherit_change = 0
            for i in range(7):
                inherit = randint(0, 1)
                baby.append(breedable[inherit][inherit_change])
                inherit_change += 1
            mutationyesno = randint(1, 1000)
            if mutationyesno <= baby[5]:
                stat = randint(0, 6)
                change = randint(0,1)
                if change == 0:
                    baby[stat] += 1
                elif change == 1:
                    baby[stat] -= 1
                if baby[4] == 0:
                    baby[4] = 1
            baby.append(age)
            offspring.append(baby)
            baby = []
            litter += 1
            births += 1
        del breedable[0]
        del breedable[0]
        
    #aging of population
    age_check = 0
    while len(population) != age_check:
        population[age_check][7] =+ 1
        age_check += 1
    
    #offspring added to population
    population.extend(offspring)
    
    #resets
    offspring = []
    breedable = []
    shuffled_breed = []
    number_of_genarations += 1
    print(number_of_genarations)
    print(f"Number of people: {len(population)}")
    print(f"Deaths: {deaths}")
    print(f"Births: {births}")

print(f"Number of people: {len(population)}")
print(f"Deaths: {deaths}")
print(f"Births: {births}")
print(f"People: {population}")
