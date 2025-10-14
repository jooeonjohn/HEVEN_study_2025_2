#!/usr/bin/env python3
import rospy
# Int32 메시지 타입 사용으로 변경
from std_msgs.msg import Int32

def callback(data):
    # 수신된 정수(data.data)를 출력 포맷(%d)에 맞게 출력
    rospy.loginfo("%d" % data.data)

def listener():
    rospy.init_node('listener_node', anonymous=True)
    # 토픽의 메시지 타입을 Int32로 변경하여 구독
    sub=rospy.Subscriber("my_msg", Int32, callback)
    rospy.spin()

if __name__ == "__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
