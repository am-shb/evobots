import random
import pyrosim
from robot import ROBOT


class INDIVIDUAL:
    def __init__(self):
        self.genome = random.random() * 2 - 1
        self.fitness = 0
        print(self.genome)

    def Evaluate(self):
        sim = pyrosim.Simulator(play_paused=False, eval_time=300)

        robot = ROBOT(sim, self.genome)

        sim.start()
        sim.wait_to_finish()

        y = sim.get_sensor_data(sensor_id=robot.P4, svi=1)
        self.fitness = y[-1]