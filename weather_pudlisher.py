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
    def publish_weather_info(self):
        weather, temp, humidity = self.fetch_weather_info()
        if weather and temp is not None and humidity is not None:
            weather_info = f"今の天気は: {weather}です。, 今の気温は: {temp}°Cです。, 今の湿度は: {humidity}%です。"
            self.get_logger().info(f"Publishing: {weather_info}")
            msg = String()
            msg.data = weather_info
            self.publisher_.publish(msg)
        else:
            self.get_logger().error("Failed to retrieve weather information.")
    def main(args=None):
    rclpy.init(args=args)
    node = WeatherPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Node stopped cleanly.')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
