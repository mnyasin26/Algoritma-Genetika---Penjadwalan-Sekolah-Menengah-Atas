# Crossover Function
from copy import deepcopy
from function import calc_cost

def crossover(parent1, parent2, data):
    child1 = deepcopy(parent1)
    child2 = deepcopy(parent2)
    # Tukar angkatan kelas VII
    child1['Timetable']['VII'] = parent2['Timetable']['VII']
    child2['Timetable']['VII'] = parent1['Timetable']['VII']
    # Hitung Costnya Kembali
    child1['Cost'] = calc_cost.cost_function(child1['Timetable'], data)[0]
    child2['Cost'] = calc_cost.cost_function(child2['Timetable'], data)[0]

    return child1, child2
