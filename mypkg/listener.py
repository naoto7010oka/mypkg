import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16


class ListenerNode(Node):
    def __init__(self):
        super().__init__('listener')  
        
        self.subscription = self.create_subscription(Int16,'countup',self.callback, 10)

    def callback(self, msg):
        
        self.get_logger().info(f'Listen: {msg.data}')


def main(args=None):
    
    rclpy.init(args=args)
    
    node = ListenerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        
        node.get_logger().info('Shutting down node.')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
