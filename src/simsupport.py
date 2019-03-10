import numpy as np

def getPlaneData(client):
	# Read data from client
	positionData = client.getPOSI() #Ranges from 1-7
	controlData = client.getCTRL()  #Ranges from 1-7
	airspeed = client.getDREF("sim/flightmodel/position/indicated_airspeed2")[0]

	# Unpack data
	latitude = positionData[0]
	longitude = positionData[1]
	altitude = positionData[2] * 3.28084 #Returns altitude in FEET
	pitch = positionData[3]
	roll = positionData[4]
	heading = positionData[5]
	elevator = controlData[0]
	aileron = controlData[1]
	rudder = controlData[2]

	return [latitude, longitude, altitude, airspeed, heading, pitch, \
		roll, elevator, aileron, rudder]
		
def makeWaypoints(fp):
	stacked = np.stack((fp['lat'], fp['lon'], fp['alt'], fp['vel']))
	return np.transpose(stacked).tolist()
	
def makeAvoidances(fp):
	stacked = np.stack((fp['cylLat'], fp['cylLon'], fp['cylR']))
	return np.transpose(stacked).tolist()