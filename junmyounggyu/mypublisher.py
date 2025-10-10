#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64
def talker():
	pub = rospy.Publisher('my_msg', Int64, queue_size=10)
	rospy.init_node('talker_node', anonymous=True)
	rate = rospy.Rate(10)
	
	count = 1

	while not rospy.is_shutdown():
		rospy.loginfo("Publishing: %d" % count) # 현재 보내는 숫자를 터미널에 출력
        
        # "hello world" 대신 count 변수를 발행
		pub.publish(count)

        # 다음 숫자를 위해 count를 1 증가
		count += 1
        
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass