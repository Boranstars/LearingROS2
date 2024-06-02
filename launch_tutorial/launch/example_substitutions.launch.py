from launch_ros.actions import Node

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, TimerAction
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, PythonExpression

def generate_launch_description():

    #LaunchConfiguration本身并不存储任何值，它只是一个获取值的接口。
    #defualt参数可以用来指定当配置项在运行时没有被提供时使用的默认值
    #当你尝试获取一个配置项的值时，LaunchConfiguration会首先查看是否在运行时提供了这个配置项的值。如果没有，它会使用default参数指定的值。
    #如果没有提供default参数，LaunchConfiguration会返回一个空字符串。
    turtlesim_namespace = LaunchConfiguration('turtlesim_namespace', default='turtlesim1')
    use_provided_red = LaunchConfiguration('use_provided_red', default='False')
    new_background_red = LaunchConfiguration('new_background_red', default='200') 

    #LaunchConfiguration和DeclareLaunchArgument的主要区别在于，LaunchConfiguration是用来获取参数值的，而DeclareLaunchArgument是用来声明和设置参数的。
    #LaunchConfiguration的值是由DeclareLaunchArgument设置的，而不是直接设置的。
    turtlesim_namespace_launch_arg = DeclareLaunchArgument(
        'turtlesim_namespace',
        default_value='turtlesim1',
        description='The namespace to be used by the turtlesim node'
    )

    use_provided_red_launch_arg = DeclareLaunchArgument(
        'use_provided_red',
        default_value='False',
        description='Whether to use the provided red value'
    )

    new_background_red_launch_arg = DeclareLaunchArgument(
        'new_background_red',
        default_value='200',
        description='The new background red value'
    )

    #Node的参数是一个字典，其中包含了所有的参数名和值。
    #这些参数的值可以是LaunchConfiguration对象，也可以是PythonExpression对象。
    turtlesim_node = Node(
        package='turtlesim',
        executable='turtlesim_node',
        namespace=turtlesim_namespace,
        name='sim'
    )

    
    spwan_turtle = ExecuteProcess(
        cmd=[[
            'ros2 service call ',
            turtlesim_namespace,
            '/spawn ',
            'turtlesim/srv/Spawn ',
            '"{x: 2.0, y: 2.0, theta: 0.2}"'
        ]],
        shell=True,
    )

    change_background_r = ExecuteProcess(
        cmd=[[
            'ros2 param set ',
            turtlesim_namespace,
            '/sim background_r ',
            '120'
        ]],
        shell=True,
    )

    change_background_r_conditioned = ExecuteProcess(
        condition=IfCondition(
            PythonExpression([
                new_background_red,
                ' == 200',
                ' and ',
                use_provided_red
            ])
        ),
        cmd=[[
            'ros2 param set ',
            turtlesim_namespace,
            '/sim background_r ',
            new_background_red
        ]],
        shell=True
    )

    return LaunchDescription([
        turtlesim_namespace_launch_arg,
        use_provided_red_launch_arg,
        new_background_red_launch_arg,
        turtlesim_node,
        spwan_turtle,
        change_background_r,
        TimerAction(
            period=2.0,
            actions=[
                change_background_r_conditioned
            ]
        )
    ])
    


