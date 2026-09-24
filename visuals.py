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

def update_visuals(aircraft):
    scene.center = vector(aircraft.get_pos()[0], aircraft.get_pos()[1], aircraft.get_pos()[2]-500)
    plane.pos = vector(aircraft.get_pos()[0], aircraft.get_pos()[1], aircraft.get_pos()[2])
    hud.text = f"ALTITUDE: {(aircraft.get_pos()[2]):.1f} m\nVx: {aircraft.get_vel()[0]:.1f} m/s\nVy: {aircraft.get_vel()[1]:.1f} m/s\nVz: {aircraft.get_vel()[2]:.1f} m/s\n\nROLL: {aircraft.get_roll():.1f}°\nPITCH: {aircraft.get_pitch():.1f}°\nYAW: {aircraft.get_yaw():.1f}°"
    