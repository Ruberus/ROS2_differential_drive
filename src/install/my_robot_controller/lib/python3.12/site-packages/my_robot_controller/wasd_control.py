import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys, select, termios, tty

msg= """
Moving around:

  w
a s d

To stop: Any other button
To quit: CNTRL-C
"""

class WASDControl(Node):
    def __init__(self):
        super().__init__('wasd_control')
        self.publisher_=self.create_publisher(Twist, '/cmd_vel', 10)
        self.settings=termios.tcgetattr(sys.stdin)
    def get_key(self):
        tty.setraw(sys.stdin.fileno())
        select.select([sys.stdin],[],[],0.1)
        key=sys.stdin.read(1)
        termios.tscsetattr(sys.stdin,termios.TCSADRAIN, self.settings)
        return key
    def run(self):
        print(msg)
        while True:
            if key == 'w':
                twist.linear.x = 0.5
            elif key == 's':
                twist.linear.x = -0.5
            elif key == 'a':
                twist.angular.z = 1.0
            elif key == 'd':
                twist.angular.z = -1.0
            elif key == '\x03':
                break
            else:
                twist.angular.z=0.0
                twist.linear.x=0.0
            self.publisher_.publish(twist)

def main():
    rclpy.init()
    node=WASDControl()
    try:
        node.run()
    except:
        print(e)
    finally:
        rclpy.shutdown()
if __name__=='main':
    main()
