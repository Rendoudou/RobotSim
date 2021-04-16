#!/usr/bin/env python
import roslib
import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty

roslib.load_manifest('teleop_twist_keyboard')

msg = """
Reading from the keyboard  and Publishing to Twist!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .
For Holonomic mode (strafing), hold down the shift key:
---------------------------
   U    I    O
   J    K    L
   M    <    >
t : up (+z)
b : down (-z)
anything else : stop
q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%
CTRL-C to quit
"""

moveBindings = {
    'u': (1, 0, 0, 1),
    'i': (1, 0, 0, 0),
    'o': (1, 0, 0, -1),
    'j': (0, 0, 0, 1),
    'l': (0, 0, 0, -1),
    'm': (-1, 0, 0, -1),
    ',': (-1, 0, 0, 0),
    '.': (-1, 0, 0, 1),

    'U': (1, 0, 0, 1),
    'I': (1, 0, 0, 0),
    'O': (1, 0, 0, -1),
    'J': (0, 0, 0, 1),
    'L': (0, 0, 0, -1),
    'M': (-1, 0, 0, -1),
    '<': (-1, 0, 0, 0),
    '>': (-1, 0, 0, 1),

    't': (0, 0, 1, 0),
    'b': (0, 0, -1, 0),

    'T': (0, 0, 1, 0),
    'B': (0, 0, -1, 0),
}

speedBindings = {
    'q': (1.1, 1.1),
    'z': (.9, .9),
    'w': (1.1, 1),
    'x': (.9, 1),
    'e': (1, 1.1),
    'c': (1, .9),
}

speed = 0.60
turn = 0.6
key_stop = 'k'

settings = termios.tcgetattr(sys.stdin)


def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


def vels(cur_speed, cur_turn):
    return "currently: cur_speed: %s cur_turn: %s " % (cur_speed, cur_turn)
    pass


if __name__ == "__main__":
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    rospy.init_node('teleop_twist_keyboard')

    x = 0
    y = 0
    z = 0
    th = 0
    status = 0

    try:
        print msg
        print vels(speed, turn)
        while not rospy.is_shutdown():
            key = getKey()
            if key in moveBindings.keys():
                x = moveBindings[key][0]
                y = moveBindings[key][1]
                z = moveBindings[key][2]
                th = moveBindings[key][3]
            elif key in speedBindings.keys():
                speed = speed * speedBindings[key][0]
                turn = turn * speedBindings[key][1]

                print vels(speed, turn)
                if status == 14:
                    print msg
                status = (status + 1) % 15
            else:
                x = 0
                y = 0
                z = 0
                th = 0
                if key == '\x03':
                    break

            key = key_stop
            twist = Twist()
            twist.linear.x = x * speed
            twist.linear.y = y * speed
            twist.linear.z = z * speed
            twist.angular.x = 0
            twist.angular.y = 0
            twist.angular.z = th * turn
            pub.publish(twist)

    except rospy.ROSInterruptException:
        pass

    finally:
        twist = Twist()
        twist.linear.x = 0
        twist.linear.y = 0
        twist.linear.z = 0
        twist.angular.x = 0
        twist.angular.y = 0
        twist.angular.z = 0
        pub.publish(twist)

        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
