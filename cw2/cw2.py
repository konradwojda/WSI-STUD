from cec2017.functions import f4
import numpy as np
from random import randint
from statistics import stdev

UPPER_BOUND = 100
T_MAX = 10000


def evolutionary_algorithm(fun, start_population, mutation_factor, elite_size):
    t = 0
    ratings = rating(fun, start_population)
    curr_best_rating, curr_best = find_best(start_population, ratings)
    population = start_population.copy()
    while not stop(t, population, curr_best):
        reproduced = reproduction(population, ratings)
        mutated = mutation(reproduced, mutation_factor)
        new_ratings = rating(fun, mutated)
        temp_best_rating, temp_best = find_best(mutated, new_ratings)
        if temp_best_rating <= curr_best_rating:
            curr_best = temp_best.copy()
            curr_best_rating = temp_best_rating
        new_population = elite_succession(
            population, mutated, ratings, new_ratings, elite_size)
        population = [member[1] for member in new_population]
        ratings = [member[0] for member in new_population]
        t += 1
    return curr_best


def stop(t, population, value):
    return (t >= (T_MAX / len(population)) - 1)


def rating(fun, population):
    return [fun(member) for member in population]


def find_best(population, rating):
    return min(zip(rating, population))


def reproduction(population, rating):
    new_population = []
    for _ in range(len(population)):
        first = randint(0, len(population) - 1)
        second = randint(0, len(population) - 1)
        new_population.append(
            population[first] if rating[first] <= rating[second] else population[second])
    return new_population


def mutation(population, mutation_factor):
    return [(member + (np.random.normal(size=2) * mutation_factor)) for member in population]


def elite_succession(population, modified_population, rating, mod_rating, elite_size):
    sorted_members = sorted(zip(rating, population))
    elite = sorted_members[:elite_size]
    new_population = list(zip(mod_rating, modified_population)) + elite
    new_population.sort()
    for _ in range(elite_size):
        new_population.pop()
    return new_population


if __name__ == "__main__":
    results = []
    print("min\t|\tavg\t|\tstdev\t|\tmax")
    # for X in [10, 20, 30, 50, 80, 100]:
    for X in [0, 1, 2, 3, 5, 10, 15, 20]:
        # for X in [0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0]:
        for _ in range(25):
            pop = []
            for _ in range(20):
                pop.append(
                    np.random.uniform(-UPPER_BOUND, UPPER_BOUND, size=2))
            results.append(f4(evolutionary_algorithm(f4, pop, 1.0, X)))
        print(str(X) + " | " + str(min(results)) + " | " + str((sum(results) /
              len(results))) + " | " + str(stdev(results)) + " | " + str(max(results)))
        results = []
