
import rospy
from rospy_tutorials.srv import AddTwoInts 

class AddInts:

    def __init__(self):

        self.add_service = rospy.Service("/add_two_ints", AddTwoInts, self.handle_add_two_ints)
        rospy.loginfo("Add two ints has been started ...")

    
    def handle_add_two_ints(self, req):

        result = req.a + req.b
        rospy.loginfo("Sum of" + str(req.a) + " and " + str(req.b) + " is: " + str(result))
        return result
    
    