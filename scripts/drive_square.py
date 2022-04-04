#!/usr/bin/env python3

import rospy
import math
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

class Square(object):
    """ This node publishes ROS messages containing the 3D coordinates of a single point """
    
    def __init__(self):
        rospy.init_node('velocity')
        self.twist_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)


    def run(self):

        my_linear_velocity = Vector3(0.5,0,0)
        my_angular_velocity = Vector3(0,0,0)
        straight = Twist(linear = my_linear_velocity, angular = my_angular_velocity)
        
        my_linear_velocity2 = Vector3(0,0,0)
        my_angular_velocity2 = Vector3(0,0,math.pi/4)
        turn = Twist(linear = my_linear_velocity2, angular = my_angular_velocity2)      

        r = rospy.Rate(2)

    

        while not rospy.is_shutdown():
                for i in range(6):
                    self.twist_pub.publish(straight)
                    r.sleep()
                for i in range(4): # 4 / 2 Hz * 45 deg per s = 90 deg total
                    self.twist_pub.publish(turn)
                    r.sleep()   


if __name__ == '__main__':
    node = Square()
    node.run()
    rospy.spin()