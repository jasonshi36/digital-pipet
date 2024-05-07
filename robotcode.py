from pymycobot.mycobot import MyCobot
import serial
import time

# 初始化 MyCobot
mc = MyCobot('/dev/ttyAMA0', 1000000)

# 打开液体泵的串口
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(1)
print(ser.readline())

angles_list = {
    'ini': [0, 0, 0, 0, 0, 0],
    'TFA_up': [26,(-20),(-35),76,(-17),(0)],
    'TFA': [27.07,(-58.5),(-35),90,(-38.19),(-1.5)],
    'plate_up': [-60, 0, -41, 70, 0, 0],
    'A1': [(-57.3),(-22),(-36.5),64,(-56.5),0],
    'B1': [(-54.8),(-22),(-36.5),64,(-56.2),0],
    'C1': [(-53.5),(-22),(-36.5),64,(-54.5),0],
    'D1': [(-51),(-22),(-36.5),64,(-53.5),0],
    'E1': [(-49.2),(-22),(-36.5),64,(-52.2),0],
    'F1': [(-50.5),(-22),(-36.5),64,(-45.5),0],
    'G1': [(-49),(-22),(-36.5),64,(-40.5),0],
    'H1': [(-50.5),(-22),(-36.5),64,(-30),0],
    
    'A2': [(-54),(-21),(-36.5),64,(-69.3),0],
    'B2': [(-51),(-21),(-36.5),64,(-66.8),0],
    'C2': [(-48.4),(-21),(-36.5),64,(-69.5),0],
    'D2': [(-46.4),(-21),(-36.5),64,(-66.3),0],
    'E2': [(-44),(-21),(-36.5),64,(-68),0],
    'F2': [(-42.5),(-21),(-36.5),64,(-66),0],
    'G2': [(-41),(-21),(-36.5),64,(-62.5),0],
    'H2': [(-41),(-21),(-36.5),64,(-57),0],
    
    'A3': [(-50.7),(-20),(-36.5),62,(-77.5),0],
    'B3': [(-47.7),(-20),(-36.5),62,(-74.5),0],
    'C3': [(-45.5),(-20),(-36.5),62,(-74),0],
    'D3': [(-42.8),(-20),(-36.5),62,(-73),0],
    'E3': [(-41),(-20),(-36.5),62,(-72),0],
    'F3': [(-39.5),(-20),(-36.5),62,(-69.5),0],
    'G3': [(-37),(-20),(-36.5),62,(-69),0],
    'H3': [(-35.3),(-20),(-36.5),62,(-68),0],
    
    'A4': [(-48),(-20),(-36.5),62,(-85.5),0],
    'B4': [(-43.8),(-20),(-36.5),62,(-87),0],
    'C4': [(-41.5),(-20),(-36.5),62,(-86),0],
    'D4': [(-39.2),(-20),(-36.5),62,(-85.5),0],
    'E4': [(-37),(-20),(-36.5),62,(-85),0],
    'F4': [(-34.5),(-20),(-36.5),62,(-84.5),0],
    'G4': [(-33.2),(-20),(-36.5),62,(-81),0],
    'H4': [(-30.5),(-20),(-36.5),62,(-81),0],
    
    'A5': [(-45),(-19),(-36.5),62,(-97),0],
    'B5': [(-41),(-19),(-36.5),62,(-97),0],
    'C5': [(-37.7),(-19),(-36.5),62,(-98.5),0],
    'D5': [(-36),(-19),(-36.5),62,(-95),0],
    'E5': [(-33.4),(-19),(-36.5),62,(-96.5),0],
    'F5': [(-31.5),(-19),(-36.5),62,(-93),0],
    'G5': [(-29),(-19),(-36.5),62,(-92),0],
    'H5': [(-27.5),(-19),(-36.5),62,(-89.3),0],
    
    'A6': [(-42.5),(-19),(-36.5),62,(-106),0],
    'B6': [(-39.5),(-19),(-36.5),62,(-105),0],
    'C6': [(-36),(-19),(-36.5),62,(-105),0],
    'D6': [(-33.3),(-19),(-36.5),62,(-105),0],
    'E6': [(-31.5),(-19),(-36.5),62,(-106),0],
    'F6': [(-29),(-19),(-36.5),62,(-103),0],
    'G6': [(-27),(-19),(-36.5),62,(-102),0],
    'H6': [(-25.5),(-19),(-36.5),62,(-97.5),0],
    
    'A7': [(-40.8),(-19),(-36.5),62,(-114),0],
    'B7': [(-37.3),(-19),(-36.5),62,(-112.5),0],
    'C7': [(-33.8),(-19),(-36.5),62,(-113.5),0],
    'D7': [(-31.3),(-19),(-36.5),62,(-112),0],
    'E7': [(-28.5),(-19),(-36.5),62,(-111.5),0],
    'F7': [(-26.8),(-19),(-36.5),62,(-110),0],
    'G7': [(-23.8),(-19),(-36.5),62,(-110),0],
    'H7': [(-21.5),(-19),(-36.5),62,(-106.4),0],
    
    'A8': [(-39.5),(-18.5),(-36.5),62,(-122),0],
    'B8': [(-36),(-18.5),(-36.5),62,(-121.5),0],
    'C8': [(-32.5),(-18.5),(-36.5),62,(-121.5),0],
    'D8': [(-30),(-18.5),(-36.5),62,(-119),0],
    'E8': [(-26.5),(-18.5),(-36.5),62,(-119.5),0],
    'F8': [(-23.5),(-18.5),(-36.5),62,(-119.5),0],
    'G8': [(-21),(-18.5),(-36.5),62,(-117),0],
    'H8': [(-18.5),(-18.5),(-36.5),62,(-115),0],
   
    
    'A9': [(-38.5),(-20),(-36.5),62,(-127.5),0],
    'B9': [(-35),(-20),(-36.5),62,(-127.5),0],
    'C9': [(-31),(-20),(-36.5),62,(-127),0],
    'D9': [(-28),(-20),(-36.5),62,(-126),0],
    'E9': [(-25),(-20),(-36.5),62,(-126),0],
    'F9': [(-22),(-20),(-36.5),62,(-125),0],
    'G9': [(-19),(-20),(-36.5),62,(-124),0],
    'H9': [(-16.5),(-20),(-36.5),62,(-121),0],
    
    'A10': [(-38),(-20),(-36.5),62,(-136),0],
    'B10': [(-34),(-20),(-36.5),62,(-134.5),0],
    'C10': [(-30),(-20),(-36.5),62,(-134),0],
    'D10': [(-26.3),(-20),(-36.5),62,(-133.5),0],
    'E10': [(-23),(-20),(-36.5),62,(-132),0],
    'F10': [(-20),(-20),(-36.5),62,(-131),0],
    'G10': [(-17),(-20),(-36.5),62,(-130),0],
    'H10': [(-14),(-20),(-36.5),62,(-127),0],
    
    'A11': [(-38),(-20),(-36.5),62,(-142),0],
    'B11': [(-33.5),(-20),(-36.5),62,(-142),0],
    'C11': [(-29.5),(-20),(-36.5),62,(-141),0],
    'D11': [(-25.5),(-20),(-36.5),62,(-140),0],
    'E11': [(-21.8),(-20),(-36.5),62,(-138.5),0],
    'F11': [(-18.3),(-20),(-36.5),62,(-137.5),0],
    'G11': [(-15.8),(-20),(-36.5),62,(-136),0],
    'H11': [(-12.5),(-20),(-36.5),62,(-134.5),0],
    
    'A12': [(-38.5),(-20),(-36.5),62,(-148),0],
    'B12': [(-33),(-20),(-36.5),62,(-147.5),0],
    'C12': [(-29),(-20),(-36.5),62,(-146.5),0],
    'D12': [(-25.5),(-20),(-36.5),62,(-146),0],
    'E12': [(-21.5),(-20),(-36.5),62,(-145),0],
    'F12': [(-17),(-20),(-36.5),62,(-143),0],
    'G12': [(-13.5),(-20),(-36.5),62,(-142),0],
    'H12': [(-10),(-20),(-36.5),62,(-139),0]
    
    # More coords need to be added as A2, A3...
}

# Length that corresponds to each volume
len_0mL = 1820
len_1mL = 1755
len_5mL = 1528
len_10mL = 1286

volume_list = {

   '300uL' : 12,
   '500uL' :30,
   '1mL' : 55
}
# Counter for adjusting pump length
volume_used = 0
current_volume = 0
refill_statu = 0
refill_length = 1300
# Function to perform MyCobot movement
def move_mycobot(angles, speed, wait_time):
    mc.send_angles(angles, speed)
    time.sleep(wait_time)
    
def pump_action(volume, duration):
    ser.write(bytes(str(volume), 'ascii'))  # Convert volume to string before writing to serial
    time.sleep(duration)

# Function to calculate length for given volume
# Function to calculate length for given volume


# Function to dispense liquid
def dispense_liquid(volume, position):
    global refill_statu, volume_used, current_volume, refill_length
    if current_volume <= 0 or current_volume - volume_list[volume] <= 0:
        print("Liquid empty. Moving to liquid suction position.")
        refill_pump()
        refill_statu = 1

    move_mycobot(angles_list[position], 20, 2)
    if refill_statu == 1:
        time.sleep(3)
        refill_statu = 0
    #time.sleep(1)  # 移动后加入短暂延迟
    refill_length = refill_length + volume_list[volume]
    ser.write(str(refill_length).encode('ascii'))
    time.sleep(4)
    volume_used += volume_list[volume]
    current_volume -= volume_list[volume]
    print('finish ' + position + ' ' + str(refill_length))
    return False


def empty_pump():
    global volume_used, current_volume
    move_mycobot(angles_list['ini'], 20, 3)
    move_mycobot(angles_list['TFA_up'], 20, 3)  
    move_mycobot(angles_list['TFA'], 10, 3)
    pump_action(len_0mL, 6)
    move_mycobot(angles_list['TFA_up'], 20, 3)
    move_mycobot(angles_list['ini'], 20, 3)
    current_volume = 0
    volume_used = 510

# Function to refill the pump with 10ml liquid
def refill_pump():
    global refill_statu, volume_used, current_volume, refill_length
    print("Refilling the pump with 10ml liquid.")
    move_mycobot(angles_list['ini'], 20, 5)
    move_mycobot(angles_list['TFA_up'], 20, 3)  # Move to the position where the pump can be refilled
    move_mycobot(angles_list['TFA'], 10, 3)  # Move to the suction position
    pump_action(len_10mL , 7)  # Transfer liquid
    pump_action(1300 , 5)
    current_volume = 510
    volume_used = 0
    refill_length = 1300
    move_mycobot(angles_list['TFA_up'], 20, 3)
    move_mycobot(angles_list['ini'], 20, 3)
    move_mycobot(angles_list['plate_up'], 20, 3)
    
    
    # Add your code here to refill the pump with 10ml liquid

# 测试运行
try:
   

   dispense_liquid('1mL', 'A1')
   dispense_liquid('300uL', 'B1')
   dispense_liquid('1mL', 'C1')
   dispense_liquid('300uL', 'D1')
   dispense_liquid('1mL', 'E1')
   dispense_liquid('1mL', 'F1')
   dispense_liquid('300uL', 'G1')
   dispense_liquid('1mL', 'H1')
   
   dispense_liquid('300uL', 'A2')
   dispense_liquid('1mL', 'B2')
   dispense_liquid('300uL', 'C2')
   dispense_liquid('1mL', 'D2')
   dispense_liquid('300uL', 'E2')
   dispense_liquid('1mL', 'F2')
   dispense_liquid('300uL', 'G2')
   dispense_liquid('1mL', 'H2')
   '''
   dispense_liquid('300uL', 'A3')
   dispense_liquid('300uL', 'B3')
   dispense_liquid('300uL', 'C3')
   dispense_liquid('300uL', 'D3')
   dispense_liquid('300uL', 'E3')
   dispense_liquid('300uL', 'F3')
   dispense_liquid('300uL', 'G3')
   dispense_liquid('300uL', 'H3')
   '''
   dispense_liquid('1mL', 'A4')
   dispense_liquid('300uL', 'B4')
   dispense_liquid('1mL', 'C4')
   dispense_liquid('300uL', 'D4')
   dispense_liquid('1mL', 'E4')
   dispense_liquid('300uL', 'F4')
   dispense_liquid('1mL', 'G4')
   dispense_liquid('300uL', 'H4')
   '''
   
   dispense_liquid('300uL', 'A5')
   dispense_liquid('300uL', 'B5')
   dispense_liquid('300uL', 'C5')
   dispense_liquid('300uL', 'D5')
   dispense_liquid('300uL', 'E5')
   dispense_liquid('300uL', 'F5')
   dispense_liquid('300uL', 'G5')
   dispense_liquid('300uL', 'H5')
   '''
   
   dispense_liquid('1mL', 'A6')
   dispense_liquid('1mL', 'B6')
   dispense_liquid('1mL', 'C6')
   dispense_liquid('1mL', 'D6')
   dispense_liquid('1mL', 'E6')
   dispense_liquid('1mL', 'F6')
   dispense_liquid('1mL', 'G6')
   dispense_liquid('1mL', 'H6')
   
   dispense_liquid('1mL', 'A7')
   dispense_liquid('1mL', 'B7')
   dispense_liquid('1mL', 'C7')
   dispense_liquid('1mL', 'D7')
   dispense_liquid('1mL', 'E7')
   dispense_liquid('1mL', 'F7')
   dispense_liquid('1mL', 'G7')
   dispense_liquid('1mL', 'H7')
  
   dispense_liquid('1mL', 'A8')
   dispense_liquid('1mL', 'B8')
   dispense_liquid('1mL', 'C8')
   dispense_liquid('1mL', 'D8')
   dispense_liquid('1mL', 'E8')
   dispense_liquid('1mL', 'F8')
   dispense_liquid('1mL', 'G8')
   dispense_liquid('1mL', 'H8')
   '''
   dispense_liquid('300uL', 'A9')
   dispense_liquid('300uL', 'B9')
   dispense_liquid('300uL', 'C9')
   dispense_liquid('300uL', 'D9')
   dispense_liquid('300uL', 'E9')
   dispense_liquid('300uL', 'F9')
   dispense_liquid('300uL', 'G9')
   dispense_liquid('300uL', 'H9')
   
   dispense_liquid('300uL', 'A10')
   dispense_liquid('300uL', 'B10')
   dispense_liquid('300uL', 'C10')
   dispense_liquid('300uL', 'D10')
   dispense_liquid('300uL', 'E10')
   dispense_liquid('300uL', 'F10')
   dispense_liquid('300uL', 'G10')
   dispense_liquid('300uL', 'H10')
   
   dispense_liquid('300uL', 'A11')
   dispense_liquid('300uL', 'B11')
   dispense_liquid('300uL', 'C11')
   dispense_liquid('300uL', 'D11')
   dispense_liquid('300uL', 'E11')
   dispense_liquid('300uL', 'F11')
   dispense_liquid('300uL', 'G11')
   dispense_liquid('300uL', 'H11')
   
   dispense_liquid('300uL', 'A12')
   dispense_liquid('300uL', 'B12')
   dispense_liquid('300uL', 'C12')
   dispense_liquid('300uL', 'D12')
   dispense_liquid('300uL', 'E12')
   dispense_liquid('300uL', 'F12')
   dispense_liquid('300uL', 'G12')
   dispense_liquid('300uL', 'H12')
   '''
   empty_pump()

finally:
    # Close the serial ports
    ser.close()

