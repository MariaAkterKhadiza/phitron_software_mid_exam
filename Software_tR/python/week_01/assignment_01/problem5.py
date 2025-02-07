import pyautogui
import time


def draw_pyramid(num_rows):
    for i in range(1, num_rows + 1):
        for j in range(i):
            pyautogui.typewrite("#")
        pyautogui.press('enter')
        time.sleep(0.1)  


num_rows = int(input("Enter the number of rows: "))
draw_pyramid(num_rows)