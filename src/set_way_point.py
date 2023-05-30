#!/usr/bin/env python3

import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

global waypoint
global theta
global e
global u

waypoint = [7, 7]

def subscribe_pose():
	global turtlePose
	turtlePose=None
	rospy.init_node('set_way_point', anonymous=False)
	pub=rospy.Publisher("cmd_vel",Twist,queue_size=1)
	rate=rospy.Rate(30)
	rospy.Subscriber("pose",Pose,getPose)

	kp = rospy.get_param('~kp',2.5)

	while not rospy.is_shutdown():
		message=Twist()
		if turtlePose is not None:
			theta=math.atan2( waypoint[1]-turtlePose.y,waypoint[0]-turtlePose.x)
			e= math.atan(math.tan(theta-turtlePose.theta)/2)
			u= kp* e

			message.angular.z = u
			pub.publish(message)
		rate.sleep()

def getPose(pose):
	global turtlePose
	turtlePose=pose

if __name__=="__main__":

	try:
		subscribe_pose()
	except rospy.ROSInterruptException:
		pass
