#!/usr/bin/env python
from __future__ import print_function

from beginner_tutorials.srv import Celsius2Fahrenheit 
import rospy
v = 0
def handle_Celsius2Fahrenheit(req):
    v = req.a * 1.8 +32
    print ("For "+str(float(req.a))+" Celsius degrees, "+"Fahrenheit temperature is " + str(v)+" degrees")
    return (v)

def Celsius2Fahrenheit_server():
    rospy.init_node('Celsius2Fahrenheit_server')
    s = rospy.Service('C2F', Celsius2Fahrenheit, handle_Celsius2Fahrenheit)
    print("Ready to add the Celsius temperature.")
    rospy.spin()

if __name__ == "__main__":
    Celsius2Fahrenheit_server()
