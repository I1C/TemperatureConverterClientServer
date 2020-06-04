#!/usr/bin/env python
from __future__ import print_function

from beginner_tutorials.srv import Kelvin2Celsius 
import rospy
v = 0
def handle_Kelvin2Celsius(req):
    v = req.a-273.15
    print ("For "+str(float(req.a))+" Kelvin degrees, "+"Celsius temperature is " + str(v)+" degrees")
    return (v)

def Kelvin2Celsius_server():
    rospy.init_node('Kelvin2Celsius_server')
    s = rospy.Service('K2C', Kelvin2Celsius, handle_Kelvin2Celsius)
    print("Ready to add the Kelvin temperature.")
    rospy.spin()

if __name__ == "__main__":
    Kelvin2Celsius_server()
