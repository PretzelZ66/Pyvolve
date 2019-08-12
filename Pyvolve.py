import time
import random
print('Loading')


def pause(number):
    time.sleep(number)


def line(string):
    print(string)
    pause(1)

def Avr_Gen(The_list, gene_type):
    Gene_check = 0
    Average = 0
    while len(The_list) != Gene_check:
        addition = The_list[Gene_check][gene_type]
        Average += addition
        Gene_check += 1
    Average = Average // len(The_list)
    return(Average)

M = 1
R = 2
T = 10
D = 3
A = 3
S = 27
B = 1
age = 0
population = [[M, R, T, D, A, S, B, age], [M, R, T, D, A, S, B, age], [M, R, T, D, A, S, B, age], 
              [M, R, T, D, A, S, B, age], [M, R, T, D, A, S, B, age], [M, R, T, D, A, S, B, age],
              [M, R, T, D, A, S, B, age], [M, R, T, D, A, S, B, age], [M, R, T, D, A, S, B, age],
              [M, R, T, D, A, S, B, age]]
offspring = []
breedable = []

#facts
generation = 0
deaths = 0
births = 0
total_deaths = 0
total_births = 0
Avr_M = 0
Avr_R = 0
Avr_T = 0
Avr_D = 0
Avr_A = 0
Avr_S = 0
Avr_B = 0

pause(1)
line('Loaded')
line('~~CUSTOMISABLE SIMULATION PARAMETERS~~')
line('Would you like the genomes of the population to be displayed every 10 generations?')
user_response = input('YES/NO >>> ')
if user_response.lower() == 'yes':
    display_pop_genome = True
else:
    display_pop_genome = False
line('~~SIMULATION PARAMETERS HAVE BEEN SET~~')

while True:
    random.shuffle(population)
    #Deaths
    death_check = 0
    while len(population) != death_check:
        death_number = random.randint(1, 100)
        if population[death_check][7] == population[death_check][4]:
            del population[death_check]
            death_check -= 1
            deaths += 1
        elif death_number <= population[death_check][3]:
            del population[death_check]
            deaths += 1
            death_check -= 1
        death_check += 1
    
    #get Average
    Avr_M = Avr_Gen(population, 0)
    Avr_R = Avr_Gen(population, 1)
    Avr_T = Avr_Gen(population, 2)
    Avr_D = Avr_Gen(population, 3)
    Avr_A = Avr_Gen(population, 4)
    Avr_S = Avr_Gen(population, 5)
    Avr_B = Avr_Gen(population, 6)
    
    #generation of offspring
    breedable.extend(list(filter(lambda item: item[7] >= item[6], population)))

    random.shuffle(breedable)
    
    if len(breedable) % 2 == 1:
        del breedable[0]

    done_percentage = len(breedable)
    p_1 = 0
    p_2 = 0
    p_3 = 0
    
    while len(breedable) != 0:
        if breedable[1][1] > breedable[0][1]:
            litter_cap = random.randint(breedable[0][1], breedable[1][1])
        elif breedable[0][1] > breedable[1][1]:
            litter_cap = random.randint(breedable[1][1], breedable[0][1])
        elif breedable[0][1] == breedable[1][1]:
            litter_cap = random.randint(breedable[0][1], breedable[1][1]+1)
        litter = 0
        while litter != litter_cap:
            baby = []
            baby = [breedable[random.randint(0, 1)][i] for i in range(7)]
            mutationyesno = random.randint(1, 1000)
            if mutationyesno <= baby[5]:
                stat = random.randint(0, 6)
                change = random.randint(0,1)
                if change == 0:
                    baby[stat] += 1
                elif change == 1:
                    baby[stat] -= 1
                if baby[4] == 0:
                    baby[4] = 1
            baby.append(age)
            infant_death_yesno = random.randint(1, 100)
            if infant_death_yesno > baby[3]:
                offspring.append(baby)
            else:
                deaths += 1
            baby = []
            litter += 1
            births += 1
        del breedable[0]
        del breedable[0]

        if len(breedable) >= (done_percentage * 0.75):
            if p_3 == 0:
                print("   25%")
                p_3 = 1
        elif len(breedable) >= (done_percentage * 0.50):
            if p_2 == 0:
                print("   50%")
                p_2 = 1
        elif len(breedable) >= (done_percentage * 0.25):
            if p_1 == 0:
                print("   75%")
                p_1 = 1
        
    #aging of population
    age_check = 0
    while len(population) != age_check:
        population[age_check][7] += 1
        age_check += 1
    
    #offspring added to population
    population.extend(offspring)

    #Gene average

    #resets
    offspring = []
    breedable = []
    generation += 1
    pause(1)
    print('   ')
    print(f'Generation: {generation}')
    print(f"Population: {len(population)}")
    print(f"Deaths: {deaths}")
    print(f"Births: {births}")
    print(f"Net Growth: {(births - deaths)/len(population)}%")
    print('   ')
    if display_pop_genome == True:
        if generation %10 == 0:
            line(population)
    total_deaths += deaths
    total_births += births
    births = 0
    deaths = 0

print(f"Final Population: {len(population)}")
print(f"Total Deaths: {total_deaths}")
print(f"Total Births: {total_births}")
print(f"Creatures: {population}")
