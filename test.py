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
    'plate_up': [-60, 0, -41, 70, -70, 0],
    'A1': [(-57),(-21),(-36.5),64,(-54.5),0],
    'B1': [(-54.7),(-21),(-36.5),64,(-54.5),0],
    'C1': [(-52.7),(-21),(-36.5),64,(-54.5),0],
    'D1': [(-50.7),(-21),(-36.5),64,(-53.5),0],
    'E1': [(-48.5),(-21),(-36.5),64,(-52.2),0],
    'F1': [(-48),(-21),(-36.5),64,(-48.5),0],
    'G1': [(-47.5),(-21),(-36.5),64,(-42.5),0],
    'H1': [(-49),(-21),(-36.5),64,(-32),0],
    
    'A2': [(-53),(-21),(-36.5),64,(-69),0],
    'B2': [(-51.5),(-21),(-36.5),64,(-68),0],
    'C2': [(-47.5),(-21),(-36.5),64,(-68),0],
    'D2': [(-46),(-21),(-36.5),64,(-68),0],
    'E2': [(-43),(-21),(-36.5),64,(-68.5),0],
    'F2': [(-41.5),(-21),(-36.5),64,(-66.5),0],
    'G2': [(-40.5),(-21),(-36.5),64,(-63),0],
    'H2': [(-38.5),(-21),(-36.5),64,(-62),0],
    
    'A3': [(-50),(-20),(-36.5),62,(-76),0],
    'B3': [(-47),(-20),(-36.5),62,(-76),0],
    'C3': [(-44.5),(-20),(-36.5),62,(-76),0],
    'D3': [(-42),(-20),(-36.5),62,(-76),0],
    'E3': [(-39.4),(-20),(-36.5),62,(-76),0],
    'F3': [(-37.5),(-20),(-36.5),62,(-74),0],
    'G3': [(-35),(-20),(-36.5),62,(-74),0],
    'H3': [(-34),(-20),(-36.5),62,(-71),0],
    
    'A4': [(-46.5),(-20),(-36.5),62,(-87),0],
    'B4': [(-43.5),(-20),(-36.5),62,(-87),0],
    'C4': [(-41),(-20),(-36.5),62,(-87),0],
    'D4': [(-38.7),(-20),(-36.5),62,(-86.5),0],
    'E4': [(-36),(-20),(-36.5),62,(-87.5),0],
    'F4': [(-33.5),(-20),(-36.5),62,(-83.5),0],
    'G4': [(-32),(-20),(-36.5),62,(-82.5),0],
    'H4': [(-30),(-20),(-36.5),62,(-81),0],
    
    'A5': [(-44),(-19),(-36.5),62,(-99),0],
    'B5': [(-41.5),(-19),(-36.5),62,(-96),0],
    'C5': [(-38.5),(-19),(-36.5),62,(-96),0],
    'D5': [(-35.5),(-19),(-36.5),62,(-96),0],
    'E5': [(-33),(-19),(-36.5),62,(-95),0],
    'F5': [(-30.5),(-19),(-36.5),62,(-95),0],
    'G5': [(-28.3),(-19),(-36.5),62,(-93),0],
    'H5': [(-26.5),(-19),(-36.5),62,(-91.5),0],
    
    'A6': [(-42.5),(-19),(-36.5),62,(-106),0],
    'B6': [(-39),(-19),(-36.5),62,(-106),0],
    'C6': [(-36),(-19),(-36.5),62,(-106),0],
    'D6': [(-33),(-19),(-36.5),62,(-106),0],
    'E6': [(-30.5),(-19),(-36.5),62,(-104),0],
    'F6': [(-28),(-19),(-36.5),62,(-102),0],
    'G6': [(-25.5),(-19),(-36.5),62,(-102),0],
    'H6': [(-23),(-19),(-36.5),62,(-101),0],
    
    'A7': [(-40.5),(-19),(-36.5),62,(-114),0],
    'B7': [(-36.5),(-19),(-36.5),62,(-114),0],
    'C7': [(-33.5),(-19),(-36.5),62,(-114),0],
    'D7': [(-31),(-19),(-36.5),62,(-113),0],
    'E7': [(-28),(-19),(-36.5),62,(-113),0],
    'F7': [(-25.5),(-19),(-36.5),62,(-111),0],
    'G7': [(-23),(-19),(-36.5),62,(-110),0],
    'H7': [(-20),(-19),(-36.5),62,(-109),0],
    
    'A8': [(-38.5),(-19),(-36.5),62,(-121),0],
    'B8': [(-35),(-19),(-36.5),62,(-121),0],
    'C8': [(-31.5),(-19),(-36.5),62,(-121),0],
    'D8': [(-28.5),(-19),(-36.5),62,(-121),0],
    'E8': [(-25.5),(-19),(-36.5),62,(-120),0],
    'F8': [(-23),(-19),(-36.5),62,(-118),0],
    'G8': [(-20),(-19),(-36.5),62,(-118),0],
    'H8': [(-18),(-19),(-36.5),62,(-116),0],
   
    
    'A9': [(-37),(-20),(-36.5),62,(-127),0],
    'B9': [(-33.5),(-20),(-36.5),62,(-127),0],
    'C9': [(-30),(-20),(-36.5),62,(-127),0],
    'D9': [(-27),(-20),(-36.5),62,(-127),0],
    'E9': [(-24),(-20),(-36.5),62,(-126),0],
    'F9': [(-20.5),(-20),(-36.5),62,(-126),0],
    'G9': [(-17.5),(-20),(-36.5),62,(-124),0],
    'H9': [(-15.5),(-20),(-36.5),62,(-122),0],
    
    'A10': [(-36.5),(-20),(-36.5),62,(-134),0],
    'B10': [(-32.5),(-20),(-36.5),62,(-134),0],
    'C10': [(-29),(-20),(-36.5),62,(-134),0],
    'D10': [(-26),(-20),(-36.5),62,(-133),0],
    'E10': [(-23),(-20),(-36.5),62,(-131),0],
    'F10': [(-19.5),(-20),(-36.5),62,(-131),0],
    'G10': [(-16.5),(-20),(-36.5),62,(-130),0],
    'H10': [(-13),(-20),(-36.5),62,(-128),0],
    
    #colume11 and 12 are not fine tuned yet
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


# Function to perform MyCobot movement
def move_mycobot(angles, speed, wait_time):
    mc.send_angles(angles, speed)
    time.sleep(wait_time)




# Function to dispense liquid
def dispense_liquid(position):

    move_mycobot(angles_list['plate_up'], 20, 3)
    move_mycobot(angles_list[position], 20, 2)
    time.sleep(6)
    move_mycobot(angles_list['plate_up'], 20, 3)
    move_mycobot(angles_list['ini'], 20, 3)
   





    


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


# 添加按钮来完成液体转移功能
def transfer_liquid():
   
          
    for hole in selected_holes:
        dispense_liquid(hole)
           



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
    
    


# 添加液体转移按钮
transfer_button = tk.Button(root, text="Liquid Transfer", command=transfer_liquid)
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





