import constants as c

class ROBOT:
    def __init__(self, sim, wts):
        self.send_objects(sim)
        self.send_joints(sim)
        self.send_sensors(sim)
        self.send_neurons(sim)
        self.send_synapses(sim, wts)

        del self.O, self.J, self.S, self.SN, self.MN

    def send_objects(self, sim):
        self.O = {}
        self.O[0] = sim.send_box(x=0, y=0, z=c.L+c.R, length=c.L, width=c.L, height=2*c.R, r=0.5, g=0.5, b=0.5)
        self.O[1] = sim.send_cylinder(x=0, y=c.L, z=c.L+c.R, length=c.L, radius=c.R, r1=0, r2=1, r3=0, r=1, g=0, b=0)
        self.O[2] = sim.send_cylinder(x=c.L, y=0, z=c.L+c.R, length=c.L, radius=c.R, r1=1, r2=0, r3=0, r=0, g=1, b=0)
        self.O[3] = sim.send_cylinder(x=0, y=-c.L, z=c.L+c.R, length=c.L, radius=c.R, r1=0, r2=1, r3=0, r=0, g=0, b=1)
        self.O[4] = sim.send_cylinder(x=-c.L, y=0, z=c.L+c.R, length=c.L, radius=c.R, r1=1, r2=0, r3=0, r=1, g=0, b=1)
        self.O[5] = sim.send_cylinder(x=0, y=1.5*c.L, z=c.L/2+c.R, length=c.L, radius=c.R, r1=0, r2=0, r3=1, r=1, g=0, b=0)
        self.O[6] = sim.send_cylinder(x=1.5*c.L, y=0, z=c.L/2+c.R, length=c.L, radius=c.R, r1=0, r2=0, r3=1, r=0, g=1, b=0)
        self.O[7] = sim.send_cylinder(x=0, y=-1.5*c.L, z=c.L/2+c.R, length=c.L, radius=c.R, r1=0, r2=0, r3=1, r=0, g=0, b=1)
        self.O[8] = sim.send_cylinder(x=-1.5*c.L, y=0, z=c.L/2+c.R, length=c.L, radius=c.R, r1=0, r2=0, r3=1, r=1, g=0, b=1)


    def send_joints(self, sim):
        self.J = {}
        self.J[0] = sim.send_hinge_joint(first_body_id=self.O[0], second_body_id=self.O[1], x=0, y=c.L/2, z=c.L+c.R, n1=-1, n2=0, n3=0)
        self.J[1] = sim.send_hinge_joint(first_body_id=self.O[1], second_body_id=self.O[5], x=0, y=1.5*c.L, z=c.L+c.R, n1=-1, n2=0, n3=0)
        self.J[2] = sim.send_hinge_joint(first_body_id=self.O[0], second_body_id=self.O[2], x=c.L/2, y=0, z=c.L+c.R, n1=0, n2=1, n3=0)
        self.J[3] = sim.send_hinge_joint(first_body_id=self.O[2], second_body_id=self.O[6], x=1.5*c.L, y=0, z=c.L+c.R, n1=0, n2=1, n3=0)
        self.J[4] = sim.send_hinge_joint(first_body_id=self.O[0], second_body_id=self.O[3], x=0, y=-c.L/2, z=c.L+c.R, n1=1, n2=0, n3=0)
        self.J[5] = sim.send_hinge_joint(first_body_id=self.O[3], second_body_id=self.O[7], x=0, y=-1.5*c.L, z=c.L+c.R, n1=1, n2=0, n3=0)
        self.J[6] = sim.send_hinge_joint(first_body_id=self.O[0], second_body_id=self.O[4], x=-c.L/2, y=0, z=c.L+c.R, n1=0, n2=-1, n3=0)
        self.J[7] = sim.send_hinge_joint(first_body_id=self.O[4], second_body_id=self.O[8], x=-1.5*c.L, y=0, z=c.L+c.R, n1=0, n2=-1, n3=0)


    def send_sensors(self, sim):
        self.S = {}
        self.S[0] = sim.send_touch_sensor(body_id=self.O[5])
        self.S[1] = sim.send_touch_sensor(body_id=self.O[6])
        self.S[2] = sim.send_touch_sensor(body_id=self.O[7])
        self.S[3] = sim.send_touch_sensor(body_id=self.O[8])
        self.L4  = sim.send_light_sensor(body_id=self.O[0])
        self.S[4] = self.L4


    def send_neurons(self, sim):
        self.SN = {}
        for s in self.S:
            self.SN[s] = sim.send_sensor_neuron(sensor_id=self.S[s])
        
        self.MN = {}
        for j in self.J:
            self.MN[j] = sim.send_motor_neuron(joint_id=self.J[j], tau=0.3)


    def send_synapses(self, sim, wts):
        for j in self.SN:
            for i in self.MN:
                sim.send_synapse(source_neuron_id=self.SN[j], target_neuron_id=self.MN[i], weight=wts[j,i])