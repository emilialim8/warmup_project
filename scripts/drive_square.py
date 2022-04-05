#!/usr/bin/env python3

import rospy
import math #to use pi for radians

from geometry_msgs.msg import Twist #type for overall velocity
from geometry_msgs.msg import Vector3 #type for angular and linear velocity

class Square(object):
    """ This node goes in a square """
    
    def __init__(self):
        #starts node
        rospy.init_node('velocity')
        # sets up node as publisher to the /cmd_vel topic to change velocity
        self.twist_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)


    def run(self):
        #setup straight velocity
        my_linear_velocity = Vector3(0.5,0,0)
        my_angular_velocity = Vector3(0,0,0)
        straight = Twist(linear = my_linear_velocity, angular = my_angular_velocity)
        
        #setup turning velocity
        my_linear_velocity2 = Vector3(0,0,0)
        # will turn for 2 s, so turn 45 deg per s or pi/4 rad
        my_angular_velocity2 = Vector3(0,0,math.pi/4)
        turn = Twist(linear = my_linear_velocity2, angular = my_angular_velocity2)      

        #sets the rate of publishing as 2 Hz, 2 times per second
        r = rospy.Rate(2) 

        while not rospy.is_shutdown(): #continues as long as not shutdown
                for i in range(6): #goes straight for 3 seconds (6 messages at 2 Hz)
                    self.twist_pub.publish(straight)
                    r.sleep()
                for i in range(4): #turns for 2 seconds (4 messages at 2 Hz) 
                    self.twist_pub.publish(turn)
                    r.sleep()   


if __name__ == '__main__':
    #declares node and runs
    node = Square()
    node.run()
    rospy.spin()