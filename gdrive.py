from bsmLib.vector import vector
from math import pi

f = open('gData.txt', 'r')
c  = f.read()
f.close()

start = c.find("44")
end = c.find("',", start)
lat = c[start:end]
print lat

start2 = c.find("09")
end2 = c.find("')", start)
long = c[start2:end2]
print long

