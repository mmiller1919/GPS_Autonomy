from time import sleep
from gps import GPS
g = GPS()
#r = g.read()
r = '$GPRMC,154633.000,A,4457.4413,N,09320.5487,W,0.19,0.07,011118,,,A*7B'

while True:
    sleep(2)

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

    f = open('gData.txt', 'w')
    coords = lat, lon
    f.write(str(coords))
    f.close() 
