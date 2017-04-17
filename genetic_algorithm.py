import random

#get_fitness=how probably the answer(guess) is it close to the correct value
def get_fitness(guess):
    return sum(1 for expected, actual in zip(target, guess)
               if expected == actual)
#generate_parent=generate a combintion of letter with the len of the inserted value
def generate_parent(length):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    return ''.join(genes)

#mutate=change one random letter in a sequence 
def mutate(parent):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate \
        if newGene == childGenes[index] \
        else newGene
    return ''.join(childGenes)


if __name__ == "__main__":
	random.seed()
	geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
	target = "Hello World!"

	bestParent = generate_parent(len(target))
	bestFitness = get_fitness(bestParent)
	print(bestParent)
	while True:
	    child = mutate(bestParent)
	    childFitness = get_fitness(child)

	    if bestFitness >= childFitness:
	        continue
	    print("this is my guess: "+child)
	    if childFitness >= len(bestParent):
	    	print("got your message",child,"in ",childFitness, "time")
	        break
	    bestFitness = childFitness
	    bestParent = child
