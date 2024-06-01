import time
import random
import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
from learning_interface.action import Fib

class FibActionServer(Node):
    
    def __init__(self,name):
        super().__init__(name)
        self._action_server = ActionServer(self,Fib,'fibonacci',self.execute_callback)

    def execute_callback(self,goal_handle):
        self.get_logger().info('Executing goal...')
        feedback_msg = Fib.Feedback()
        feedback_msg.partial_sequence = [0,1]
        for i in range(1,goal_handle.request.order):
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                return Fib.Result()
            self.get_logger().info('Feedback: {0}'.format(feedback_msg.partial_sequence))
            feedback_msg.partial_sequence.append(feedback_msg.partial_sequence[i]+feedback_msg.partial_sequence[i-1])
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)
            
        goal_handle.succeed()
        result = Fib.Result()
        result.sequence = feedback_msg.partial_sequence
        return result # 必须返回一个result对象
    

def main(args=None):
    rclpy.init(args=args)
    fib_action_server = FibActionServer('fib_action_server')
    rclpy.spin(fib_action_server)
    rclpy.shutdown()
