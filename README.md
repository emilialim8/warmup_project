# warmup_project
## Drive in a square
This code allows the robot to drive in a square. The robot first goes straight for approximately 0.4 m and then turn 90 degrees. It repeats this behavior until it completes a square and (theoretically) returns to its starting position. To accomplish this, the robot moves forward with a linear velocity of 0. for 2 seconds. Then I set the linear velocity to 0 and the angular velocity to 45 degrees per second. The robot then rotates for 2 seconds, resulting in a 90 degree turn.

In the initialization function, I subscribe to the /cmd_vel topic. In the run function, I set two possible velocity values that allow the robot to either turn or go straight. Then in a while loop, I have the robot alternate between going straight and turning. The proper velocity is published at a rate of 2 Hz and is published 4 times before switching, resulting in 2 seconds of each behavior.

![drive square](https://github.com/emilialim8/warmup_project/blob/35d1fb89f1d5442e35d7a84669f45e443c43f45e/drive_square.gif)


## Person Follower
The goal of this code is to have the robot follow a person. To implement this, I found the angle of the object closest to the robot. Using proportional control, I had the robot move to face towards the closest object and also slow down as it got closer. 

In the initialization function, I subscribed to the scanner topic in order to process the laser scanner data and set up a publisher for velocity topic in order to set velocities. To process the scanning data, I looped through all of the angles to find the angle that had the closest object to it, not including any zeros as they likely represent the scanner not sensing any object. After converting angles over 180 to the proper direction, I used proportional control for the angular velocity with an ideal angle of 0 and proportional control for the linear velocity with an ideal distance of 0.3. 

![person follower](https://github.com/emilialim8/warmup_project/blob/d0a6f20ffa07e21bbb0510cbe827e35395af63c2/person_follower.gif)

## Wall Follower
The goal of this code is to have the robot follow a wall. In order to get this behavior, I adapted my code from person follower but once the robot was in the accepted range of distances from the wall, rather than having the robot face the closest object, I had the robot attempt to maintain the closest object at an angle of 90 degrees as the robot continued to move forward.

In the initialization function, I subscribed to the scanner topic in order to process the laser scanner data and set up a publisher for velocity topic in order to set velocities. I processed the scanner data very similarly to person follower to get the angle of the closest object. If the closest object was in the accepted range of distances, I had the robot maintain a 90 degree angle from the object. If the angle change necessary to do this was larger than 5 degrees, I had the robot move at a slower linear velocity and also increased the constant for propoertional control of the angular velocity. If the robot sensed an object but it was further than the maximum distance, I had it turn to face the object and move forward at a constant velocity. If the robot sensed an object too close by, I had it move back with proportional control to the proper distance while also turning to face the object to avoid potential collisions. If no object was sensed, I had the robot move forward at a constant rate. 

![wall follower](https://github.com/emilialim8/warmup_project/blob/d0a6f20ffa07e21bbb0510cbe827e35395af63c2/wall_follower.gif)


## Challenges

After over coming the inital confusion of how ROS works with topics and sending messages, implementing drive in a square was relatively straight forward aside from slight discrepancies in turns. With person follower, I initially struggled with processing and interpreting the scan data. For wall follower, I started by adapting my person follower code which lead to some issues with maintaining a consistent distance from the wall as well as issues with turning around outside corners as the robot would get too far away from the wall while turning and would not be able to find the wall again. I was able to fix this issue my implementing my person follower code when the robot got too far away so it would move back towards the wall. 

## Future Work

For drive in a square, some of the inaccuracies in turning could potentially be fixed by controlling the turns with odometry rather than through timing each turn. For person follower, it could be good to check a range of angles and average them rather than rely on a single measurement. 
For wall follower, it could be interesting to try implementing a method that is based on mainting the ideal distance at a specific angle rather mainting the closest distance at 90 degrees. For example, using proportional control to maintain a distance of 0.3 m at a 90 degree angle. This would likely resolve some of the slight discrepancies in the distance to the wall, as well as potentially allow for better turns. 

## Takeaways

- This project also helped me to better understand the system of subscribing and publishing to different topics in order to control the robot. While initally this was somewhat confusing for me, through these projects I grew more comfortable with the idea of publishing commands to topics and subscribing and processing data from other topics.
- Proportional control is a very powerful tool for implementing dynamic behaviors. Through simple math, it is possible to create a feedback system to respond to different environments. 