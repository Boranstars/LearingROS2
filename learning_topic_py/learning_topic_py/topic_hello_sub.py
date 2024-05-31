import rclpy
from rclpy.node import Node
import time
from std_msgs.msg import String

class HelloSubNode(Node):

    def __init__(self,name):
        super().__init__(name)
        self.subscription = self.create_subscription(String, 'hello', self.listener_callback, 10)
    
    def listener_callback(self,msg):
        self.get_logger().info('I heard: "%s"' % msg.data)



def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(HelloSubNode('hello_sub_node'))
    rclpy.shutdown()