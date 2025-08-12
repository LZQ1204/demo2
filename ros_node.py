#!/usr/bin/env python3
"""一个简单的ROS节点，用于发布问候消息。"""

import rospy
from std_msgs.msg import String

def main() -> None:
    """初始化ROS节点并周期性发布问候。"""
    rospy.init_node("greeting_node")
    publisher = rospy.Publisher("greetings", String, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz
    while not rospy.is_shutdown():
        message = String()
        message.data = "Hello from ROS!"
        publisher.publish(message)
        rate.sleep()


if __name__ == "__main__":
    main()
