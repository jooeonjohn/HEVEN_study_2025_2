#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32   # 🔸 String → Int32 로 변경

def talker():
    pub = rospy.Publisher('my_msg', Int32, queue_size=10)
    rospy.init_node('talker_node', anonymous=True)
    rate = rospy.Rate(1)  # 1Hz, 1초에 한 번씩 발행

    num = 1  # 1부터 시작
    while not rospy.is_shutdown():
        pub.publish(num)
        rospy.loginfo(f"Publishing: {num}")
        num += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

