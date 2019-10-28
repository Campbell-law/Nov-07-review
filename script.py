import random

from dna import DNA

# how many DNA objects should be in the population
population_size = 1000

# target is ultimately 1.00, a perfect match
bestScore = 0

# holds our population
population = []

# keeps count of how long it takes to get the final result
generation = 1

# randomly generate the first 1,000 entities
for i in range(int(population_size)):
    population.append(DNA())

# until we've found the perfect match
while bestScore < 1.0:

    # calculate the best score of available options
    for i in range(len(population)):
        population[i].update_fitness()

        # if this is the new best string, print it out
        if population[i].fitness > bestScore:
            bestScore = population[i].fitness
            print(f"Generation #{generation:3}: {population[i].getPhrase()}  score:  {bestScore:.3f}".replace(chr(127), " "))

    # create the new mating pool of options
    matingPool = []

    # copy over the previous generation's population into a temporary array
    previous_population = population[:]
    population = []

    # look at each item in the old population, add them to the mating pool depending on how 'good' they are
    for i in range(len(previous_population)):
        n = int(previous_population[i].fitness * 100)
        for j in range(n):
            matingPool.append(previous_population[i])

    # randomly generate 1,000 new entities based on the mating pool
    for i in range(len(previous_population)):
        a = random.choice(range(len(matingPool)))
        b = random.choice(range(len(matingPool)))

        # create the new entity from the randomly chosen parents
        parentA = matingPool[a]
        parentB = matingPool[b]
        child = parentA.crossover(parentB)
        child.mutate()

        # add the new entity to the next generation's population
        population.append(child)

    # all done with this generation, onto the next!
    generation += 1