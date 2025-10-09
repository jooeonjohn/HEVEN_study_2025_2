#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def callback(msg: Int32):
    rospy.loginfo("I heard, %d", msg.data)

    def listener():
        rospy.init_node('listener_node', anonymous=True)
        sub = rospy.Subscriber('my_msg', Int32, callback)
        rospy.spin()

if __name__ == "__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass

