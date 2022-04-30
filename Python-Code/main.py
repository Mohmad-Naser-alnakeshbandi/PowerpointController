import serial
import pyautogui
ser = serial.Serial('COM5',9600)
ser.flushInput()
while True:
        ser_data = ser.readline()
        data = chr(ser_data[0])
        print(data)
        if data == "R":
                pyautogui.press('right')
        if data == "L":
                pyautogui.press('left')



