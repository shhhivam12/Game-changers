import serial
import time

ArduinoSerial = serial.Serial('COM3',9600) 
f = open("nemadata.txt", "a")
c=0
starttime = time.time()
# print('hhh')
while(True):
    curtime = time.time() - starttime
    b = ArduinoSerial.readline()
    
    s1 =  b.decode().strip() # convert to string
    # nemasentence = s1.split(',')
    print(b)
    # f.writelines(nemasentence)

    # if(nemasentence[0] == '$GPGLL'):
    #     c+=1
    #     print('--------------------------------')
    #     print(nemasentence)
    #     print("")
    #     print(f'time - {curtime}')
    #     print(f'count - {c}')
    #     print(len(nemasentence))
    #     print('--------------------------------')



ArduinoSerial.close()

