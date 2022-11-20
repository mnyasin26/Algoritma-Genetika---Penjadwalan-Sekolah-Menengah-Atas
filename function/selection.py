# Selection, mencari 2 individu terbaik pada populasi
from copy import deepcopy

def selection(population):
    population_temp = deepcopy(population)

    # Mencari individu terbaik
    temp = {}
    for i in range(0, len(population_temp)):
        temp[i] = population_temp[i]['Cost']
    index = min(temp, key=temp.get)
    parent1 = deepcopy(population_temp[index])
    # Pop individu untuk parent1
    population_temp.pop(index)

    # Mencari individu terbaik
    temp = {}
    for i in range(0, len(population_temp)):
        temp[i] = population_temp[i]['Cost']
    index = min(temp, key=temp.get)
    parent2 = deepcopy(population_temp[index])
    
    # return 2 individu terbaik
    return parent1, parent2
