import rospy
from geometry_msgs.msg import Twist

def callback(data):
    rospy.loginfo("tutle at (" + str(data.linear.x) + ", " + str(data.linear.y) + ")")

def listener ():
    # In ROS , nodes are uniquely named. If two nodes with the same
    # name are launched , the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our ’listener ’ node so that multiple listeners can
    # run simultaneously.
    rospy.init_node("turtle_listener", anonymous=True)
    rospy.Subscriber("/turtle1/cmd_vel", Twist, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == "__main__":
    listener ()