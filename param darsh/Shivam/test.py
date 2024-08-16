import flask as F
import serial
import json

app = F.Flask(__name__)
@app.route("/")
def Hello():
    gpsdata = getData()
    return json.dumps(gpsdata)

def getData():
    c=0
    ArduinoSerial = serial.Serial('COM3',9600) 
    while(c<20):
        # data={'latitude':'10970.776','longitude':'868788775.898786'}
        # print(data)
        # return data
        c+=1
        b = ArduinoSerial.readline()
        print('1')
        print(b)
        b = ArduinoSerial.readline()
        print('2')
        print(b)
        s1 =  b.decode().strip() # convert to string
        nemasentence = s1.split(',')
        if(nemasentence[0] == '$GPGLL'):
            data={'latitude':nemasentence[1],'longitude':nemasentence[3]}
            print(data)
            return data
        


if __name__=='__main__':
    app.run()


