def gcpHeading(initialLoc, finalLoc):
# Coordinates defined as coordinate(latitude, longitude)
#   NEED SUPPORT FOR ALTITUDE IN COORDINATE STRUCT (FLIGHTUTILITY.H)
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