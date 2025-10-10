#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def callback(msg):
    rospy.loginfo(f"Received: {msg.data}")

def listener():
    rospy.init_node('int_listener', anonymous=True)
    rospy.Subscriber('my_int', Int32, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
