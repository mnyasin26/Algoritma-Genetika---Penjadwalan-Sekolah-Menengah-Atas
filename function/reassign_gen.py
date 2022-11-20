# Reassign individu (eliminate first)
from copy import deepcopy

# Hapus 2 gen yang nilai costnya paling tinggi
def eliminate(population):
    # Pop individu dengan cost tertinggi
    temp = {}
    for i in range(0, len(population)):
        temp[i] = population[i]['Cost']
    index = max(temp, key=temp.get)
    population.pop(index)
    # Pop individu dengan cost tertinggi
    temp = {}
    for i in range(0, len(population)):
        temp[i] = population[i]['Cost']
    index = max(temp, key=temp.get)
    population.pop(index)

# Masukkan gen ke dalam populasi
def reassign(population, child1, child2):
    eliminate(population)
    gen1 = deepcopy(child1)
    gen2 = deepcopy(child2)

    population.append(gen1)
    population.append(gen2)
