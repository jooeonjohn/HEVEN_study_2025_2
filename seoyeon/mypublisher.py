#!/usr/bin/env python3
import rospy
# String 대신 Int32 메시지 타입을 사용합니다.
from std_msgs.msg import Int32

def talker():
    # 토픽의 메시지 타입을 Int32로 변경합니다.
    pub = rospy.Publisher('my_msg', Int32, queue_size=10)
    rospy.init_node('talker_node', anonymous=True)
    rate = rospy.Rate(10)

    # 1부터 시작하는 정수 카운터 변수를 설정합니다.
    count = 1

    while not rospy.is_shutdown():
        # Int32 타입 메시지 객체를 만들고 .data에 정수 값 할당
        int_msg = Int32()
        int_msg.data = count
        
        rospy.loginfo("Publishing: %d" % int_msg.data)
        
        # 메시지 발행
        pub.publish(int_msg)
        
        # 정수 카운터 1 증가
        count += 1
        
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
