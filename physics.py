GRAVITY = -9.81

def update_aircraft(aircraft, dt):

    aircraft.force = [0.0, 0.0, 0.0]

    #gravity
    aircraft.force[2] += aircraft.mass * GRAVITY
    aircraft.force[0] += aircraft.thrust

    # F = m * a => a = F / m
    aircraft.acc[0] = aircraft.force[0] / aircraft.mass
    aircraft.acc[1] = aircraft.force[1] / aircraft.mass
    aircraft.acc[2] = aircraft.force[2] / aircraft.mass

    #v new = v old + a * dt
    aircraft.vel[0] += aircraft.acc[0] * dt
    aircraft.vel[1] += aircraft.acc[1] * dt
    aircraft.vel[2] += aircraft.acc[2] * dt

    #p new = p old + v * dt
    aircraft.pos[0] += aircraft.vel[0] * dt
    aircraft.pos[1] += aircraft.vel[1] * dt
    aircraft.pos[2] += aircraft.vel[2] * dt

