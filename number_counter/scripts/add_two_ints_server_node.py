#!/usr/bin/env python

import rospy

from addInts import AddInts

if __name__ == '__main__':

    rospy.init_node("add_two_ints_server")
    rospy.loginfo("Add two ints server node created ...")
    AddInts()
    rospy.spin()
