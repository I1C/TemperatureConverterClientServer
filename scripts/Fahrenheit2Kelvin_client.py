#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from beginner_tutorials.srv import *

def Fahrenheit2Kelvin_client(x):
    rospy.wait_for_service('F2K')
    try:
        F2KK = rospy.ServiceProxy('F2K', Fahrenheit2Kelvin)
        return F2KK(x)
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x]"% float(sys.argv[0])

if __name__ == "__main__":
     if len(sys.argv) == 2:
        x = float(sys.argv[1])
        Fahrenheit2Kelvin_client(x)
     else:
        print(usage())
        sys.exit(1)
     print("Requesting %s"%(x))
     var=(x+459.67)*5/9
     print(str(x)+" Fahrenheit degrees is " + str(var) + " Kelvin degrees")
     
