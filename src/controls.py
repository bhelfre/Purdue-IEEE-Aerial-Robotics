def getControlParams(planeData, desState):
#Replaces the function controlPlane.m
#   Contains the control algorithms for the aircraft's control surfaces.
#   Uses a PID system to continually adjust the throttle, ailerons, and
#   elevator.
## Setup
	#planeData specified as: [lat, lon, alt, vel, hdg, pitch, roll, elev, ail, rud]
	desHdg = desState[0]
	desAlt = desState[1]
	desVel = desState[2]
	currAlt = planeData[2]
	currVel = planeData[3]
	currHdg = planeData[4]
	currPitch = planeData[5]
	currRoll = planeData[6]
	
	#print(currVel)
	#print(desVel)

	# Get new parameter values
	throttle = __getNewThrottle(desVel, currVel)
	elevator = __getNewElevator(desAlt, currAlt, currPitch)
	aileron = __getNewAileron(desHdg, currHdg, currRoll)
	rudder = __getNewRudder()
	return [throttle, elevator, aileron, rudder]
	
def __getNewThrottle(desVel, currVel):
	#Parameter definitions
	throttleGain_P = 0.5
	throttleGain_I = 1
	throttleGain_D = 0
	maxThrottle = 1
	
	#Calculations
	throttle = (desVel - currVel) * throttleGain_P
	if (throttle > maxThrottle):
		throttle = maxThrottle
	elif (throttle < 0):
		throttle = 0
	return throttle

def __getNewElevator(desAlt, currAlt, currPitch):
	#Parameter definitions
	maxPitch = 15
	elevatorGain_P = 0.05 #orig 0.05
	elevatorGain_I = 0
	elevatorGain_D = 0

	#Calculations
	desPitch = desAlt - currAlt
	if (desPitch > maxPitch):
		desPitch = maxPitch
	elif (desPitch < -maxPitch):
		desPitch = -maxPitch
	return (desPitch - currPitch) * elevatorGain_P
	
def __getNewAileron(desHdg, currHdg, currRoll):
	#Parameter definitions
	head2RollGain_P = 1.8 #orig 1.8
	head2RollGain_I = 0
	head2RollGain_D = 0
	maxRoll = 30
	aileronGain_P = 0.01
	aileronGain_I = 0
	aileronGain_D = 0

	#Calculations
	hdgChange = desHdg - currHdg
	head2Roll = hdgChange * head2RollGain_P

	if (head2Roll > maxRoll):
		head2Roll = maxRoll
	elif (head2Roll < -maxRoll):
		head2Roll = -maxRoll
	return (head2Roll - currRoll) * aileronGain_P
	
def __getNewRudder():
	#Rudder is currently unused. Add code here to implement it.
	return 0
