import math

def getDist2D(initialLoc, finalLoc):
# Coordinates defined as coordinate(latitude, longitude, altitude)
#   NEED SUPPORT FOR ALTITUDE IN COORDINATE STRUCT (FLIGHTUTILITY.H)
#   Calculates lateral distance between two GPS coordinates in KM.
	## Set variables
	EARTH_MEAN_RADIUS = 6371 #in km
	phi1 = math.radians(initialLoc[0])
	phi2 = math.radians(finalLoc[0])
	deltaPhi = phi2 - phi1
	deltaLambda = math.radians(finalLoc[1] - initialLoc[1])

	## Manipulate data
	a = math.sin(deltaPhi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * \
		math.sin(deltaLambda / 2) ** 2
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
	distance = EARTH_MEAN_RADIUS * c #Returns distance in KM
	return distance
	
def getDist3D(initialLoc, finalLoc):
	dist2D = getDist2D(initialLoc, finalLoc)
	altDiff = finalLoc[2] - initialLoc[2]
	return math.sqrt(dist2D ** 2 + altDiff ** 2)
	
def getHeading(initialLoc, finalLoc):
	# Coordinates defined as coordinate(latitude, longitude)
	## Set variables
	phi1 = math.radians(initialLoc[0])
	phi2 = math.radians(finalLoc[0])
	lambda1 = math.radians(initialLoc[1])
	lambda2 = math.radians(finalLoc[1])

	## Manipulate data
	deltaLambda = lambda2 - lambda1
	theta = math.atan2(math.sin(deltaLambda) * math.cos(phi2), \
		(math.cos(phi1) * math.sin(phi2) - math.sin(phi1) * math.cos(phi2) * \
		math.cos(deltaLambda)))
	theta = math.degrees(theta)
	heading = (theta + 360.0) % 360.0
	return heading
	
def getDesiredState(planeData, desWayp):
	desAlt = desWayp[2]
	desVel = desWayp[3]
	desHdg = getHeading(planeData[0:3], desWayp)
	return [desHdg, desAlt, desVel] 