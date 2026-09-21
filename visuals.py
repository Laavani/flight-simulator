from vpython import *
# in powershell: python -m pip install -r reqs.txt

scene = canvas(
    title="6-DOF Flight Simulator",
    width=1200,
    height=600,
)

hud = label(
    pixel_pos=True,
    pos=vector(100, 150, 0),
    text="ALTITUDE: 1000 m\nSPEED: 10 m/s\n\nROLL: 0.0°\nPITCH: 0.0°\nYAW: 0.0°"
)

body = box(
    pos=vector(0, 0, 0),
    size=vector(6, 1.5, 1.5)
)
nose = cone(
    pos=vector(3, 0, 0),
    axis=vector(2, 0, 0),
    radius=0.75
)
left_wing = box(
    pos=vector(0, 0, 0),
    size=vector(2.5, 5, 0.2)
)
tail = box(
    pos=vector(-2.3, 0, 0),
    size=vector(1, 2.5, 0.2)
)

plane = compound([body, nose, left_wing, tail])

def update_visuals(position, velocity):
    plane.pos = vector(position[0], position[1], position[2])
    hud.text = f"ALTITUDE: {(-1*position[2]):.1f} m\nSPEED: {velocity[2]:.1f} m/s\n\nROLL: 0.0°\nPITCH: 0.0°\nYAW: 0.0°"

position = [0, 0, 0]
velocity = [6, 2, 7]
while True:
    rate(60)
    dt = 1/60
    position[0] += velocity[0] * dt
    position[1] += velocity[1] * dt
    position[2] += velocity[2] * dt
    update_visuals(position, velocity)
    