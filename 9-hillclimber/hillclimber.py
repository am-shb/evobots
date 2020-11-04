import matplotlib.pyplot as plt
import random, copy
import pickle
from individual import INDIVIDUAL

parent = INDIVIDUAL()
parent.Evaluate(False)
print(parent.fitness)

for i in range(100):
    child = copy.deepcopy(parent)
    child.Mutate()
    child.Evaluate()
    print("[g: %d] [pw: %f] [p: %f] [c: %f]" % (i, parent.genome, parent.fitness, child.fitness))

    if child.fitness > parent.fitness:
        child.Evaluate(False)
        parent = child

        f = open('robot.p','wb')
        pickle.dump(parent , f)
        f.close()

