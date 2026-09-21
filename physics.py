GRAVITY = -9.81

def update_aircraft(aircraft, dt):

    aircraft.acc[2] = GRAVITY

    #v new = v old + a * dt
    aircraft.vel[0] += aircraft.acc[0] * dt
    aircraft.vel[1] += aircraft.acc[1] * dt
    aircraft.vel[2] += aircraft.acc[2] * dt

    #p new = p old + v * dt
    aircraft.pos[0] += aircraft.vel[0] * dt
    aircraft.pos[1] += aircraft.vel[1] * dt
    aircraft.pos[2] += aircraft.vel[2] * dt

