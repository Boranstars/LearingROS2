import random
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from learning_interface.action import Fib

class FibactionClent(Node):

    def __init__(self:Node,name):
        super().__init__(name)
        self._action_client = ActionClient(self,Fib,'fibonacci')

    def send_goal(self,order: int):
        goal_msg = Fib.Goal()
        goal_msg.order = order

        self._action_client.wait_for_server()

        self._send_goal_future = self._action_client.send_goal_async(goal_msg)

        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self,future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            return
        
        self.get_logger().info('Goal accepted')
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)
    
    def get_result_callback(self,future):
        result = future.result().result
        self.get_logger().info('Result: {0}'.format(result.sequence))
        rclpy.shutdown()
 
def main(args=None):
    rclpy.init(args=args)
    fib_action_client = FibactionClent('fib_action_client')
    fib_action_client.send_goal(random.randint(10,20))
    rclpy.spin(fib_action_client)

    

if __name__ == '__main__':
    main()