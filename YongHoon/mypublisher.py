#!/usr/bin/env python3

import rospy
# from std_msgs.msg import String
from std_msgs.msg import Int32


def talker():
	pub = rospy.Publisher('my_num', Int32, queue_size=10)
	rospy.init_node('talker_node', anonymous=True)
	rate = rospy.Rate(10)
	num=1
	while not rospy.is_shutdown():
		pub.publish(num)
		rospy.loginfo("==Pusblishing...")
		rate.sleep()
		num+=1

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass