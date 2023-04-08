import serial
arduino = serial.Serial('COM9', baudrate=9600, timeout=1)
import sys

def write_read(x):
    b = bytes(x, 'utf-8')
    print(b)
    arduino.write(b)
    print("pass")
    # if it doesn't get anything back in 1 second, then the timeout returns arduino.read()
    data = arduino.read()
    return data

def flashLight(label):
    drowsiness = '0' if label == "Awake" else '1'

    # while True:
    #     if drowsiness == 'quit':
    #         arduino.close()
    #         break
    try:
        value = write_read(drowsiness)
        print(drowsiness)
    except KeyboardInterrupt:
        print("\nCtrl+C pressed. Closing the connection.")
        arduino.close()
        sys.exit()

# while True:    
#     num = input("Enter a number: ") # Taking input from user
#     if (num == 'quit'):
#         arduino.close()
#         break
#     value = write_read(num)
#     print(value) # printing the value