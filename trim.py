import time
from time import sleep
from gps import GPS
from scipy import stats
a = []
o = []

g = GPS()
r = g.read()

move = time.time()

while move < (time.time() + 20):
    start = r.find('$GPRMC')
    end = r.find(',0.', start)
    log = r[start:end]

    start2 = log.find('A')
    end2 = log.find('W', start2)
    log2 = log[start2:end2]

    start3 = log2.find('44')
    end3 = log2.find(',N', start3)
    lat = log2[start3:end3]

    start4 = log2.find('09')
    end4 = log2.find(',W,', start4)
    lon = log2[start4:end4]

    a.append(lat)
    o.append(lon)

print a
print o
