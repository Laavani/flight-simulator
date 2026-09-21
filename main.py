from aircraft import Aircraft
from physics import update_aircraft

aircraft = Aircraft()

dt = 0.01
time = 0.0

while aircraft.pos[2] > 0:
    update_aircraft(aircraft, dt)
    time += dt

print("Aircraft has hit the ground.")
print("Time taken:", time)
print("Position:", aircraft.pos)
print("Velocity:", aircraft.vel)
