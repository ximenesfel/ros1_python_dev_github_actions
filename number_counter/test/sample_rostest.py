#!/usr/bin/env python

import unittest

import rospy


class SampelRostest(unittest.TestCase):
    def test_smoke(self):
        self.assertTrue(True)


if __name__ == "__main__":
    import rostest
    rospy.init_node("sim_test_cases")
    rostest.rosrun("number_counter", "sample_rostest", SampelRostest)