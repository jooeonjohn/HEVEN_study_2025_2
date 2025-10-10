#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def talker():
    rospy.init_node('talker_node', anonymous=True)
    pub = rospy.Publisher('my_msg', Int32, queue_size=10)
    rate = rospy.Rate(10)  # 10Hz (원하면 조절 가능)
    n = 1                  # 1부터 시작
    while not rospy.is_shutdown():
        msg = Int32(data=n)
        pub.publish(msg)
        rospy.loginfo("==Publishing... %d", n)
        n += 1
        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
