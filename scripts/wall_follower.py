#!/usr/bin/env python3

import rospy

#import  message types
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist, Vector3

max_dist = 0.5 # maximum distance from wall
min_dist = 0.2

class FollowWall(object):

    def __init__(self):
        #initialize node, publisher and subscriber
        rospy.init_node("wall_follow")
        self.twist_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        rospy.Subscriber("/scan", LaserScan, self.process_scan)

        #set default Twist with all 0's
        lin = Vector3()
        ang = Vector3()
        self.twist = Twist(linear = lin, angular = ang)

    def process_scan(self, data):
        #find angle of closest distance that's not zero like with person follower
        closest = 1000
        closest_angle = 0
        for x in range(360):
            if data.ranges[x] <= closest and data.ranges[x] > 0:
                closest = data.ranges[x]
                closest_angle = x

        if closest <= max_dist and closest >= min_dist:
            # if closest distance is within set distance to robot,
            # use proportional control to get object to 90 degrees from robot
            if closest_angle > 180:
                closest_angle = closest_angle - 360 #convert angles past 180
            
            kp = 0         
            if (closest_angle-90 > 5) or (closest_angle-90) < -5: 
                # print("big angle")
                # use slower linear speed and turn at faster rate when change in angle large
                self.twist.linear.x = 0.08                
                kp = 0.9*0.017                
            else:
                # print("small angle")
                # use faster linear speed and turn slower when angle is pretty close to 90
                self.twist.linear.x = 0.15
                kp = 0.5*0.017   
            #set new angular velocity using proportional control and publish velocities
            new_ang = kp*(closest_angle-90) #subtract 90 b/c 90 degrees is ideal
            self.twist.angular.z = new_ang
            self.twist_pub.publish(self.twist)
        elif closest > (max_dist + 0.01) and closest != 1000: 
            # when robot is able to sense something but is not yet within following distance
            # implement person follower to keep moving closer to the object at a constant speed
            # print("moving towards wall")
            if closest_angle > 180:
                closest_angle = closest_angle - 360
                #print(closest_angle)
            new_ang =  1.2*.017*closest_angle
            self.twist.angular.z = new_ang
            self.twist.linear.x = 0.1 
            self.twist_pub.publish(self.twist)
        elif closest < min_dist:
            # when the robot gets too close to the wall, implements person follower to move back
            if closest_angle > 180:
                closest_angle = closest_angle - 360
            # print("too close to wall")
            new_ang =  1.2*.017*closest_angle
            new_lin = 0.5*(closest-min_dist) 
            self.twist.angular.z = new_ang
            self.twist.linear.x = new_lin
            self.twist_pub.publish(self.twist)
        else: 
            # when nothing is close robot moves straight
            # print("no wall")
            self.twist.linear.x = .2
            self.twist.angular.z = 0
            self.twist_pub.publish(self.twist)

    def run(self):
        # keep running
        rospy.spin()

if __name__ == '__main__':
    # initialize and run node
    node = FollowWall()
    node.run()   