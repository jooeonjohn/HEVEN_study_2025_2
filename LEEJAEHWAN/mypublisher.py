#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32   # String → Int32

def talker():
    pub = rospy.Publisher('my_msg', Int32, queue_size=10)   # 토픽 타입 변경
    rospy.init_node('talker_node', anonymous=True)
    rate = rospy.Rate(1)    # 1Hz (1초에 1번씩 증가된 값 publish)

    num = 1
    while not rospy.is_shutdown():
        pub.publish(num)
        rospy.loginfo("Publishing: %d", num)
        num += 1   # 값 증가
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
