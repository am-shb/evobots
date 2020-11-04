import matplotlib.pyplot as plt
import pyrosim
import random
from robot import ROBOT

for i in range(10):
    sim = pyrosim.Simulator(play_paused=True, eval_time=300)

    robot = ROBOT(sim, random.random()*2 - 1)

    sim.start()
    sim.wait_to_finish()

# sensorData = sim.get_sensor_data( sensor_id = P2 )
# print(sensorData)

# f = plt.figure()
# panel = f.add_subplot(111)
# panel.set_ylim(-2,+0.5)
# plt.plot(sensorData)
# plt.show()