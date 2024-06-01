from setuptools import find_packages, setup

package_name = 'learning_action_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='boran',
    maintainer_email='boranyang3@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'action_fib_server = learning_action_py.action_fib_server:main',
            'action_fib_client = learning_action_py.action_fib_client:main',
        ],
    },
)
