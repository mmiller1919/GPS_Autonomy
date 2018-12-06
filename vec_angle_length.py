import bsmLib.RPL as RPL
from vec_angle import vec_angle 
from bsmLib.vector import vector
import time
from math import pi
from gps import GPS

g = GPS()
r = g.read()
#r = '$GPRMC,154633.000,A,4457.4413,N,09320.5487,W,0.19,0.07,011118,,,A*7B'

def data_transfer():
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
    
    return lat, lon

def data_read():
    start = c.find("44")
    end = c.find("',", start)  
    lat = float(c[start:end])
    rlat =  lat - 4400
    trlat = rlat / 60
    latA =  trlat + 44


    start2 = c.find("93")
    end2 = c.find("')", start)
    long = float(c[start2:end2])
    rlong = long - 9300
    trlong = rlong / 60
    longA =  0 - (trlong + 93)

RPL.init() 

motorL = 0
motorR = 1
#2000 for right 1000 for left
latB = int(raw_input("Latitude > "))
longB = int(raw_input("Longitude > "))

def vec_trans_angle(x):
	TurnTime = abs(x) / 20
	#vectors are read in distances of 15.24 cm per unit
	if x > 0:
		move = time.time()
		#turns left
 		while time.time() < (move + TurnTime):
	  		RPL.servoWrite(motorL, 0)
			RPL.servoWrite(motorR, 2000)
		if time.time() > (move + TurnTime):
    			RPL.servoWrite(motorL, 0)
    			RPL.servoWrite(motorR, 0)
			
	
	if x < 0: 
		move2 = time.time()
		#turns right
		while time.time() < (move2 + TurnTime):
	  		RPL.servoWrite(motorL, 1000)
			RPL.servoWrite(motorR, 0)
		if time.time() > (move2 + TurnTime):
    			RPL.servoWrite(motorL, 0)
    			RPL.servoWrite(motorR, 0)
			

def vec_length(x1,y1):
  	v = vector(x1, y1) 
  	length = v.mag()
  	return length

def vec_trans_length(magnitude):
  #robot goes 13.3 cm in 1 second
  	Length = abs(magnitude) * 15.24
  	Runtime = Length / 12.3
  	move3 = time.time()
 	while time.time() < (move3 + Runtime):
    		RPL.servoWrite(motorL, 2000)
		RPL.servoWrite(motorR, 1000)
  	if time.time() > (move3 + Runtime):
    		RPL.servoWrite(motorL, 0)
    		RPL.servoWrite(motorR, 0)
		
	
def vec_combined(x1,y1,x2,y2):
	vec_trans_angle(vec_angle(x1,y1,x2,y2))
	vec_trans_length(vec_length(x2,y2))
	
vec_combined(Numberx1, Numbery1, Numberx2, Numbery2)
