class Aircraft:
    def __init__(self):
        self.mass = 5000
        self.pos = [0, 0, 0]
        self.vel = [0, 0, 0]
        self.acc = [0, 0, 0]
        self.ang_vel = [0, 0, 0]

    def get_pos(self):
        return self.pos
    def get_vel(self):
        return self.vel
    def get_mass(self):
        return self.mass
    def get_acc(self):
        return self.acc
    def get_ang_vel(self):
        return self.ang_vel