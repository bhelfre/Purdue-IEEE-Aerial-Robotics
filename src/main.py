import xpc
import math
import simsupport
import controls as ctrl
import flightmath as fm
import numpy as np

def runSimulation():
	with xpc.XPlaneConnect() as client:
			
		fp = { 				##### STRUCTURE CONTAINING ALL FLIGHT PATH DATA #####
			'lat'    : [ 0, 148, 150,   0], #Waypoint latitude (decimal degrees)
			'lon'    : [ 0, -15, 140,   0], #Waypoint longitude (decimal degrees)
			'alt'    : [ 0,   0,   0,   0], #Waypoint altitude (m)
			'vel'    : [20,  20,  20,  20], #Desired velocity at each waypoint (knots)
			'cylLat' : [-5,  10, 100,  60, 50], #Latitude of avoidance cylinder (dec deg)
			'cylLon' : [40, 135, 100, 160, 68], #Longitude of avoidance cylinder (dec deg)
			'cylR'   : [ 5,  15,  10,  10, 10], #Radius of avoidance cylinder (m)
			'leg'    :  1, #Current leg of flight, allows for indexing of current waypoint
			'maxGs'  : 50, #Maximum number of G's allowed on turns
			'rph'    : [0, 0, 0],  #Initial aircraft roll, pitch, and heading (deg)
			'successRadius' :  5, #Distance from waypoint to "reach" it (m)
			'avoidanceDist' : 10, #Minimum distance aircraft can be from each avoidance (m)
			'avoiding'      :  0, #State variable to assist with obstacle avoidance
			'avoidance'     : [],
		}
		
		#Append internal data to dictionary
		fp['wayp'] = simsupport.makeWaypoints(fp)
		fp['avoidances'] = simsupport.makeAvoidances(fp)
		fp['desWayp'] = fp['wayp'][fp['leg']]

		#Define simulation variables
		maxSimTime = 60	#Maximum simulation time (s)
		initialTime = client.getDREF("sim/time/local_time_sec")[0];
		currTime = initialTime
		planeData = simsupport.getPlaneData(client)
		currLoc = planeData[0:2]
		#data = [0, "fp['leg']", "fp['vel[fp['leg']]']", "fp['rph']", "fp[fp['wayp(1, :)']", 0];  #dependency on cautionary line! #
		
		# Simulation execution
		while currTime <= initialTime + maxSimTime:
		
			# Get the plane's current state
			planeData = simsupport.getPlaneData(client)
			currLoc = planeData[0:3]
			
			#print(planeData)
			
			# Update control surface parameters based on plane's current state
			desState = fm.getDesiredState(planeData, fp['desWayp'])
			controlParams = ctrl.getControlParams(planeData, desState)
			client.sendCTRL(controlParams + [-998, -998, -998])
			
			'''
			# Handle avoidance state machine
			fp['avoidance'] = getNearbyAvoidance(fp, currLoc, currState);
			if not fp['avoidance']:
				if fp['avoidance'] != 0:
					fp['avoiding'] = 1;
				else if fp['avoiding'] == 1:
					fp['avoiding'] = 2; #Required to prevent cutting through avoidances because plane faces next wayp by default
				else if (abs(getHeading(currLoc, fp['desWayp'] - currState[4]))) <= 0.0001:
					fp['avoiding'] = fp['avoiding'] + 1;
			else:
				if fp['avoiding'] > 0:
					if (abs(getHeading(currLoc, fp['desWayp'] - currState[4]))) <=0.0001:
						fp['avoiding'] = fp['avoiding'] + 1;
					if fp['avoiding'] >= 10:
						fp['avoiding'] = 0;
				else:
					fp['avoiding'] = 0;
			'''
			
			# Determine if desired waypoint has been reached
			if fm.getDist3D(currLoc, fp['desWayp']) <= fp['successRadius']:
				# Update flight leg
				fp['leg'] = fp['leg'] + 1;

				# Exit if all waypoints have been reached
				if fp['leg'] > len(fp['wayp']) - 1:
					break
					
				# Update waypoint
				fp['desWayp'] = fp['wayp'][fp['leg']][:];

			# Add current position information to flight data array
			#data[iter][:] = [currTime, fp['leg'], currState, currLoc, fp['avoiding']];
			#iter = iter + 1;
			currTime = client.getDREF("sim/time/local_time_sec")[0];
	
	
	
if __name__ == "__main__":
	runSimulation()
	'''with xpc.XPlaneConnect() as client:
		# Verify connection
		try:
			# If X-Plane does not respond to the request, a timeout error
			# will be raised.
			client.getDREF("sim/test/test_float")
			
		except:
			print "Error establishing connection to X-Plane."
			print "Exiting..."
			'''
		