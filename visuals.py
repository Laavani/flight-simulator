from vpython import *
# in powershell: python -m pip install -r reqs.txt

scene = canvas(title="6-DOF Flight Simulator")
plane = box( pos=vector(0, 0, 0), size=vector(3, 1, 1))

while True:
    rate(60)
    plane.pos.x += 0.1