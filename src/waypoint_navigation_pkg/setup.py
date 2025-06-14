from setuptools import setup
import os
from glob import glob

package_name = 'waypoint_navigation_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Add the launch files so they're properly installed
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jprl',
    maintainer_email='user@todo.todo',
    description='Waypoint navigation node for Nav2',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'waypoint_publisher = waypoint_navigation_pkg.waypoint_publisher:main',
        ],
    },
)
