import constants as c
from environments import ENVIRONMENTS

envs = ENVIRONMENTS(c.numEnvs)

# import copy
# import constants as c
from population import POPULATION

parents = POPULATION(c.popSize)
parents.Initialize()
parents.Evaluate(envs, pp=False, pb=True)
print('0', end=' ')
parents.Print()

for i in range(1, c.numGens):
    children = POPULATION(c.popSize)
    children.Fill_From(parents)
    children.Evaluate(envs, pp=False, pb=True)
    print(i, end=' ')
    children.Print()
    parents.replaceWith(children)

best = parents.p[0]
for e in envs.envs:
    best.Start_Evaluation(envs.envs[e], pp=False, pb=False)
    best.Compute_Fitness()