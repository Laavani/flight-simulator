from vpython import *
# in powershell: python -m pip install -r reqs.txt

scene = canvas(title="6-DOF Flight Simulator")

plane = box(
    pos=vector(0, 0, 0),
    size=vector(6, 1.5, 1.5)
)

# Nose
nose = cone(
    pos=vector(3, 0, 0),
    axis=vector(2, 0, 0),
    radius=0.75
)

# Wings
left_wing = box(
    pos=vector(0, 0, 0),
    size=vector(2.5, 5, 0.2)
)

# Tail
tail = box(
    pos=vector(-2.3, 0, 0),
    size=vector(1, 2.5, 0.2)
)
while True:
    rate(60)