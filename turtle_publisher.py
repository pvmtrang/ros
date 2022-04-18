import math
import rospy
from geometry_msgs.msg import Twist

def publisher ():
    # con turtlesim su dung topic cmd_vel nay, topic nay su dung datatype twist
    # rostopic list, rostopic type [ten topic]
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist , queue_size =10)
    rospy.init_node("turtle_publisher", anonymous=True)
    rate = rospy.Rate (1) 
    i = 1
    while not rospy.is_shutdown ():
        msg = Twist()
        if i % 2 == 0:
            msg.angular.z = 0
            msg.linear.x = 2
            rospy.loginfo("Moving forward 2m")
        else: 
            msg.linear.x = 0
            msg.angular.z = math.pi / 2
            rospy.loginfo("Turning left")
        pub.publish(msg)
        i += 1
        rate.sleep()

if __name__ == "__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass