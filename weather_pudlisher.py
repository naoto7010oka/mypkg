import rclpy
from rclpy.node import Node
import requests
from std_msgs.msg import String

class WeatherPublisher(Node):
    def __init__(self):
        super()._init_('weather_publisher')
        self.publisher_= self.create_publisher(String,'weather_info', 10)
        self.timer = self.create_timer(10.0, self.publish_weather_info)
        self.api_key = 'YOUR_API_KEY'
        self.location = 'Tokyo Disney Resort'
        self.get_logger().info('Weather Publisher Node has been sterted.')

