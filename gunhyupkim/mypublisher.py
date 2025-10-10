#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def talker():
    pub = rospy.Publisher('my_int', Int32, queue_size=10)
    rospy.init_node('int_talker', anonymous=True)
    rate = rospy.Rate(1)  # 1Hz = 1초마다 한 번씩 발행
    num = 1

    while not rospy.is_shutdown():
        rospy.loginfo(f"Publishing: {num}")
        pub.publish(num)
        num += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
