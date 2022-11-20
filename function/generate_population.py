# Generate Population
from function import generate_individu
from function import calc_cost

# num = banyaknya gen/individu
# data = timetable
# return population = populasi yang berisi gen sebanyak num_gen
def generate_population(num: int, data):
    population = []
    for i in range(0, num):
        # Membuat gen dan Menghitung Cost dari gen
        individu = {}
        individu['Timetable'] = generate_individu.generate_individu(data)
        temp_cost = calc_cost.cost_function(individu['Timetable'], data)
        individu['Cost'] = temp_cost[0]
        individu['Cost_cons1'] = temp_cost[1]
        individu['Cost_cons2'] = temp_cost[2]
        population.append(individu)
    return population
