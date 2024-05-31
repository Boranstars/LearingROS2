import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from learning_interface.srv import CompileWords
import time


class ServiceComplieWordsServer(Node):

    def __init__(self,name):
        super().__init__(name)
        self.server = self.create_service(CompileWords, 'compile_words', self.compile_words_callback)
    
    def compile_words_callback(self,request,response):
        response.output = ' '.join(request.input.split()[::-1])
        self.get_logger().info(f'Request: {request.input}')
        self.get_logger().info(f'Response: {response.output}')
        return response
    
def main(args=None):
    rclpy.init(args=args)
    node = ServiceComplieWordsServer('service_compile_words_server')
    rclpy.spin(node)
    rclpy.shutdown()