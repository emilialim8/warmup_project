#!/usr/bin/env python3

import rospy

# import message types
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist, Vector3

dist = 0.3 #ideal following distance

class FollowPerson(object):

    def __init__(self):
        #initialize node 
        rospy.init_node("follow")
        #create publisher and subscriber
        self.twist_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        rospy.Subscriber("/scan", LaserScan, self.process_scan)

        #set default Twist with all 0's
        lin = Vector3()
        ang = Vector3()
        self.twist = Twist(linear = lin, angular = ang)

    def process_scan(self, data):
        #initialize with high number, greater than any possible distance reading
        closest = 1000
        closest_angle = 0
        for x in range(360): #check all data values
            if data.ranges[x] <= closest and data.ranges[x] > 0:
                #save lowest non-zero distance and its corresponding angle
                closest = data.ranges[x]
                closest_angle = x
        if closest != 1000: #checks that something was sensed
            if closest_angle > 180:
                #turns values greater than 180 into a negative angle
                closest_angle = closest_angle - 360
            #set constants for proportional control
            kp1 = 1.2*0.017 
            kp2 = 0.5
            new_ang = kp1*(closest_angle) #proportional control for angle
            #ideal angle is 0 so don't need to substract anything
            new_lin = kp2*(closest-dist) #proportional control for distance
            #ideal distance is following distance

            #set new velocities and publish
            self.twist.linear.x = new_lin
            self.twist.angular.z = new_ang
            self.twist_pub.publish(self.twist)
   
    def run(self):
        #keep running
        rospy.spin()

if __name__ == '__main__':
    #initialize and run node
    node = FollowPerson()
    node.run()   