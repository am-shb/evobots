import copy
from population import POPULATION

parents = POPULATION(10)
parents.Initialize()
parents.Evaluate()
print('0', end=' ')
parents.Print()

for i in range(1, 500):
    children = POPULATION(10)
    children.Fill_From(parents)
    children.Evaluate()
    print(i, end=' ')
    children.Print()
    parents.replaceWith(children)

best = parents.p[0]
best.Start_Evaluation(False)
best.Compute_Fitness()