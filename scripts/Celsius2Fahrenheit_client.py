#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from beginner_tutorials.srv import *

def Celsius2Fahrenheit_client(x):
    rospy.wait_for_service('C2F')
    try:
        C2FF = rospy.ServiceProxy('C2F', Celsius2Fahrenheit)
        return C2FF(x)
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x]"% float(sys.argv[0])

if __name__ == "__main__":
     if len(sys.argv) == 2:
        x = float(sys.argv[1])
        Celsius2Fahrenheit_client(x)
     else:
        print(usage())
        sys.exit(1)
     print("Requesting %s"%(x))
     var=x*1.8+32
     print(str(x)+" Celsius degrees is " + str(var) + " Fahrenheit degrees")
     
