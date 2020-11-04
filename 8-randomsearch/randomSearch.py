import matplotlib.pyplot as plt
import random
from individual import INDIVIDUAL

for i in range(10):
    individual = INDIVIDUAL()
    individual.Evaluate()
    print(individual.fitness)


# f = plt.figure()
# f.add_subplot(131)
# plt.plot(x)
# f.add_subplot(132)
# plt.plot(y)
# f.add_subplot(133)
# plt.plot(z)
# plt.show()