import bsmLib
from bsmLib import tcpServer
from bsmLib import vector

t = tcpServer(port = '10002')
t.listen()

vec = vector()

def c_read():
    coords = t.recv()

    start = coords.find( '(' )
    end = coords.find( ')' )

    if start != -1 and end != -1:
        result = coords[start+1:end]

    lat, long = result.split

    vec.set(lat, long)
    return vec

if __name__ = "__main__":
    while(1):
        print(c_read())
