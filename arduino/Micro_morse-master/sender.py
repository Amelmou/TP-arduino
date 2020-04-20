import keyboard
import time
import serial
arduino= serial.Serial('COM9',9600)
time.sleep(1)
while True:
	time.sleep(0.01)
	if keyboard.is_pressed('Space'):
		arduino.write('1'.encode())
	else:
		arduino.write('0'.encode())