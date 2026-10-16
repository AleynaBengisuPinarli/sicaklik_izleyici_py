#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class IzleyiciNode(Node):
    def __init__(self):
        super().__init__('izleyici_node')
        
        # Bonus: Eşik değeri parametresi (varsayılan: 30.0)
        self.declare_parameter('esik_deger', 30.0)
        
        self.subscription = self.create_subscription(
            Float32,
            'sicaklik',
            self.listener_callback,
            10
        )
        self.get_logger().info('İzleyici Düğümü Başlatıldı. Sıcaklıklar dinleniyor...')

    def listener_callback(self, msg):
        esik = self.get_parameter('esik_deger').get_parameter_value().double_value
        self.get_logger().info(f'Alınan Sıcaklık: {msg.data} °C')
        
        if msg.data > esik:
            self.get_logger().warn(f'DİKKAT! Sıcaklık eşik değerini aştı! ({msg.data} °C > {esik} °C)')

def main(args=None):
    rclpy.init(args=args)
    izleyici_node = IzleyiciNode()
    try:
        rclpy.spin(izleyici_node)
    except KeyboardInterrupt:
        pass
    izleyici_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

