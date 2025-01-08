#!/usr/bin/python3
import time
import serial

print("UART Demonstration Program")
print("NVIDIA Jetson Nano Developer Kit")
#https://jetsonhacks.com/2019/10/10/jetson-nano-uart/
#TODO: Make some kind of system for communicating non text stuff
#eg
#Whether the line being sent is for translated or transcripted
#^l for translated
#^c for transcripted
#/n for when the line is done
#Maybe some other system for live updating the same label vs new label. ^n for new label?
#See ^? -> If n is next, new label. Then, check after if l or c and place accordingly. If not n? Check if l or c and place accordingly but for replacing the same label. If neither idk
#try it out

serial_port = serial.Serial(
    port="/dev/ttyTHS1",
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)
# Wait a second to let the port initialize
time.sleep(1)
#Test cases
#1: Keep updating the same label
#2: Make new labels
#3: Send both translated and transcripted
#


test_case = 1

try:
    # Send a simple header
    serial_port.write("UART Demonstration Program\r\n".encode())
    serial_port.write("NVIDIA Jetson Nano Developer Kit\r\n".encode())
    while True:
        if (test_case == 1):
            i = 0
            if serial_port.inWaiting() > 0:
                serial_port.write("^lTest case 1. Num here shld increase {}\n".format(i).encode())
                i = i + 1
                time.sleep(1)
        elif (test_case == 2):
            i = 0
            if serial_port.inWaiting() > 0:
                serial_port.write("^n^lTest case 1. Num here shld increase {}\n".format(i).encode())
                i = i + 1
                time.sleep(1)
        elif (test_case == 3):
            i = 0
            if serial_port.inWaiting() > 0:
                tort = "^l"
                if (i%2 == 0):
                    tort = "^c"
                else:
                    tort = "^l"
                serial_port.write("^n{}Test case 1. Num here shld increase {}\n".format(tort,i).encode())
                i = i + 1
                time.sleep(1)



except KeyboardInterrupt:
    print("Exiting Program")

except Exception as exception_error:
    print("Error occurred. Exiting Program")
    print("Error: " + str(exception_error))

finally:
    serial_port.close()
    pass
