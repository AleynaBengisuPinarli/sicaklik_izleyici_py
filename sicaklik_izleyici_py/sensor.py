#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class SensorNode(Node):
    def __init__(self):
        super().__init__('sensor_node')
        self.publisher_ = self.create_publisher(Float32, 'sicaklik', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info('Sensor Düğümü Başlatıldı. Sıcaklık verileri yayınlanıyor...')

    def timer_callback(self):
        msg = Float32()
        msg.data = round(random.uniform(20.0, 40.0), 2)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Yayınlanan Sıcaklık: {msg.data} °C')

def main(args=None):
    rclpy.init(args=args)
    sensor_node = SensorNode()
    try:
        rclpy.spin(sensor_node)
    except KeyboardInterrupt:
        pass
    sensor_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

