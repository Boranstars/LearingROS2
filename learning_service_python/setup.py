from setuptools import find_packages, setup

package_name = 'learning_service_python'

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
            'service_compile_words_server = learning_service_python.service_complie_words_server:main',
            'service_compile_words_client = learning_service_python.service_complie_words_client:main',
        ],
        
    },
    
    
)
