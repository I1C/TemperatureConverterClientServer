#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from beginner_tutorials.srv import *

def Kelvin2Celsius_client(x):
    rospy.wait_for_service('K2C')
    try:
        K2CC = rospy.ServiceProxy('K2C', Kelvin2Celsius)
        return K2CC(x)
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x]"% float(sys.argv[0])

if __name__ == "__main__":
     if len(sys.argv) == 2:
        x = float(sys.argv[1])
        Kelvin2Celsius_client(x)
     else:
        print(usage())
        sys.exit(1)
     print("Requesting %s"%(x))
     var=x-273.15
     print(str(x)+" Kelvin degrees is " + str(var) + " Celsius degrees")
     
