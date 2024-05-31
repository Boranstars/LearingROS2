import rclpy
from rclpy.node import Node
import time

class HelloRosNode(Node):
    def __init__(self,name='hello_ros_node'):
        super().__init__(name)
        
        while rclpy.ok():
            time.sleep(1)
            self.get_logger().info('Hello ROS2!')
        
def main(args=None):
    rclpy.init(args=args)
    node = HelloRosNode()
    rclpy.spin(node)
    rclpy.shutdown()