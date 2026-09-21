class Aircraft:
    def __init__(self):

        self.mass = 10000
        self.thrust = 10000.0
        #position in meters
        self.pos = [0, 0, 1000.0]
        #velocity in meters per second
        self.vel = [100.0, 0, 0]
        #acceleration in meters per second squared
        self.acc = [0, 0, 0]
        #angular velocity in radians per second
        self.ang_vel = [0, 0, 0]
        self.forces = [0.0, 0.0, 0.0]

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
    def get_forces(self):
            return self.forces
    def get_thrust(self):
        return self.thrust
    