import copy
from population import POPULATION

parents = POPULATION(5)
parents.Evaluate()
# parents.Print()

for i in range(100):
    children = copy.deepcopy(parents)
    children.Mutate()
    children.Evaluate()
    parents.replaceWith(children)
    print(i, end=' ')
    parents.Print()
