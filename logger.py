import serial
import time
import binascii
import binascii

import matplotlib.pyplot as plt

key=""
time_log=[]
data_log=[[],[],[],[],[]]
log=[]

imu_port="COM8"
file_name="IMU"+ str(time.time()).replace(".","_")+".csv"

try:
    imu = serial.Serial(port=imu_port,baudrate=9600)
    print(imu )
except Exception as e:
    print(e)


print("connected to: " + imu.portstr)

def router(msg):
    global key
    key= msg.name
    print(msg.name)
    pass

kb.on_press(router)

f = open(file_name,"w+")

def drew(data):
    plt.subplot(3, 2, 1)
    plt.plot(data_log[1],'yo-')
    plt.xlabel('Time(ms)')
    plt.ylabel('Acc x')
    plt.pause(0.00001)
    pass

def decode(row):

    str_t = row.decode()
    str_t=str_t.split(";")
    save(str_t[0])
    data=str_t[0].split(" ")
    print(data)
    return data
    pass

def save(data):

    f.write(str(data))
    f.write("\n")
    pass



while True:


    try:
        row=imu.readline()
        data=decode(row)
        #bdrew(data)
        pass
    except Exception as e:
        print(e)

if key=="b":

    f.close()


