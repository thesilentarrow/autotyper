import pyautogui
import time
import re

spaces = 0 
x=0
delay_speed = 0

def tabbing_mech(line):
    global x
    global spaces
    count_space = 0
    
    print('x:',x)
    if x==1:
        pyautogui.press('tab')
        print("xxxxxxxxxxxxx")
    for char in line:
         if char == " ":
            count_space += 1
         elif char == "\t":
            count_space += 4
         else:
            break
    print(count_space, spaces, line)
    
    
    if spaces > count_space:
        back_tab = (spaces - count_space) // 4 
        spaces = count_space
        print("tab back")
        for i in range(back_tab):
            pyautogui.keyDown('shift')
            pyautogui.press('tab')
            pyautogui.keyUp('shift')
        return line.lstrip()
    elif count_space == 0:
        return line
    elif spaces == count_space:
        return line.lstrip()
    elif spaces < count_space:
        print("indenting")
        spaces = count_space
        return line.lstrip()

 
for i in range(8): 
    time.sleep(1)
    print(i)

with open("code.txt", 'r') as f:
    for lines in f:  
        if not lines.strip():
            print("empty line")
            continue
        else:
            lines = re.sub(r'#.*', '', lines)
            if not lines.strip():
                print("empty line")
                continue 
            type_me = tabbing_mech(lines) #Used for IDEs
            pyautogui.typewrite(type_me, delay_speed)
            lines1=lines.rstrip()+'\n'
            if 'break' in lines1 or 'return\n' in lines1:
                x=1
            else:
                x=0

        