#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Range

Sonar_0 = Sonar_1 = Sonar_2 = Sonar_3 = Sonar_4 = 0

def callback_sonar_0(data):
        global Sonar_0
        Sonar_0 = data.range

def callback_sonar_1(data):
        global Sonar_1
        Sonar_1 = data.range

def callback_sonar_2(data):
        global Sonar_2
        Sonar_2 = data.range

def callback_sonar_3(data):
        global Sonar_3
        Sonar_3 = data.range

def callback_sonar_4(data):
        global Sonar_4
        Sonar_4 = data.range


if __name__ == '__main__':
        print(" Sonar 1  |  Sonar 2  |  Sonar 3  |  Sonar 4  |  Sonar 5")
        print("--------------------------------------------------------")
        rospy.init_node('listener', anonymous=True)
        while  not rospy.is_shutdown():
                rospy.Subscriber('/pi_sonar/sonar_0', Range, callback_sonar_0)
                rospy.Subscriber('/pi_sonar/sonar_1', Range, callback_sonar_1)
                rospy.Subscriber('/pi_sonar/sonar_2', Range, callback_sonar_2)
                rospy.Subscriber('/pi_sonar/sonar_3', Range, callback_sonar_3)
                rospy.Subscriber('/pi_sonar/sonar_4', Range, callback_sonar_4)
                print("{:9.6f} | {:9.6f} | {:9.6f} | {:9.6f} | {:9.6f}".format(Sonar_0, Sonar_1, Sonar_2, Sonar_3, Sonar_4))
                rospy.sleep(0.3)
