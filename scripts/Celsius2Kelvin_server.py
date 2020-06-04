#!/usr/bin/env python
from __future__ import print_function

from beginner_tutorials.srv import Celsius2Kelvin 
import rospy
v = 0
def handle_Celsius2Kelvin(req):
    v = req.a + 273.15
    print ("For "+str(float(req.a))+" Celsius degrees, "+"Kelvin temperature is " + str(v)+" degrees")
    return (v)

def Celsius2Kelvin_server():
    rospy.init_node('Celsius2Kelvin_server')
    s = rospy.Service('C2K', Celsius2Kelvin, handle_Celsius2Kelvin)
    print("Ready to add the Celsius temperature.")
    rospy.spin()

if __name__ == "__main__":
    Celsius2Kelvin_server()
