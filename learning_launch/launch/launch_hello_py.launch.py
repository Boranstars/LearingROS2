from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='learning_topic_py',
            executable='topic_hello_pub',
            # name='hello_pub',
        ),
        Node(
            package='learning_topic_py',
            executable='topic_hello_sub',
            # name='hello_sub',
        ),
    ])