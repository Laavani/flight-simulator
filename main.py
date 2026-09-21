from aircraft import Aircraft
from physics import update_aircraft

aircraft = Aircraft()

dt = 0.01
time = 0.0

while aircraft.pos[2] > 0:
    update_aircraft(aircraft, dt)
    time += dt

print("Aircraft has hit the ground.")
print("Time taken:", round(time, 2), "seconds")
print("Position:", [round(value, 2) for value in aircraft.pos])
print("Velocity:", [round(value, 2) for value in aircraft.vel])
print("Acceleration:", [round(value, 2) for value in aircraft.acc], "m/s^2")
print("Thrust:", round(aircraft.thrust, 2), "N")
