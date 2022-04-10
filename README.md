# warmup_project
## Drive in a square
This code allows the robot to drive in a square. The robot first goes straight for approximately 0.4 m and then turn 90 degrees. It repeats this behavior until it completes a square and (theoretically) returns to its starting position. To accomplish this, the robot moves forward with a linear velocity of 0. for 2 seconds. Then I set the linear velocity to 0 and the angular velocity to 45 degrees per second. The robot then rotates for 2 seconds, resulting in a 90 degree turn.

In the initialization function, I subscribe to the /cmd_vel topic. In the run function, I set two possible velocity values that allow the robot to either turn or go straight. Then in a while loop, I have the robot alternate between going straight and turning. The proper velocity is published at a rate of 2 Hz and is published 4 times before switching, resulting in 2 seconds of each behavior.

![drive square](https://github.com/emilialim8/warmup_project/blob/35d1fb89f1d5442e35d7a84669f45e443c43f45e/drive_square.gif)


## Person Follower
challenging to go on 

![person follower]https://github.com/emilialim8/warmup_project/blob/d0a6f20ffa07e21bbb0510cbe827e35395af63c2/person_follower.gif

## Wall Follower

![wall follower]https://github.com/emilialim8/warmup_project/blob/d0a6f20ffa07e21bbb0510cbe827e35395af63c2/wall_follower.gif