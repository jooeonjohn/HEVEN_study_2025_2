#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64

def callback(data):
        rospy.loginfo("I heard, %d", data.data)
        
def listner():
    sub = rospy.Subscriber("my_msg", Int64, callback)
    rospy.init_node('listener_node', anonymous=True)
    rospy.spin()
    
if __name__ == "__main__":
    try:
        listner()
    except rospy.ROSInterruptException:
        pass