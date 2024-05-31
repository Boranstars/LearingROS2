import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HelloPubNode(Node):

    def __init__(self,name):
        super().__init__(name)
        self.publisher_ = self.create_publisher(String, 'chat', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello ROS2!'
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = HelloPubNode('hello_pub_node')
    rclpy.spin(node)
    rclpy.shutdown()


