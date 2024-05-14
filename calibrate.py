from pymycobot.mycobot import MyCobot
import serial
import time

# 初始化 MyCobot
mc = MyCobot('/dev/ttyAMA0', 1000000)

angles_list = {
    'ini': [0, 0, 0, 0, 0, 0],
    'TFA_up': [26,(-20),(-35),76,(-17),(0)],
    'TFA': [27.07,(-58.5),(-35),90,(-38.19),(-1.5)],
    'plate_up': [-60, 0, -41, 70, -70, 0],
    'A1': [(-57),(-21),(-36.5),64,(-54.5),0]
    }
    
    
def move_mycobot(angles, speed, wait_time):
    mc.send_angles(angles_list[angles], speed)
    time.sleep(wait_time)
    
move_mycobot('ini', 20, 3)
move_mycobot('plate_up', 20, 3)
move_mycobot('A1', 20, 10)
move_mycobot('plate_up', 20, 3)
move_mycobot('ini', 20, 3)
