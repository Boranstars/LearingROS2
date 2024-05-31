from setuptools import find_packages, setup

package_name = 'learning_topic_py'

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
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'topic_hello_pub = learning_topic_py.topic_hello_pub:main',
            'topic_hello_sub = learning_topic_py.topic_hello_sub:main',
        ],
    },
)
