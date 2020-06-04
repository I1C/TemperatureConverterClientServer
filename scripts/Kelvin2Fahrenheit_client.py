#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from beginner_tutorials.srv import *

def Kelvin2Fahrenheit_client(x):
    rospy.wait_for_service('K2F')
    try:
        K2FF = rospy.ServiceProxy('K2F', Kelvin2Fahrenheit)
        return K2FF(x)
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x]"% float(sys.argv[0])

if __name__ == "__main__":
     if len(sys.argv) == 2:
        x = float(sys.argv[1])
        Kelvin2Fahrenheit_client(x)
     else:
        print(usage())
        sys.exit(1)
     print("Requesting %s"%(x))
     var=x*9/5-459.67
     print(str(x)+" Kelvin degrees is " + str(var) + " Fahrenheit degrees")
     
