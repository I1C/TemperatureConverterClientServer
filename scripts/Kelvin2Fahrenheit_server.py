#!/usr/bin/env python
from __future__ import print_function

from beginner_tutorials.srv import Kelvin2Fahrenheit 
import rospy
v = 0
def handle_Kelvin2Fahrenheit(req):
    v = req.a * 9/5 - 459.67
    print ("For "+str(float(req.a))+" Kelvin degrees, "+"Fahrenheit temperature is " + str(v)+" degrees")
    return (v)

def Kelvin2Fahrenheit_server():
    rospy.init_node('Kelvin2Fahrenheit_server')
    s = rospy.Service('K2F', Kelvin2Fahrenheit, handle_Kelvin2Fahrenheit)
    print("Ready to add the Kelvin temperature.")
    rospy.spin()

if __name__ == "__main__":
    Kelvin2Fahrenheit_server()
