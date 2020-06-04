#!/usr/bin/env python
from __future__ import print_function

from beginner_tutorials.srv import Fahrenheit2Kelvin 
import rospy
v = 0
def handle_Fahrenheit2Kelvin(req):
    v = (req.a+459.67)*5/9
    print ("For "+str(float(req.a))+" Fahrenheit degrees, "+"Kelvin temperature is " + str(v)+" degrees")
    return (v)

def Fahrenheit2Kelvin_server():
    rospy.init_node('Fahrenheit2Kelvin_server')
    s = rospy.Service('F2K', Fahrenheit2Kelvin, handle_Fahrenheit2Kelvin)
    print("Ready to add the Fahrenheit temperature.")
    rospy.spin()

if __name__ == "__main__":
    Fahrenheit2Kelvin_server()
