from aircraft import Aircraft
from physics import update_aircraft
from vpython import rate
from visuals import update_visuals

aircraft = Aircraft()

dt = 1/60
time = 0.0

while aircraft.pos[2] > 0:
    update_aircraft(aircraft, dt)
    rate(60) # loop 60 times per second
    update_visuals(aircraft)
    time += dt

print("Aircraft has hit the ground.")
print("Time taken:", round(time, 2), "seconds")
print("Position:", [round(value, 2) for value in aircraft.pos])
print("Velocity:", [round(value, 2) for value in aircraft.vel])
print("Acceleration:", [round(value, 2) for value in aircraft.acc], "m/s^2")
print("Thrust:", round(aircraft.thrust, 2), "N")
print("Reference Area:", round(aircraft.reference_area, 2), "m^2")
print("Drag:", round(aircraft.drag, 2), "N")