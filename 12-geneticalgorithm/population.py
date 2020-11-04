from individual import INDIVIDUAL
import copy
import random

class POPULATION:
    def __init__(self, popSize):
        self.p = {}
        self.popSize = popSize


    def Initialize(self):
        for i in range(self.popSize):
            self.p[i] = INDIVIDUAL(i)

    
    def Evaluate(self, pb=True):
        for i in self.p:
            self.p[i].Start_Evaluation(pb)
        
        for i in self.p:
            self.p[i].Compute_Fitness()


    def Mutate(self):
        for i in self.p:
            self.p[i].Mutate()


    def replaceWith(self, other):
        for i in self.p:
            if self.p[i].fitness < other.p[i].fitness:
                self.p[i] = other.p[i]

    
    def Fill_From(self, other):
        self.Copy_Best_From(other)
        self.Collect_Children_From(other)

    
    def Copy_Best_From(self, other):
        best = other.p[0]
        max_fitness = other.p[0].fitness
        for i in other.p:
            if other.p[i].fitness > max_fitness:
                best = other.p[i]
                max_fitness = other.p[i].fitness
        
        self.p[0] = copy.deepcopy(best)


    def Collect_Children_From(self, other):
        for i in range(1, self.popSize):
            winner = other.Winner_Of_Tournament_Selection()
            self.p[i] = copy.deepcopy(winner)
            self.p[i].Mutate()


    def Winner_Of_Tournament_Selection(self):
        p1, p2 = random.sample(range(self.popSize), 2)
        if self.p[p1].fitness > self.p[p2].fitness:
            return self.p[p1]
        return self.p[p2]


    def Print(self):
        for i in self.p:
            self.p[i].Print()
        print()