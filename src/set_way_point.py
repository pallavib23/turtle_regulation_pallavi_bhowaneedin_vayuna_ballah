#!/usr/bin/env python3

import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_msgs.msg import Bool

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
	is_moving_pub = rospy.Publisher("is_moving", Bool, queue_size=1)
	rate=rospy.Rate(30)
	rospy.Subscriber("pose",Pose,getPose)

	kp = rospy.get_param('~kp',2.5)
	kpl = rospy.get_param('~kpl', 1.0)
	distance_tolerance = rospy.get_param ('~distance_tolerance', 0.1)

	while not rospy.is_shutdown():
		message=Twist()
		is_moving_msg = Bool()
		if turtlePose is not None:
			theta=math.atan2(waypoint[1]-turtlePose.y, waypoint[0]-turtlePose.x)
			e= math.atan(math.tan(theta-turtlePose.theta)/2)
			u= kp * e

			message.angular.z = u

			distance = calculate_distance(waypoint[0], waypoint[1], turtlePose.x, turtlePose.y)
			print("Distance:", distance)

			if distance > distance_tolerance:
				v = kpl * distance
				message.linear.x = v

				is_moving_msg.data = True
			else:
				is_moving_msg.data = False

			pub.publish(message)
			is_moving_pub.publish(is_moving_msg)
			rate.sleep()

def getPose(pose):
	global turtlePose
	turtlePose=pose

def calculate_distance(xA, yA, xB, yB):
	return math.sqrt((yB - yA)**2 + (xB - xA)**2)


if __name__=="__main__":
	try:
		subscribe_pose()
	except rospy.ROSInterruptException:
		pass

