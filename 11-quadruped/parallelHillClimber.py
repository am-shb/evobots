import copy
from population import POPULATION

parents = POPULATION(5)
parents.Evaluate()

for i in range(1000):
    children = copy.deepcopy(parents)
    children.Mutate()
    children.Evaluate()
    parents.replaceWith(children)
    print(i, end=' ')
    parents.Print()

parents.Evaluate(False)