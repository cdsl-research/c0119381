import utime
from machine import I2C,Pin
from vl53l1x import VL53L1X
import urequests


def httpPost(timeV1,distanceV1):
    url = 'http://192.168.100.144/receive/yamamoto_post.php?'

    url += "time=" + str(timeV1) + "&distance="+ str(distanceV1)
    #print(url)
    res = urequests.get(url)
    
    print("\r"+str(res.status_code),end="")
    res.close()

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
    print("range: cm ", dist)
    utime.sleep(0.1)
    distanceList.append(dist)


utime.sleep(2)
print("Wi-Fi接続開始")
wifi = connect_wifi(SSID_NAME, SSID_PASS)

utime.sleep(1)
print("送信処理開始")
timeV = 0
splitTime = 0.1 #データの取得間隔
for di in distanceList:
    httpPost(timeV,di)
    timeV += splitTime
    utime.sleep(0.1)

f=open("list4.csv","w")
f.close()
for d in distanceList:
    f=open("list4.csv","a")
    f.write(str(d)+"\n")
    f.close()
print("書き込み完了")
