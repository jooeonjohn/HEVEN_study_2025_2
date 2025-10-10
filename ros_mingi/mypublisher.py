#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def talker(): #함수 정의 
	pub = rospy.Publisher('my_msg', Int32, queue_size=10)
	 # rospy 라이브러리 이용 my_msg라는 토픽을 스트링 형식으로 퍼블리셔
	rospy.init_node('talker_node', anonymous=True)
	rate = rospy.Rate(10) #10Hz로 정보 송신 10/s 
	
	i=0
		

	while not rospy.is_shutdown():
		i=i+1
		hello_str = i
		pub.publish(hello_str)
		rospy.loginfo("==Pusblishing...")
		rate.sleep() #발행주기 맞춰줌

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
