from bsmLib.networking import tcpClient
t = tcpClient("192.168.21.153")
t.connect()

while(1):
    data = t.recv()
    data = data.split(",")
    x = int(data[0])
    y = int(data[1])
    print(x, y)
