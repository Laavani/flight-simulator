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
        self.force = [0.0, 0.0, 0.0]
        #reference area in square meters
        self.reference_area = 20.0
        self.drag_coefficient = 0.02
        self.drag = 0.0

        self.roll = 0.0
        self.pitch = 0.0
        self.yaw = 0.0

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
            return self.force
    def get_thrust(self):
        return self.thrust
    def get_reference_area(self):
        return self.reference_area
    def get_roll(self):
        return self.roll
    def get_pitch(self):
        return self.pitch
    def get_yaw(self):
        return self.yaw
    