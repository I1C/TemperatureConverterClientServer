#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from beginner_tutorials.srv import *

def Celsius2Kelvin_client(x):
    rospy.wait_for_service('C2K')
    try:
        C2KK = rospy.ServiceProxy('C2K', Celsius2Kelvin)
        return C2KK(x)
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x]"% float(sys.argv[0])

if __name__ == "__main__":
     if len(sys.argv) == 2:
        x = float(sys.argv[1])
        Celsius2Kelvin_client(x)
     else:
        print(usage())
        sys.exit(1)
     print("Requesting %s"%(x))
     var=x+273.15
     print(str(x)+" Celsius degrees is " + str(var) + " Kelvin degrees")
     
