import math
import random
import pyrosim
import numpy
import constants as c
from robot import ROBOT


class INDIVIDUAL:
    def __init__(self, id):
        self.genome = numpy.random.random((5,8)) * 2 - 1
        self.fitness = 0
        self.ID = id

    def Start_Evaluation(self, env, pp=False, pb = True):
        self.sim = pyrosim.Simulator(play_paused=pp, eval_time=c.evalTime, play_blind=pb)

        self.robot = ROBOT(self.sim, self.genome)
        env.Send_To(self.sim)

        self.sim.start()


    def Compute_Fitness(self):
        self.sim.wait_to_finish()

        distance = self.sim.get_sensor_data(sensor_id=self.robot.L4)
        self.fitness += distance[-1]

        del self.robot
        del self.sim

    def Mutate(self):
        r = random.randint(0, 4)
        c = random.randint(0, 7)
        self.genome[r,c] = random.gauss(self.genome[r,c], math.fabs(self.genome[r,c]))
        self.genome = numpy.clip(self.genome, -1, 1)

    def Print(self):
        print("[%d %f] " % (self.ID, self.fitness), end='')