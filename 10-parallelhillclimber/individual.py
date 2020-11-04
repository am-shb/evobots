import math
import random
import pyrosim
import numpy
from robot import ROBOT


class INDIVIDUAL:
    def __init__(self, id):
        self.genome = numpy.random.random(4) * 2 - 1
        self.fitness = 0
        self.ID = id

    def Start_Evaluation(self, pb = True):
        self.sim = pyrosim.Simulator(play_paused=False, eval_time=300, play_blind=pb)

        self.robot = ROBOT(self.sim, self.genome)

        self.sim.start()


    def Compute_Fitness(self):
        self.sim.wait_to_finish()

        y = self.sim.get_sensor_data(sensor_id=self.robot.P4, svi=1)
        self.fitness = y[-1]

        del self.robot
        del self.sim

    def Mutate(self):
        geneToMutate = random.randint(0, 3)
        self.genome[geneToMutate] = random.gauss(self.genome[geneToMutate], math.fabs(self.genome[geneToMutate]))

    def Print(self):
        print("[%d %f] " % (self.ID, self.fitness), end='')