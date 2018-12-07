from bsmLib.vector import vector
from math import pi


def rad_deg(x):
    y = 180 * x / pi
    return y

def vec_angle(x1, y1, x2, y2):
    x = vector(x1, y1)
    y = vector(x2, y2)

    one = x.heading()
    two = y.heading()

    final = two - one
    angle_between = rad_deg(final)
    print angle_between
    return angle_between
