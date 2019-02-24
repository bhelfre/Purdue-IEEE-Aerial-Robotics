def gcpDistance(initialLoc, finalLoc):
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