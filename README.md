# Purdue-IEEE-Aerial-Robotics
Code base for the AUVSI-SUAS competition.

MATLAB -> PYTHON CONVERSION:

FUNCTION NAME CONVERSIONS:
	calcDist3D -> gcpDistance AND check for altitude within range (or create new function!)
	calcDist2D -> gcpDistance
	getHeading -> gcpHeading (this is NOT the same as querying X-Plane for the heading! It calculates the heading between two points.

GENERAL NOTES:
- Only need to calculate desiredHdg, desiredAlt, desiredVel
	- Use the above calculations to set elevator, aileron, throttle

MAKE CHANGES IN THE FOLLOWING FILES:
	getNewHeading
		- Don't need to calculate roll
		- Only need to calculate desiredHdg. Should be able to stop after line 33.
	getNewPitch
		- Stop after line 9, probably.
	
NO CONVERSION FOR THE FOLLOWING:
	updateACPos
	