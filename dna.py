import random

# set of characters to select from
chars = range(32,128)

# target phrase
target = "back in the saddle again"

mutationRate = 0.01

# defines what a new "DNA" is
class DNA:

    # gets called with a new DNA object is created
    def __init__(self):

        # genes is a string, basically, representing the attempt to match target
        self.genes = []

        # initially, the guesses are all random strings
        for i in range(len(target)):
            gene = chr(random.choice(chars))
            self.genes.append(gene)

    # update_fitness counts how many spaces happen to match
    def update_fitness(self):
        score = 0
        for i in range(len(self.genes)):
            if self.genes[i] == target[i]:
                score += 1

        # final fitness score is reported as a percentage
        self.fitness = float(score)/len(target)

    # this is how "mating" works in this genetic algorithm, combining two DNA sequences
    def crossover(self, partner):

        # create a new DNA object
        child = DNA()

        # randomly determine how much of a child's genes come from each parent
        midpoint = random.choice(range(len(self.genes)))

        # construct the child's genes from the parents'
        for i in range(len(self.genes)):
            if i > midpoint:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = partner.genes[i]

        return child

    # mutation is necessary in the wild for random successes to "breed in"
    def mutate(self):
        for i in range(len(self.genes)):
            if random.random() < mutationRate:
                self.genes[i] = chr(random.choice(chars))

    # prints out the genes comprising that DNA object
    def getPhrase(self):
        return ''.join(self.genes)