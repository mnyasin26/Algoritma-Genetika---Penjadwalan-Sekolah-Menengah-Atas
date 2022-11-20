# TODO Bikin gen yang isinya random (99,99%)
# TODO Fitness/Cost Function (95%)
# TODO Generate Population (100%)
# TODO Selection (100%)
# TODO Crossover (100%)
# TODO Mutation (99%)
# TODO reassign population (eliminate weak gen) (100%)
# TODO Main Looping and Termination
# TODO Logging
# TODO Finalization
# TODO Develop Website
# TODO Deploy Website

import json
import os
clear = lambda: os.system('cls')

from function import generate_population
from function import selection
from function import crossover
from function import mutation
from function import reassign_gen
from function import filter_guru

from copy import deepcopy

input_file = 'input.json'
output_file = 'classes/output3.json'

# Baca data json
def load_data(path):
    with open(path, 'r') as read_file:
        data = json.load(read_file)

    return data

# Masukan data json ke variabel
data = load_data(input_file)
# Menyaring data Guru pada Mapel menjadi unique
filter_guru.filter_guru(data)

# Parameter
gen_num = 4 # Banyaknya individu dalam populasi
laju_mutasi = 0.04
population = generate_population.generate_population(gen_num, data)
max_generation = 5000 # batas maksimal iterasi

# Main Looping
i = 0
for i in range(0, max_generation):
    # Logging
    if i % 10 == 0:
        clear()
        print("Iteration: " + str(i))
        j = 1
        for individu in population:
            print("\nIndividu-"+ str(j))
            # Cost-1 = Mapel yang dibagi 2 tetapi terdapat pada satu hari 
            print("Cost-1: " + str(individu['Cost_cons1']))
            # Cost-2 = Konflik jadwal guru yang mengajar kelas berbeda tetapi pada saat waktu yang sama
            print("Cost-2: " + str(individu['Cost_cons2']))
            print("Total Cost: "+ str(individu['Cost']))
            j += 1

    # Terminate ketika semua constrains satisfied
    if population[0]['Cost'] == 0:
        break

    # Seleksi
    parent1, parent2 = deepcopy(selection.selection(population))
    # Crossover
    child1, child2 = deepcopy(crossover.crossover(parent1, parent2, data))
    # Mutasi
    mutation.mutation_func(child1, data, laju_mutasi)
    mutation.mutation_func(child2, data, laju_mutasi)
    # Masukkan individu hasil mutasi ke populasi
    reassign_gen.reassign(population, child1, child2)  

# Fungsi untuk menulis hasil solusi/gen/kromosom/individu ke file
def write_data(data, path):
    with open(path, 'w') as write_file:
        json.dump(data, write_file, indent=4)

# Ambil timetable terbaik lalu tuliskan ke file
write_data(population[0]['Timetable'], 'output.json')
