from bsmLib import tcpClient
from bsmLib import vector
from GPS_Data import GPS

def average(r):
    s0 = 0
    s1 = 0
    for i in range(r):
        s0 += r[i].x
        s1 += r[i].y
    s0 = s0 / len(r)
    s1 = s1 / len(r)
    v = vector(s0, s1)
    return v


g = GPS()

tcpClient(host = '192.168.21.153', port = '10002')
t = tcpClient()
t.connect()

while(1):
    data = 0
    r = []
    for i in range(10):
        cord = g.read()
        r.append(cord)
    data = average(r)

    t.send(str(data))
