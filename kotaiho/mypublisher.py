#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64

def talker():
	pub = rospy.Publisher('my_msg', Int64, queue_size=10)
	rospy.init_node('talker_node', anonymous=True)
	rate = rospy.Rate(10)
	count = 0
	
	while not rospy.is_shutdown():
		pub.publish(count)
		rospy.loginfo("==Pusblishing...")
		rate.sleep()
		count += 1

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass