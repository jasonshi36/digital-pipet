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
    'A1': [(-57.5),(-22),(-36.5),64,(-56.5),0],
    'B1': [(-54.5),(-22),(-36.5),64,(-56.5),0],
    'C1': [(-53.5),(-22),(-36.5),64,(-54.5),0],
    'D1': [(-51),(-22),(-36.5),64,(-53.5),0],
    'E1': [(-49),(-22),(-36.5),64,(-52.5),0],
    'F1': [(-50.5),(-22),(-36.5),64,(-45.5),0],
    'G1': [(-49),(-22),(-36.5),64,(-40.5),0],
    'H1': [(-50.5),(-22),(-36.5),64,(-29.5),0],
    
    'A2': [(-54),(-21),(-36.5),64,(-69.3),0],
    'B2': [(-51),(-21),(-36.5),64,(-66.8),0],
    'C2': [(-48),(-21),(-36.5),64,(-69.5),0],
    'D2': [(-46),(-21),(-36.5),64,(-66.3),0],
    'E2': [(-43.5),(-21),(-36.5),64,(-68),0],
    'F2': [(-41.6),(-21),(-36.5),64,(-66.5),0],
    'G2': [(-41),(-21),(-36.5),64,(-62),0],
    'H2': [(-41),(-21),(-36.5),64,(-57.5),0],
    
    'A3': [(-50.4),(-20),(-36.5),62,(-78),0],
    'B3': [(-47.4),(-20),(-36.5),62,(-74.5),0],
    'C3': [(-45.5),(-20),(-36.5),62,(-75),0],
    'D3': [(-42),(-20),(-36.5),62,(-72.5),0],
    'E3': [(-41),(-20),(-36.5),62,(-71),0],
    'F3': [(-39),(-20),(-36.5),62,(-69.5),0],
    'G3': [(-36.5),(-20),(-36.5),62,(-69),0],
    'H3': [(-35),(-20),(-36.5),62,(-68),0],
    
    'A4': [(-47.7),(-20),(-36.5),62,(-85.5),0],
    'B4': [(-43.5),(-20),(-36.5),62,(-87),0],
    'C4': [(-41.5),(-20),(-36.5),62,(-86),0],
    'D4': [(-39.2),(-20),(-36.5),62,(-85.5),0],
    'E4': [(-37),(-20),(-36.5),62,(-85),0],
    'F4': [(-34.5),(-20),(-36.5),62,(-84),0],
    'G4': [(-33),(-20),(-36.5),62,(-81),0],
    'H4': [(-30),(-20),(-36.5),62,(-81.6),0],
    
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
    
    'A7': [(-40.5),(-19),(-36.5),62,(-114),0],
    'B7': [(-37),(-19),(-36.5),62,(-112.5),0],
    'C7': [(-33.5),(-19),(-36.5),62,(-113.5),0],
    'D7': [(-31),(-19),(-36.5),62,(-112),0],
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
    'B10': [(-34),(-20),(-36.5),62,(-135),0],
    'C10': [(-30),(-20),(-36.5),62,(-134.5),0],
    'D10': [(-26.3),(-20),(-36.5),62,(-134),0],
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
    'B12': [(-33),(-20),(-36.5),62,(-148),0],
    'C12': [(-29),(-20),(-36.5),62,(-147),0],
    'D12': [(-25.5),(-20),(-36.5),62,(-146),0],
    'E12': [(-21.5),(-20),(-36.5),62,(-145),0],
    'F12': [(-17),(-20),(-36.5),62,(-143),0],
    'G12': [(-13.5),(-20),(-36.5),62,(-142.5),0],
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
   '1mL' : 65
}
# Counter for adjusting pump length
counter = 1

# Function to perform MyCobot movement
def move_mycobot(angles, speed, wait_time):
    mc.send_angles(angles, speed)
    time.sleep(wait_time)
    
def pump_action(volume, duration):
    ser.write(bytes(str(volume), 'ascii'))  # Convert volume to string before writing to serial
    time.sleep(duration)
    print(ser.readline())

# Function to calculate length for given volume
def calculate_length():
    global counter
    return str(int(1300 + counter * volume))

    
# Function to dispense liquid
def dispense_liquid(volume, position):
    global counter, refill_statu
   
    if 1300 + counter * volume > 1800:
        print("Liquid empty. Moving to liquid suction position.")
        refill_pump()
        refill_statu = 1
        return True
        
    move_mycobot(angles_list[position], 20, 2)
    if refill_statu == 1:
        time.sleep(3)
        refill_statu = 0
    time.sleep(1)  # 移动后加入短暂延迟
    length = calculate_length()
    ser.write(length.encode('ascii'))
    time.sleep(2)
    print('finish '+position+' '+length)
    counter += 1
    return False
    
def check_pump():
    pass

def empty_pump():
    move_mycobot(angles_list['ini'], 20, 3)
    move_mycobot(angles_list['TFA_up'], 20, 3)  
    move_mycobot(angles_list['TFA'], 10, 3)
    pump_action(len_0mL, 6)
    move_mycobot(angles_list['TFA_up'], 20, 3)
    move_mycobot(angles_list['ini'], 20, 3)

# Function to refill the pump with 10ml liquid
def refill_pump():
    global counter
    counter = 0  # Reset the counter
    print("Refilling the pump with 10ml liquid.")
    move_mycobot(angles_list['ini'], 20, 5)
    move_mycobot(angles_list['TFA_up'], 20, 3)  # Move to the position where the pump can be refilled
    move_mycobot(angles_list['TFA'], 10, 3)  # Move to the suction position
    pump_action(len_10mL , 7)  # Transfer liquid
    pump_action(1300 , 7)
    move_mycobot(angles_list['TFA_up'], 20, 3)
    move_mycobot(angles_list['ini'], 20, 3)
    move_mycobot(angles_list['plate_up'], 20, 3)
    
    
    # Add your code here to refill the pump with 10ml liquid

# 测试运行
try:
   
   refill_pump()
   dispense_liquid('300uL', 'A1')
   dispense_liquid('300uL', 'B1')
   dispense_liquid('300uL', 'C1')
   dispense_liquid('300uL', 'D1')
   dispense_liquid('300uL', 'E1')
   dispense_liquid('300uL', 'F1')
   dispense_liquid('300uL', 'G1')
   dispense_liquid('300uL', 'H1')
   '''
   dispense_liquid(300, 'A2')
   dispense_liquid(300, 'B2')
   dispense_liquid(300, 'C2')
   dispense_liquid(300, 'D2')
   dispense_liquid(300, 'E2')
   dispense_liquid(300, 'F2')
   dispense_liquid(300, 'G2')
   dispense_liquid(300, 'H2')
   
   dispense_liquid(300, 'A3')
   dispense_liquid(300, 'B3')
   dispense_liquid(300, 'C3')
   dispense_liquid(300, 'D3')
   dispense_liquid(300, 'E3')
   dispense_liquid(300, 'F3')
   dispense_liquid(300, 'G3')
   dispense_liquid(300, 'H3')
   dispense_liquid(300, 'A4')
   dispense_liquid(300, 'B4')
   dispense_liquid(300, 'C4')
   dispense_liquid(300, 'D4')
   dispense_liquid(300, 'E4')
   dispense_liquid(300, 'F4')
   dispense_liquid(300, 'G4')
   dispense_liquid(300, 'H4')
   dispense_liquid(300, 'A5')
   dispense_liquid(300, 'B5')
   dispense_liquid(300, 'C5')
   dispense_liquid(300, 'D5')
   dispense_liquid(300, 'E5')
   dispense_liquid(300, 'F5')
   dispense_liquid(300, 'G5')
   dispense_liquid(300, 'H5')
   
   dispense_liquid(300, 'A6')
   dispense_liquid(300, 'B6')
   dispense_liquid(300, 'C6')
   dispense_liquid(300, 'D6')
   dispense_liquid(300, 'E6')
   dispense_liquid(300, 'F6')
   dispense_liquid(300, 'G6')
   dispense_liquid(300, 'H6')
   
   dispense_liquid(300, 'A7')
   dispense_liquid(300, 'B7')
   dispense_liquid(300, 'C7')
   dispense_liquid(300, 'D7')
   dispense_liquid(300, 'E7')
   dispense_liquid(300, 'F7')
   dispense_liquid(300, 'G7')
   dispense_liquid(300, 'H7')
   
   dispense_liquid(300, 'A8')
   dispense_liquid(300, 'B8')
   dispense_liquid(300, 'C8')
   dispense_liquid(300, 'D8')
   dispense_liquid(300, 'E8')
   dispense_liquid(300, 'F8')
   dispense_liquid(300, 'G8')
   dispense_liquid(300, 'H8')
   
   dispense_liquid(300, 'A9')
   dispense_liquid(300, 'B9')
   dispense_liquid(300, 'C9')
   dispense_liquid(300, 'D9')
   dispense_liquid(300, 'E9')
   dispense_liquid(300, 'F9')
   dispense_liquid(300, 'G9')
   dispense_liquid(300, 'H9')
   
   dispense_liquid(300, 'A10')
   dispense_liquid(300, 'B10')
   dispense_liquid(300, 'C10')
   dispense_liquid(300, 'D10')
   dispense_liquid(300, 'E10')
   dispense_liquid(300, 'F10')
   dispense_liquid(300, 'G10')
   dispense_liquid(300, 'H10')
   
   dispense_liquid(300, 'A11')
   dispense_liquid(300, 'B11')
   dispense_liquid(300, 'C11')
   dispense_liquid(300, 'D11')
   dispense_liquid(300, 'E11')
   dispense_liquid(300, 'F11')
   dispense_liquid(300, 'G11')
   dispense_liquid(300, 'H11')
   
   dispense_liquid(300, 'A12')
   dispense_liquid(300, 'B12')
   dispense_liquid(300, 'C12')
   dispense_liquid(300, 'D12')
   dispense_liquid(300, 'E12')
   dispense_liquid(300, 'F12')
   dispense_liquid(300, 'G12')
   dispense_liquid(300, 'H12')
   '''
   empty_pump()

finally:
    # Close the serial ports
    ser.close()
