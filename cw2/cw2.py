from cec2017.functions import f4
import numpy as np
from random import randint

def evolutionary_algorithm(fun, start_population, mutation_factor, elite_size, t_max):
    t = 0
    ratings = rating(fun, start_population)
    curr_best = find_best(start_population, ratings)
    population = start_population.copy()
    while not stop(t, t_max, population, curr_best):
        reproducted = reproduction(population, ratings)
        mutated = mutation(reproduced, mutation_factor)
        ratings = rating(fun, mutated)
        temp_best = find_best(fun, mutated)
        if fun(temp_best) <= fun(curr_best):
            curr_best = temp_best.copy()
        population = elite_succession(population, mutated, ratings, 2)
        t += 1
    return curr_best

def stop(t, t_max, population, value):
    return (t >= t_max)

def rating(fun, population):
    return [fun(member) for member in population]

def find_best(population, rating):
    return population[min(rating)]

def reproduction(population, rating):
    new_population = []
    for _ in range(population.size):
        first = randint(0, population.size)
        second = randint(0, population.size)
        new_population.append(population[first] if rating[first] >= rating[second] else second)
    return np.array(new_population)
def mutation(population, mutation_factor):
    pass

def elite_succession(population, modified_population, rating, elite_size):
    pass