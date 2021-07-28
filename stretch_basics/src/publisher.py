#!/usr/bin/env python

# This example shows the basic code for publishing on topics.

# Import ROS Python basic API and sys
import rospy
import sys

# We're going to publish 64-bit integers, so we need to import this from the
# std_msgs pacakge.  Note that we need to import this from std_msgs.msg. This
# idiom is common in ROS when importing messages.
from std_msgs.msg import Int64


if __name__ == '__main__':
	# Initialize the node, and call it "publisher".
	rospy.init_node('publisher', argv=sys.argv)

	# Set up a publisher.  This will publish on a topic called "counter", with a
	# message type of Int64.
	publisher = rospy.Publisher('counter', Int64, queue_size=10)

	# Rate allows us to control the (approximate) rate at which we publish things.
	# For this example, we want to publish at 1Hz.
	rate = rospy.Rate(1)

	# Set up a counter that we're going to increment to give us some data to
	# publish.
	counter = 0

	# This will loop until ROS shuts down the node.  This can be done on the
	# command line with a ctrl-C, or automatically from roslaunch.
	while not rospy.is_shutdown():
		# Publish the value of the counter.
		publisher.publish(counter)

		# Print out a log message to the INFO channel to let us know it's working.
		rospy.loginfo('Published {0}'.format(counter))

		# Increment the counter.
		counter += 1

		# Do an idle wait to control the publish rate.  If we don't control the
		# rate, the node will publish as fast as it can, and consume all of the
		# available CPU resources.
		rate.sleep()
