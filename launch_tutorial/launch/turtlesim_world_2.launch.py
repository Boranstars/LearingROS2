import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node, PushRosNamespace
from launch.actions import GroupAction, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():

    # 从yaml文件中加载参数
    config = os.path.join(
      get_package_share_directory('launch_tutorial'),
      'config',
      'turtlesim.yaml'
      )



    return LaunchDescription([
      Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim',
            parameters=[config]
      )
   ])