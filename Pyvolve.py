#pyvolve 1.2.0
import time, random
print('loading')


def pause(number):
    time.sleep(number)


def line(string):
    print(string)
    pause(1)

def avr_gen(the_list, gene_type):
    gene_check = 0
    average = 0
    if len(the_list) != 0:
        while len(the_list) != gene_check:
            addition = the_list[gene_check][gene_type]
            average += addition
            gene_check += 1
        average = average // len(the_list)
        return(average)
    return(0)

m = 1
r = 2
t = 10
d = 3
a = 3
s = 27
b = 1
age = 0
fed = 0
fatigue = 0
b_c = 0 #birth count
contaminated = False
population = []
offspring = []
breedable = []
average_genome = []
pop_template = [m, r, t, d, a, s, b, age, fed, fatigue, b_c, contaminated]

#facts
generation = 0
deaths = 0
births = 0
food = 0
fpg_cap = 10000
breedable_count = 0

temperature = 0
temp_rate = 0.1
temp_increase = 1
temp_state = True
temp_max = 5

events =  0
event_clock1 = 0
event_clock2 = 0
event_clock3 = 0

avr_m = 0
avr_r = 0
avr_t = 0
avr_d = 0
avr_a = 0
avr_s = 0
avr_b = 0

class virus:
    infected = 0
    food = 0
    kill_chance = 5
    mutaion_chance = 1
    infectiousness = 10
    metabolism = 3
met_clock = virus.metabolism

pause(1)
line('loaded')
print('')
line('~~customisable simulation parameters~~')

line('what would you like to call the results file?')
file_name = input('>>> ')
file_name_raw = file_name + '_raw.txt'
file_name += '.txt'
with open(file_name, 'x') as file:
    file.close()
    
with open(file_name_raw, 'x') as file:
    file.close()

line('''what preset would you like to use? default(0), nuclear playground(1),
thermonuclear playground(2), virus playground(3), event mayhem(4), custom(other)''')
preset_type = int(input('>>> '))

if preset_type == 0:
    #default
    start_pop = 50
    event_chance_cap = 100
    mutation_rate = 1
    default_mutation_rate = mutation_rate
    mutation_severity = 1
    infect_counter = 1
    
elif preset_type == 1:
    #nuclear playground
    start_pop = 50
    event_chance_cap = 69
    mutation_rate = 100
    default_mutation_rate = 100
    mutation_severity = 5
    infect_counter = 1

elif preset_type == 2:
    #thermonuclear playground
    start_pop = 50
    event_chance_cap = 49
    mutation_rate = 500
    default_mutation_rate = 500
    mutation_severity = 25
    infect_counter = 0

elif preset_type == 3:
    #virus playground
    start_pop = 50
    event_chance_cap = 100
    mutation_rate = 1
    default_mutation_rate = mutation_rate
    mutation_severity = 1
    infect_counter = 50

    virus.kill_chance = 50
    virus.mutaion_chance = 10
    virus.infectiousness = 100
    virus.metabolism = 20
    virus.food = 1000

elif preset_type == 4:
    #event mayhem
    start_pop = 50
    event_chance_cap = 0
    mutation_rate = 1
    default_mutation_rate = mutation_rate
    mutation_severity = 1
    infect_counter = 50
    
else:
    line('what would you like the starting population to be?')
    start_pop = int(input('>>> '))
    if start_pop <= 1:
        start_pop = 2

    line('would you like a low (3), medium (2), or high (1) event chance?')
    event_chance = int(input('1/2/3 >>> '))
    if event_chance > 0 and event_chance <= 3:
        event_chance_cap = event_chance
    else:
        event_chance_cap = 2
    event_chance_cap = event_chance_cap * 50
    
    line('what would you like the default radiation level to be?')
    mutation_rate = int(input('>>> '))
    default_mutation_rate = mutation_rate

    line('what would you like the mutation severity to be?')
    mutation_severity = int(input('>>> '))

    line('how many creatures would you like to start out with the virus?')
    infect_counter = int(input('>>> '))

pop_gen_check = 0
while pop_gen_check != start_pop:
    if infect_counter != virus.infected:
        contaminated = True
        virus.infected += 1
    else:
        contaminated = False
    
    pop_template = [m, r, t, d, a, s, b, age, fed, fatigue, b_c, contaminated]
    population.append(pop_template)
    pop_gen_check += 1

virus.food += virus.infected * 10

line('~~simulation parameters have been set~~')

while True:
    deaths = 0
    pause(1)
    random.shuffle(population)
    
    #food changing
    print('    changing food')
    food += random.randint(5000, fpg_cap)
    foodupdown = random.randint(-1, 1)
    if foodupdown == -1:
        fpg_cap -= 1000
        if fpg_cap < 5000:
            fpg_cap = 5000
    elif foodupdown == 1:
        fpg_cap += 1000

    #breedable assignment
    print('    sorting breedables from unbreedables')
    breedable_check = 0
    for i in range(len(population)):
        if len(population[breedable_check]) == 13:
            del population[breedable_check][12]
        
        if population[breedable_check][6] <= population[breedable_check][7] and population[breedable_check][9] == 0:
            breedable = True
            population[breedable_check].append(breedable)
            breedable_count += 1
        else:
            breedable = False
            population[breedable_check].append(breedable)
        breedable_check += 1
    
    #event clocks
    print('    event clocks')
    if event_clock1 > 0:
        event_clock1 -= 1
        if event_clock1 == 0:
            mutation_rate = default_mutation_rate
    if event_clock2 > 0:
        event_clock2 -= 1 
        temperature -= random.randint(1, 3)
    if event_clock3 > 0:
        event_clock3 -= 1
        print("aftershock")
        death_check = 0
        while len(population) != death_check:
            death_number = random.randint(1, 400)
            if death_number == 13:
                if population[death_check][12] is True and breedable_count > 2:
                    del population[death_check]
                    death_check -= 1
                    deaths += 1
                    breedable_count -= 1
            death_check += 1
        
    #random events
    print('    random event check')
    event_done = ''
    event_check = random.randint(0, event_chance_cap)
    if event_check == 0:
        event = random.randint(events, 7)
        if event == 0:
            event_done = 'environment stability lowered'
            event_chance_cap -= 1
            if event_chance_cap > 0:
                event_chance_cap -= random.randint(1, 5)
            if event_chance_cap < 0:
                events = 1
                
        elif event == 1:
            event_done = 'LOW LEVEL RADIATION HAZARD'
            mutation_rate += random.randint(2, 4)
            event_clock1 += random.randint(1, 10)
            
        elif event == 2:
            event_done = 'MEDIUM LEVEL ADIATION HAZARD'
            mutation_rate += random.randint(4, 6)
            event_clock1 += random.randint(5, 15)
            
        elif event == 3:
            event_done = 'HIGH LEVEL RADIATION HAZARD'
            mutation_rate += random.randint(6, 8)
            event_clock1 += random.randint(10, 20)
            
        elif event == 4:
            event_done = 'VOLCANIC ERRUPTION'
            temp_max += random.randint(3, 5)
            temperature += random.randint(1, 3)
            death_check = 0
            while len(population) != death_check:
                death_number = random.randint(1, 250)
                if death_number == 13:
                    if population[death_check][12] is True and breedable_count > 2:
                        del population[death_check]
                        death_check -= 1
                        deaths += 1
                        breedable_count -= 1
                death_check += 1
            event_clock2 += random.randint(2, 4)
                
        elif event == 5:
            event_done = 'FAMINE'
            food -= random.randint(3000, 9000)
            if food <= 0:
                food = 0
            if foodupdown == -1:
                fpg_cap -= 1000
                if fpg_cap < 5000:
                    fpg_cap = 5000
                    
        elif event == 6:
            event_done = 'PLAGUE'
            plague_check = 0
            while len(population) != plague_check:
                death_number = random.randint(0, 100)
                if death_number == 0:
                    population[plague_check][11] = True
                    plague_check += 1
                    
        elif event == 7:
            event_done = 'EARTHQUAKE'
            death_check = 0
            while len(population) != death_check:
                death_number = random.randint(1, 300)
                if death_number == 13:
                    if population[death_check][12] is True and breedable_count > 2:
                        del population[death_check]
                        death_check -= 1
                        deaths += 1
                        breedable_count -= 1
                death_check += 1
            event_clock3 += random.randint(1, 3)

        elif event == 8:
            event_done = 'CASSOWARY RAID'
            death_check = 0
            while len(population) != death_check:
                death_number = random.randint(1, 10)
                if death_number == 6:
                    del population[death_check]
                    death_check -=1
                    deaths += 1
                death_check += 1
        print(event_done)
        
    #temperature change
    print('    temperature change')
    if temp_state is True:
        temperature += temp_rate
    elif temp_state is False:
        temperature -= temp_rate

    if temperature >= temp_max or temperature <= 0-temp_max:
        if temp_state is True:
            temperature = temp_max
            temp_state = False
        else:
            temperature = 0-temp_max
            temp_state = True
        temp_max += random.randint(1, 2)
        temp_increase += 1
        temp_rate = 0.1 * temp_increase
        
    #temperature deaths
    print('    temperature deaths')
    temp_check = 0
    for i in range(len(population)):
        if population[temp_check][2] < temperature or 0-population[temp_check][2] > temperature:
            del population[temp_check]
            deaths += 1
            temp_check -= 1
        temp_check += 1
    
    #fatigue down
    print('    fatigue down')
    fatigue_check = 0
    for x in range(len(population)):
        if population[fatigue_check][9] > 0:
            population[fatigue_check][9] -= 1
        fatigue_check += 1
    
    #feeding
    print('    feeding')
    food_check = 0
    for x in range(len(population)):
        if population[food_check][8] == 0 and food > 0:
            food -= 1
            population[food_check][8] = population[food_check][0]
        food_check += 1
    
    #starvation check
    print('    starvation check')
    starve_check = 0
    for x in range(len(population)):
        if population[starve_check][8] == 0:
            del population[starve_check]
            starve_check -= 1
            deaths += 1
        starve_check += 1
    
    #virus deaths
    print('    virus killing')
    virus_check = 0
    for x in range(len(population)):
        virus_chance = random.randint(1, 100)
        if virus_chance <= virus.kill_chance:
            del population[virus_check]
            virus_check -= 1
            deaths += 1
            virus.food += random.randint(1, 3)
        virus_check += 1
    
    #deaths
    print('    deaths')
    death_check = 0
    while len(population) != death_check:
        death_number = random.randint(1, 100)
        if population[death_check][7] == population[death_check][4]:
            del population[death_check]
            death_check -= 1
        elif death_number <= population[death_check][3]:
            del population[death_check]
            deaths += 1
            death_check -= 1
        death_check += 1
    
    #generation of offspring
    print('    generation of offspring')
    births = 0
    completed = 0
    past_completed = 0
    breedable1 = []
    breedable2 = []
    
    
    while len(population) != completed:
        breedable1 = []
        breedable2 = []
        while breedable1 == []:
            if completed >= len(population):
                break
            if population[completed][12] is True:
                breedable1 = population[completed]
                past_completed = completed
            completed += 1
        if completed >= len(population):
                break
        
        while breedable2 == []:
            if completed >= len(population):
                break
            if  population[completed][12] is True:
                breedable2 = population[completed]
                break
            completed += 1
            
        if completed >= len(population):
            break
        
        if breedable2[1] > breedable1[1]:
            litter_cap = random.randint(breedable1[1], breedable2[1])
        elif breedable1[1] > breedable2[1]:
            litter_cap = random.randint(breedable2[1], breedable1[1])
        elif breedable1[1] == breedable2[1]:
            litter_cap = random.randint(breedable1[1], breedable2[1]+1)
        litter = 0
        
        while litter != litter_cap:
            baby = []
            for i in range(7):
                baby_inherit = random.randint(0, 1)
                if baby_inherit == 0:
                    baby.append(breedable1[i])
                else:
                    baby.append(breedable2[i])
                    
            mutationyesno = random.randint(1, 1000)
            if mutationyesno <= baby[5]*mutation_rate:
                stat = random.randint(0, 6)
                change = random.randint(0,1)
                if change == 0:
                    baby[stat] += random.randint(1, mutation_severity)
                elif change == 1:
                    baby[stat] -= random.randint(1, mutation_severity)
                
                if baby[1] <= 0:
                    baby[1] = 1
                if baby[4] <= 0:
                    baby[4] = 1
                if baby[6] <= -1:
                    baby[6] = 0
            baby.append(age)
            baby.append(fed)
            baby.append(fatigue)
            baby.append(b_c)
            
            if breedable1[11] is True or breedable2[11] is True:
                willinfect = random.randint(1, 100)
                if willinfect >= virus.infectiousness:
                    contaminated = True
            else:
                contaminated = False
            baby.append(contaminated)
            
            infant_death_yesno = random.randint(1, 100)
            if infant_death_yesno > baby[3]:
                offspring.append(baby)
            else:
                deaths += 1
            baby = []
            litter += 1
            births += 1
        f_added = random.randint(1, 2)
        population[completed][9] = (f_added + population[completed][10])
        population[past_completed][9] = (f_added + population[past_completed][10])
        population[completed][10] += 1
        population[past_completed][10] += 1
        
        completed += 1
        
    #aging of population
    print('    aging of population')
    age_check = 0
    while len(population) != age_check:
        population[age_check][7] += 1
        age_check += 1
    
    #hunger check
    print('    hunger check')
    hungry_check = 0
    for x in range(len(population)):
        population[hungry_check][8] -= 1
        hungry_check += 1
    
    #offspring added to population
    print('    offspring added to population')
    population.extend(offspring)
    
    #virus mutation
    print('    mutating virus')
    if virus.mutaion_chance >= random.randint(1, 100):
        virus_decider = random.randint(1, 4)
        change = random.randint(1, 2)
        if change == 2:
            change = -1
        
        if virus_decider == 1:
            virus.kill_chance += change
        elif virus_decider == 2:
            virus.mutaion_chance += change
        elif virus_decider == 3:
            virus.infectiousness +=  change
        elif virus_decider == 4:
            virus.metabolism += change
        
    #get averages
    print('    getting average genes')
    avr_m = avr_gen(population, 0)
    avr_r = avr_gen(population, 1)
    avr_t = avr_gen(population, 2)
    avr_d = avr_gen(population, 3)
    avr_a = avr_gen(population, 4)
    avr_s = avr_gen(population, 5)
    avr_b = avr_gen(population, 6)

    average_genome = [avr_m, avr_r, avr_t, avr_d, avr_a, avr_s, avr_b]

    virus_genome = [virus.kill_chance, virus.mutaion_chance, virus.infectiousness, virus.metabolism]

    #dead creatures converted to food.
    print('    dead creatures converted to food')
    for x in range(deaths):
        if random.randint(1, 20) == 1:
            food += 1
            
    #virus curing
    print('    curing virus')
    for i in range(len(population)):
        if population[i][11] is True:
            if random.randint(1, 100) == 1:
                population[i][11] = False

    #virus feeding/deaths
    print('    virus feeding and starvation')
    if met_clock == 0:
        for i in range(len(population)):
            if population[i][11] is True:
                if virus.food >= 1:
                    virus.food -= 1
            elif virus.food == 0:
                population[i][11] = False
        met_clock = virus.metabolism
    else:
        met_clock -= 1
    
    #virus check
    print('    checking for virus')
    virus.infected = 0
    for i in range(len(population)):
        if population[i][11] is True:
            virus.infected += 1
    
    #resets
    print('    resets')
    offspring = []
    generation += 1
    breedable_count = 0
    
    #facts
    print('---------------------------------------------')
    print(f'generation: {generation}')
    print(f"population: {len(population)}")
    print(f"deaths: {deaths}")
    print(f"births: {births}")
    if len(population) != 0:
        print(f"net growth: {(births - deaths)/len(population)}%")
    else:
        print("net growth: -100%")
    print(f'food: {food}')
    print(f'temperature: {temperature}')
    print(f'virus infected: {virus.infected}')
    print(f'average genome: {average_genome}')
    print(f'virus genome: {virus_genome}')
    print('---------------------------------------------')
    
    with open(file_name, 'a') as output:
        output.write(f'generation: {generation}\n')
        output.write(f'population: {len(population)}\n')
        output.write(f"deaths: {deaths}\n")
        output.write(f'births: {births}\n')
        if len(population) != 0:
            output.write(f'net growth: {(births - deaths)/len(population)}%\n')
        else:
            output.write("net growth: -100%\n")
        output.write(f'food: {food}\n')
        output.write(f'temperature: {temperature}\n')
        output.write(f'infected: {virus.infected}\n')
        output.write(f'average genome: {average_genome}\n')
        output.write(f'virus genome: {virus_genome}\n')
        if event_done != "":
            output.write(f'event: {event_done}\n')
        output.write('---------------------------------------------\n')
        if len(population) == 0:
            output.write("every thing died\n")
        output.close()
    
    with open(file_name_raw, 'a') as output:
        output.write(f'{generation}\n')
        output.write(f'{len(population)}\n')
        output.write(f"{deaths}\n")
        output.write(f'{births}\n')
        if len(population) != 0:
            output.write(f'{(births - deaths)/len(population)}%\n')
        else:
            output.write("-100%\n")
        output.write(f'{food}\n')
        output.write(f'{temperature}\n')
        output.write(f'{virus.infected}\n')
        output.write(f'{average_genome[0]}\n')
        output.write(f'{average_genome[1]}\n')
        output.write(f'{average_genome[2]}\n')
        output.write(f'{average_genome[3]}\n')
        output.write(f'{average_genome[4]}\n')
        output.write(f'{average_genome[5]}\n')
        output.write(f'{average_genome[6]}\n')
        output.close()
    
    if len(population) == 0:
        print("everh thing died")
        break
