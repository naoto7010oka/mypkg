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
     def fetch_weather_info(self):
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather"
            params = {
                'q': self.location,
                'appid': self.api_key,
                'units': 'metric',
                'lang': 'ja'
            }
            response = requests.get(url, params=params)
            data = response.json()
            if response.status_code == 200:
                weather = data['weather'][0]['description']
                temp = data['main']['temp']
                humidity = data['main']['humidity']
                return weather, temp, humidity
            else:
                self.get_logger().error(f"Failed to fetch weather data: {data.get('message', 'Unknown error')}")
                return None, None, None
        except Exception as e:
            self.get_logger().error(f"Error fetching weather info: {str(e)}")
            return None, None, None

