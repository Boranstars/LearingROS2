import argparse
import rclpy
from rclpy.node import Node 
from std_msgs.msg import String
from learning_interface.srv import CompileWords

class ServiceComplieWordsClient(Node):
    def __init__(self,name):
        super().__init__(name)
        self.client = self.create_client(CompileWords, 'compile_words')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting...')
        self.req = CompileWords.Request()
        
    # def send_word_list(self, word_list):
        
    #     self.req.input = ' '.join(word_list)
    #     future = self.client.call_async(self.req)
    #     future.add_done_callback(self.callback)
    def send_word_list(self):
        while True:
            word_list = input("请输入单词列表，用空格分隔，或输入 'exit' 退出：").split()
            if not  word_list : continue
            if word_list[0].lower() == 'exit' :
                break
            self.req.input = ' '.join(word_list)
            future = self.client.call_async(self.req)
            future.add_done_callback(self.callback)

    def callback(self, future):
        try:
            response = future.result()
            self.get_logger().info(f'Response: {response.output}')
        except Exception as e:
            self.get_logger().error(f'Service call failed: {e}')


def main(args=None):
    rclpy.init(args=args)
    client = ServiceComplieWordsClient("service_compile_words_client")
    
    # parser = argparse.ArgumentParser(description='Send a word list to the compile_words service')
    # parser.add_argument('words', metavar='W', type=str, nargs='+',
    #                     help='a list of words to be compiled')
    # args = parser.parse_args()

    client.send_word_list()
    rclpy.spin(client)
    rclpy.shutdown()