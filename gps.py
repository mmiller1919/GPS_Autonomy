from os import popen
from time import sleep
from bsmLib.networking import tcpServer
t = tcpServer()
t.listen()

class GPS:
    def __init__ (self, device = "/dev/serial0"):
        self.device = device
        self.rawReading = ""

    def msgUpdate(self):
        self.rawReading = popen("cat " + self.device).read()

    def read(self):
        self.msgUpdate()
	return self.rawReading

if __name__ == "__main__":
    g = GPS()
    r = g.read()
    sleep(1)
    print r
    t.send(r)
