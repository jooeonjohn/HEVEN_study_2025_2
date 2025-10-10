#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def callback(msg):
    rospy.loginfo(f"Received: {msg.data}")

def listener():
    rospy.init_node('listener_node', anonymous=True)
    rospy.Subscriber('my_msg', Int32, callback)
    rospy.spin()  # 노드가 종료될 때까지 대기

if __name__ == '__main__':
    listener()

