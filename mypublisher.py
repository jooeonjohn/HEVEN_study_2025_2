#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def talker():
    rospy.init_node('mynode', anonymous=True)
    pub = rospy.Publisher('chatter', Int32, queue_size=10)
    rate = rospy.Rate(1) # 1hz
    count = 1

    while not rospy.is_shutdown():
        rospy.loginfo("Publishing %d", count)
        pub.publish(count)
        count += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

