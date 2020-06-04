#!/usr/bin/env python
from __future__ import print_function

from beginner_tutorials.srv import Fahrenheit2Celsius 
import rospy
v = 0
def handle_Fahrenheit2Celsius(req):
    v = (req.a-32)/1.8
    print ("For "+str(float(req.a))+" Fahrenheit degrees, "+"Celsius temperature is " + str(v)+" degrees")
    return (v)

def Fahrenheit2Celsius_server():
    rospy.init_node('Fahrenheit2Celsius_server')
    s = rospy.Service('F2C', Fahrenheit2Celsius, handle_Fahrenheit2Celsius)
    print("Ready to add the Fahrenheit temperature.")
    rospy.spin()

if __name__ == "__main__":
    Fahrenheit2Celsius_server()
