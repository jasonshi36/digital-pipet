from pymycobot.mycobot import MyCobot
import serial
import tkinter as tk
import time

# 初始化 MyCobot
mc = MyCobot('/dev/ttyAMA0', 1000000)

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(1)

angles_list = {
    'ini': [0, 0, 0, 0, 0, 0],
    'TFA_up': [26,(-20),(-35),76,(-17),(0)],
    'TFA': [27.07,(-58.5),(-35),90,(-38.19),(-1.5)],
    'plate_up': [-60, 0, -41, 70, 0, 0],
    'A1': [(-57.3),(-19),(-36.5),64,(-56.5),0],
    'B1': [(-54.8),(-19),(-36.5),64,(-56.2),0],
    'C1': [(-53.5),(-19),(-36.5),64,(-54.5),0],
    'D1': [(-51),(-19),(-36.5),64,(-53.5),0],
    'E1': [(-49.2),(-19),(-36.5),64,(-52.2),0],
    'F1': [(-47.5),(-19),(-36.5),64,(-49),0],
    'G1': [(-49),(-19),(-36.5),64,(-40.5),0],
    'H1': [(-50.5),(-19),(-36.5),64,(-30),0],
    
    'A2': [(-54),(-19),(-36.5),64,(-69.8),0],
    'B2': [(-51),(-19),(-36.5),64,(-68.8),0],
    'C2': [(-48.4),(-19),(-36.5),64,(-70.5),0],
    'D2': [(-46.4),(-19),(-36.5),64,(-66.9),0],
    'E2': [(-44),(-19),(-36.5),64,(-68),0],
    'F2': [(-42.5),(-19),(-36.5),64,(-66.6),0],
    'G2': [(-41),(-19),(-36.5),64,(-63.3),0],
    'H2': [(-40.5),(-19),(-36.5),64,(-57),0],
    
    'A3': [(-50.7),(-19),(-36.5),62,(-77.5),0],
    'B3': [(-47.7),(-19),(-36.5),62,(-74.5),0],
    'C3': [(-45.5),(-19),(-36.5),62,(-74),0],
    'D3': [(-42.8),(-19),(-36.5),62,(-74),0],
    'E3': [(-41),(-19),(-36.5),62,(-72),0],
    'F3': [(-39.5),(-19),(-36.5),62,(-69.5),0],
    'G3': [(-37),(-19),(-36.5),62,(-69),0],
    'H3': [(-35.3),(-19),(-36.5),62,(-67),0],
    
    'A4': [(-48),(-19),(-36.5),62,(-88.5),0],
    'B4': [(-44.5),(-19),(-36.5),62,(-88.5),0],
    'C4': [(-42),(-19),(-36.5),62,(-87.5),0],
    'D4': [(-39.2),(-19),(-36.5),62,(-85.5),0],
    'E4': [(-37.5),(-19),(-36.5),62,(-85),0],
    'F4': [(-34.5),(-19),(-36.5),62,(-84.5),0],
    'G4': [(-33.2),(-19),(-36.5),62,(-81),0],
    'H4': [(-30.5),(-19),(-36.5),62,(-81),0],
    
    'A5': [(-45),(-19),(-36.5),62,(-99),0],
    'B5': [(-41.5),(-19),(-36.5),62,(-98),0],
    'C5': [(-38.5),(-19),(-36.5),62,(-98.5),0],
    'D5': [(-36.5),(-19),(-36.5),62,(-95),0],
    'E5': [(-33.4),(-19),(-36.5),62,(-96.5),0],
    'F5': [(-31.5),(-19),(-36.5),62,(-93),0],
    'G5': [(-29.3),(-19),(-36.5),62,(-92),0],
    'H5': [(-27.5),(-19),(-36.5),62,(-89.3),0],
    
    'A6': [(-43),(-19),(-36.5),62,(-109.5),0],
    'B6': [(-39.5),(-19),(-36.5),62,(-108),0],
    'C6': [(-36),(-19),(-36.5),62,(-108),0],
    'D6': [(-33.3),(-19),(-36.5),62,(-105),0],
    'E6': [(-31.5),(-19),(-36.5),62,(-102),0],
    'F6': [(-29),(-19),(-36.5),62,(-103),0],
    'G6': [(-27),(-19),(-36.5),62,(-102),0],
    'H6': [(-25),(-19),(-36.5),62,(-99),0],
    
    'A7': [(-41.5),(-19),(-36.5),62,(-116),0],
    'B7': [(-37.8),(-19),(-36.5),62,(-114),0],
    'C7': [(-34.3),(-19),(-36.5),62,(-114),0],
    'D7': [(-31.8),(-19),(-36.5),62,(-113),0],
    'E7': [(-28.5),(-19),(-36.5),62,(-112.5),0],
    'F7': [(-26.8),(-19),(-36.5),62,(-110),0],
    'G7': [(-23.8),(-19),(-36.5),62,(-110),0],
    'H7': [(-21.5),(-19),(-36.5),62,(-106.4),0],
    
    'A8': [(-39.5),(-18.5),(-36.5),62,(-125),0],
    'B8': [(-36),(-18.5),(-36.5),62,(-126),0],
    'C8': [(-32.5),(-18.5),(-36.5),62,(-126),0],
    'D8': [(-30),(-18.5),(-36.5),62,(-124),0],
    'E8': [(-26.5),(-18.5),(-36.5),62,(-122),0],
    'F8': [(-23.8),(-18.5),(-36.5),62,(-119),0],
    'G8': [(-21.2),(-18.5),(-36.5),62,(-121),0],
    'H8': [(-18.8),(-18.5),(-36.5),62,(-115),0],
   
    
    'A9': [(-39),(-20),(-36.5),62,(-133),0],
    'B9': [(-35),(-20),(-36.5),62,(-130),0],
    'C9': [(-31),(-20),(-36.5),62,(-129.5),0],
    'D9': [(-28),(-20),(-36.5),62,(-129),0],
    'E9': [(-25),(-20),(-36.5),62,(-126),0],
    'F9': [(-22),(-20),(-36.5),62,(-126),0],
    'G9': [(-19),(-20),(-36.5),62,(-124.5),0],
    'H9': [(-16.5),(-20),(-36.5),62,(-122.5),0],
    
    'A10': [(-39),(-20),(-36.5),62,(-139),0],
    'B10': [(-35),(-20),(-36.5),62,(-137.5),0],
    'C10': [(-31),(-20),(-36.5),62,(-137),0],
    'D10': [(-27.3),(-20),(-36.5),62,(-137.5),0],
    'E10': [(-23.5),(-20),(-36.5),62,(-135.5),0],
    'F10': [(-20),(-20),(-36.5),62,(-135),0],
    'G10': [(-17),(-20),(-36.5),62,(-131),0],
    'H10': [(-14),(-20),(-36.5),62,(-129.5),0],
    
    'A11': [(-39.5),(-19),(-36.5),62,(-146),0],
    'B11': [(-35),(-19),(-36.5),62,(-146),0],
    'C11': [(-30.8),(-19),(-36.5),62,(-145),0],
    'D11': [(-26.5),(-19),(-36.5),62,(-145),0],
    'E11': [(-22.4),(-19),(-36.5),62,(-142),0],
    'F11': [(-19.5),(-19),(-36.5),62,(-140),0],
    'G11': [(-15.8),(-19),(-36.5),62,(-138),0],
    'H11': [(-12.5),(-19),(-36.5),62,(-136.5),0],
    
    'A12': [(-39),(-19),(-36.5),62,(-151),0],
    'B12': [(-33.5),(-19),(-36.5),62,(-150.5),0],
    'C12': [(-29.5),(-19),(-36.5),62,(-149.5),0],
    'D12': [(-25.8),(-19),(-36.5),62,(-149),0],
    'E12': [(-21.8),(-19),(-36.5),62,(-148),0],
    'F12': [(-17.5),(-19),(-36.5),62,(-146),0],
    'G12': [(-14),(-19),(-36.5),62,(-145),0],
    'H12': [(-10.4),(-19),(-36.5),62,(-142),0]
    
    # More coords need to be added as A2, A3...
}

# Length that corresponds to each volume
len_0mL = 1820
len_1mL = 1755
len_5mL = 1528
len_10mL = 1286

volume_list = {
   '150uL' : 7,
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
    
# 创建主窗口
root = tk.Tk()
root.title("Liquid Transfer System")

# 函数：全选所有选项
def select_all():
    for _, var in hole_checkboxes:
        var.set(True)

# 函数：取消全选所有选项
def deselect_all():
    for _, var in hole_checkboxes:
        var.set(False)
# Function to select all checkboxes in a column
def select_column(column_index):
    for i in range(column_index * 8, (column_index + 1) * 8):
        hole_checkboxes[i][1].set(True)

# Function to deselect all checkboxes in a column
def deselect_column(column_index):
    for i in range(column_index * 8, (column_index + 1) * 8):
        hole_checkboxes[i][1].set(False)
        
# 添加全选和取消全选按钮
select_all_button = tk.Button(root, text="Select All", command=select_all)
select_all_button.grid(row=3, column=1, padx=5, pady=5)

deselect_all_button = tk.Button(root, text="Deselect All", command=deselect_all)
deselect_all_button.grid(row=4, column=1, padx=5, pady=5)

# 用于存储选中的孔位
selected_holes = []

# 创建96个复选框模拟96孔板
hole_checkboxes = []
for i in range(12):
    column_frame = tk.Frame(root)
    column_frame.grid(row=0, column=(i+2), padx=5, pady=5)
    for j in range(8):
        hole = f"{chr(65+j)}{i+1}"  # 构建孔位标识，例如 A1, B1, ..., H12
        var = tk.BooleanVar()
        checkbox = tk.Checkbutton(column_frame, text=hole, variable=var)
        checkbox.pack(side=tk.TOP, padx=5)
        hole_checkboxes.append((hole, var))

    # Add Check All and Uncheck All buttons for each column
    uncheck_button = tk.Button(column_frame, text="-", command=lambda col=i: deselect_column(col))
    uncheck_button.pack(side=tk.BOTTOM, padx=5)
    check_button = tk.Button(column_frame, text="+", command=lambda col=i: select_column(col))
    check_button.pack(side=tk.BOTTOM, padx=5)
    
def transfer_liquid():

    if selected_holes:
        transfer_sequence = [
            {'volume': '300uL', 'wait_time': 1800},  # 300uL, 30分钟
            {'volume': '150uL', 'wait_time': 1800},  # 150uL, 30分钟
            {'volume': '150uL', 'wait_time': 1800},  # 150uL, 30分钟
            {'volume': '150uL', 'wait_time': 5400},  # 150uL, 90分钟
            {'volume': '150uL', 'wait_time': 0}      # 150uL, 无等待时间
        ]
        
        for round_num, round_data in enumerate(transfer_sequence, start=1):
            volume = round_data['volume']
            wait_time = round_data['wait_time']
            print(f"Starting round {round_num} - Adding {volume} and waiting {wait_time/60} mintues...")
            
            for hole in selected_holes:       
                dispense_liquid(volume, hole) 
            
            empty_pump()
            if wait_time > 0:
               print("Waiting...")
               time.sleep(wait_time)
            
            print(f"Round {round_num} completed.")
            
            
    else:
        print("Please select at least one hole and a volume.")


# 添加液体转移按钮
transfer_button = tk.Button(root, text="TFA cleavage cocktail Transfer", command=transfer_liquid)
transfer_button.grid(row=13, columnspan=1, pady=5)

# 在复选框状态改变时更新选中的孔位列表
def update_selected_holes():
    selected_holes.clear()
    for hole, var in hole_checkboxes:
        if var.get():
            selected_holes.append(hole)

# 绑定复选框状态变化事件
for _, var in hole_checkboxes:
    var.trace("w", lambda *args, var=var: update_selected_holes())

# 运行主循环
root.mainloop()
