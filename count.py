import time
from machine import I2C,Pin
from vl53l1x import VL53L1X
from time import sleep
import utime

""" パラメータ """
# i2c関係
I2C_SCL_PIN = 22
I2C_SDA_PIN = 21
""" パラメータ(終わり) """
i2c = I2C(scl=Pin(I2C_SCL_PIN), sda=Pin(I2C_SDA_PIN))

distance = VL53L1X(i2c) 

distanceList = list()
#while True:
for i in range(100):
    dist = distance.read()                
    if dist<=120:
        num = num + 1
        print(f"{dist}")
        utime.sleep_ms(400)
    else:
        pass

    print("range: cm ", dist)
    time.sleep_ms(100)
    distanceList.append(dist)

f=open("list4.csv","w")
f.close()
for d in distanceList:
    f=open("list4.csv","a")
    f.write(str(d)+"\n")
    f.close()
print("書き込み完了")
