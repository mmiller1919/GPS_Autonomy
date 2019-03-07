import bsmLib.RPL as RPL
from bsmLib.vector import vector
import server as s
from time import sleep
from bsmLib import tcpServer

vec0 = s.c_read()

lat = raw_input("Latuitude: ")
long = raw_input("Longitude: ")

vec1 = vector(lat, long)

L = 0
R = 1


def f_distance(vec0, vec1):
    d = math.sqrt( ((vec0.x-vec1.x)**2)+((vec0.y-vec1.y)**2) )
    return d

def drive_forward():
    distance = 0
    while True:
        vec0 = s.c_read()
        distance = f_distance(vec0, vec1)
        if distance > 20:
            RPL.servoWrite(L, 2000)
            RPL.servoWrite(R, 1000)
        elif distance < 20:
            RPL.servoWrite(L, 0)
            RPL.servoWrite(R, 0)
        else:
            print("KYS")
            exit()

if __name__ == "__main__"
    drive_forward()
