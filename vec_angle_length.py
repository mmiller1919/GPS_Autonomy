import bsmLib.RPL as RPL
from vec_angle import vec_angle 
from bsmLib.vector import vector
import time
from math import pi
from gps import GPS

t = tcpClient("192.168.21.153")
t.connect()
data = t.recv()
r = float(data)

#data = data.split(",")
#x = int(data[0])
#y = int(data[1])
#print(x, y)
#g = GPS()
#r = g.read()
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
   
    	start5 = lat.find("44")
    	end5 = lat.find("',", start)  
    	tlat = float(c[start:end])
	rlat =  tlat - 4400
    	trlat = rlat / 60
    	latA =  trlat + 44

    	start6 = lon.find("93")
    	end6 = lon.find("')", start)
    	long = float(c[start2:end2])
    	rlong = long - 9300
    	trlong = rlong / 60
    	longA =  0 - (trlong + 93)
    	
	return latA, longA

coords_a = data_transfer()
coords = coords_a.split(",")
latA = int(coords[0])
longA = int(coords[1])
RPL.init() 

ml = 0
mr = 1
#2000 for right 1000 for left
latB = float(raw_input("Latitude > "))
longB = float(raw_input("Longitude > "))

go = time.time() + 3
while time.time() < (go):
    	RPL.servoWrite(ml, 1000)
    	RPL.servoWrite(mr, 2000)
if time.time() > (go):
    	RPL.servoWrite(ml, 0)
    	RPL.servoWrite(mr, 0)

	

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
			

def vec_length(latA,longA):
    	v = vector(latA,longA) 
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
		
	
def vec_combined(latA,longA,latB,longB):
    	vec_trans_angle(vec_angle(latA,longA,latB,longB))
    	vec_trans_length(vec_length(latB,longB))
	
vec_combined(Numberx1, Numbery1, Numberx2, Numbery2)
