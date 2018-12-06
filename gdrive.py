from bsmLib.vector import vector
from math import pi

f = open('gData.txt', 'r')
c  = f.read()
f.close()

start = c.find("44")
end = c.find("',", start)
lat = float( c[start:end])
rlat =  lat-4400
trlat = rlat / 60
latitude =  trlat + 44


start2 = c.find("93")
end2 = c.find("')", start)
long = float(c[start2:end2])
rlong = long - 9300
trlong = rlong / 60
longitude =  0 - ( trlong + 93)

