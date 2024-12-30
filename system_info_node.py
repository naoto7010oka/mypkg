import rclpy
from rclpy.node import Node
from datetime import datetime
import psutil


class SystemInfoPublisher(Node):
    def __init__(self):
        super().__init__('system_info_publisher')
        self.timer = self.create_timer(1.0, self.publish_info)  # 1秒ごとに実行
        self.get_logger().info("System Info Publisher Node has started.")

    def publish_info(self):
        # 現在時刻を取得
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # バッテリー残量を取得
        battery = psutil.sensors_battery()
        if battery is not None:
            battery_percent = battery.percent
            battery_status = "Charging" if battery.power_plugged else "Not Charging"
        else:
            battery_percent = "N/A"
            battery_status = "No battery detected"
