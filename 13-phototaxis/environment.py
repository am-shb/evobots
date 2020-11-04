import constants as c


class ENVIRONMENT:
    def __init__(self, id):
        self.ID = id
        self.l = c.L
        self.w = c.L
        self.h = c.L

        if self.ID == 0:
            self.Place_Light_Source_To_The_Front()
        elif self.ID == 1:
            self.Place_Light_Source_To_The_Right()
        elif self.ID == 2:
            self.Place_Light_Source_To_The_Back()
        elif self.ID == 3:
            self.Place_Light_Source_To_The_Left()


    def Place_Light_Source_To_The_Front(self):
        self.x = 0
        self.y = 30 * c.L
        self.z = c.L / 2


    def Place_Light_Source_To_The_Right(self):
        self.x = 30 * c.L
        self.y = 0
        self.z = c.L / 2


    def Place_Light_Source_To_The_Back(self):
        self.x = 0
        self.y = -30 * c.L
        self.z = c.L / 2


    def Place_Light_Source_To_The_Left(self):
        self.x = -30 * c.L
        self.y = 0
        self.z = c.L / 2


    def Send_To(self, sim):
        lightSource = sim.send_box(x=self.x, y=self.y, z=self.z, width=self.w, height=self.h, length=self.l)
        sim.send_light_source(body_id=lightSource)