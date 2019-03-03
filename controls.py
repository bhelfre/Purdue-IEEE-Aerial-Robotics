def getControlParams(planeData, desHdg, desAlt, desVel):
#Replaces the function controlPlane.m
#   Contains the control algorithms for the aircraft's control surfaces.
#   Uses a PID system to continually adjust the throttle, ailerons, and
#   elevator.
## Setup
	currLoc = planeData[0:2] #lat, long, alt
	planeTelemetry = planeData[3:6] #speed, heading, pitch, roll
	#controlsData = planeData[7:9] #elevator, aileron, rudder
	currAlt = currLoc[2]
	currVel = planeTelemetry[0]
	currHdg = planeTelemetry[1]
	currPitch = planeTelemetry[2]
	currRoll = planeTelemetry[3]
	#currElevator = controlsData(1)
	#currAileron = controlsData(2)
	#currRudder = controlsData(3)

	throttle = getNewThrottle(desVel, currVel)
	elevator = getNewElevator(desAlt, currAlt, desPitch, currPitch)
	aileron = getNewAileron(desHdg, currHdg)
	rudder = getNewRudder()
	
def getNewThrottle(desVel, currVel):
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

def getNewElevator(desAlt, currAlt, currPitch):
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
	
def getNewAileron(desHdg, currHdg):
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
	
def getNewRudder():
	#Rudder is currently unused. Add code here to implement it.
	return 0
