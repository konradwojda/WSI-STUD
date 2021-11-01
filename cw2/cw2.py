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
        new_ratings = rating(fun, mutated)
        temp_best = find_best(fun, mutated)
        if fun(temp_best) <= fun(curr_best):
            curr_best = temp_best.copy()
        population = elite_succession(population, mutated, ratings, new_ratings, 2)
        ratings = new_ratings.copy()
        t += 1
    return curr_best

def stop(t, t_max, population, value):
    return (t >= t_max)

def rating(fun, population):
    return [fun(member) for member in population]

def find_best(population, rating):
    return sorted(zip(rating, population))[0][1]

def reproduction(population, rating):
    new_population = []
    for _ in range(population.size):
        first = randint(0, population.size)
        second = randint(0, population.size)
        new_population.append(population[first] if rating[first] >= rating[second] else population[second])
    return np.array(new_population)

def mutation(population, mutation_factor):
    return np.array([np.random.normal(member, mutation_factor) for member in population])

def elite_succession(population, modified_population, rating, mod_rating, elite_size):
        sorted_members = sorted(zip(rating, population))
        sorted_modified_members = sorted(zip(mod_rating, modified_population))
        for _ in range(elite_size):
            sorted_modified_members.pop()
        for n in range(elite_size):
            sorted_modified_members.append(sorted_members[n])
        return np.array([member[1] for member in sorted_modified_members])
