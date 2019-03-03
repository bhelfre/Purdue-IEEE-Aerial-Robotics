def getDist2D(initialLoc, finalLoc):
# Coordinates defined as coordinate(latitude, longitude, altitude)
#   NEED SUPPORT FOR ALTITUDE IN COORDINATE STRUCT (FLIGHTUTILITY.H)
#   Calculates lateral distance between two GPS coordinates in KM.
	## Set variables
	EARTH_MEAN_RADIUS = 6371 #in km
	phi1 = deg2rad(initialLoc[0])
	phi2 = deg2rad(finalLoc[0])
	deltaPhi = phi2 - phi1
	deltaLambda = deg2rad(finalLoc[1] - initialLoc[1])

	## Manipulate data
	a = sin(deltaPhi / 2) ^ 2 + cos(phi1) * cos(phi2) * \
		sin(deltaLambda / 2) ^ 2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))
	distance = EARTH_MEAN_RADIUS * c #Returns distance in KM
	return distance
	
def getDist3D(initialLoc, finalLoc):
	dist2D = getDist2D(initialLoc, finalLoc)
	altDiff = finalLoc[2] - initialLoc[2]
	return math.sqrt(dist2D ** 2 + altDiff ** 2)
	
def getHeading(initialLoc, finalLoc):
	# Coordinates defined as coordinate(latitude, longitude)
	## Set variables
	phi1 = deg2rad(initialLoc[1])
	phi2 = deg2rad(finalLoc[1])
	lambda1 = deg2rad(initialLoc[2])
	lambda2 = deg2rad(finalLoc[2])

	## Manipulate data
	deltaLambda = lambda2 - lambda1
	theta = atan2(sin(deltaLambda) * cos(phi2), (cos(phi1) * sin(phi2) - \
		sin(phi1) * cos(phi2) * cos(deltaLambda)))
	theta = rad2deg(theta)
	heading = mod(theta + 360.0, 360.0)
	return heading