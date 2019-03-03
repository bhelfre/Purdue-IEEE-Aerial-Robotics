import math
import numpy as np


# fpStruct = struct.pack('north', 'east', 'alt', 'vel', 'cylN', 'cylE', 'cylR', 'leg', 'maxGs', 'rph', 'successRadius', 'avoidanceDist', 'avoiding');
fpDict = {
	"north" = [ 0, 148, 150,  0],
	"east" = [ 0,   -15, 140,  0],
	"alt" = [ 0,   0,   0,  0],
	"vel" = [20,  20,  20, 20],
	"cylN" = [-5,  10, 100,  60, 50],
	"cylE" = [40, 135, 100, 160, 68],
	"cylR" = [ 5,  15,  10,  10, 10],
	"leg" = 2,
	"maxGs" = 50,
	"rph" = [0,0,0],
	"successRadius" = 5,
	"avoidanceDist" = 10,
	"avoiding" = 0,
	"wayp" = makeWaypoints(fpDict),    #<- cautionary line #
	"avoidances" = makeAvoidances(fpDict),  #<- cautionary line #
	"avoidance" = [],
	"desWayp" = fp.wayp(fp.leg, :)   #<- need to find equivalent to searching within same column as fp.leg #
}

timeDelta = 0.05;	#Time change between consecutive data samples (s)
maxSimTime = 60;	#Maximum simulation time (s)
iter = 2;

#Generate Simulation variables
maxIterations = math.ceil(maxSimTime / timeDelta);

Matrix = [[0 for x in range(max)] for y in range (10)]
data = np.ones([maxIterations, 10]); # should generate matrix (double check) #

data = [0, "fpDict['leg']", "fpDict['vel[fpDict['leg']]']", "fpDict['rph']", "fpDict[fpDict['wayp(1, :)']", 0];  #dependency on cautionary line! #
currState = data[iter - 1][range(3,6)];
currLoc = data[iter -1][range(7,9)];
#Simulation Execution
for currTime in range(timeDelta, maxSimTime, timeDelta):
	# Determine if desired waypoint has been reached
	if getDist3D(currLoc, fpDict['desWayp']) <= fpDict['successRadius']:
	  # Update flight leg
	  fpDict['leg'] = fpDict['leg'] + 1;
	  
	  # Exit if all waypoints have been reached
	  if fp['leg'] > len(fpDict['wayp']):
		break
	  fp['desWayp'] = fp['wayp'][fpDict['leg']][:];
	
	# Handle avoidance state machine
	fpDict['avoidance'] = getNearbyAvoidance(fpDict, currLoc, currState);
	if not fp['avoidance']:
		if fpDict['avoidance'] != 0:
			fpDict['avoiding'] = 1;
		else if fpDict['avoiding'] == 1:
			fpDict['avoiding'] = 2;
		else if (abs(getHeading(currLoc, fpDict['desWayp'] - currState[4]))) <= 0.0001:
			fpDict['avoiding'] = fpDict['avoiding'] + 1;
	else:
		if fpDict['avoiding'] > 0:
			if (abs(getHeading(currLoc, fpDict['desWayp'] - currState[4]))) <=0.0001:
				fpDict['avoiding'] = fpDict['avoiding'] + 1;
			if fpDict['avoiding'] >= 10:
				fpDict['avoiding'] = 0;
		else:
			fpDict['avoiding'] = 0;

	# Calculate the aircarft's new state
	[currState, currLoc] = getNewACState(fpDict, [timeDelta, maxSimTime], currState, currLoc);

	# Add current position information to flight data array
	data[iter][:] = [currTime, fpDict['leg'], currState, currLoc, fpDict['avoiding']];
	iter = iter + 1;
