import time

import pyautogui

count = 5
print('Rady started go')

for i in range(count):
    print(count)
    time.sleep(1)
    count = count - 1
    
for i in range(20):
    pyautogui.typewrite('Only For Education Purpose!')
    pyautogui.press('enter')
    time.sleep(2)

