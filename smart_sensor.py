import serial
import pymysql
from time import localtime, strftime

lastTime = 0
T = serial.Serial(port='COM5', baudrate=9600)



while True:
    strDate = strftime("%Y-%m-%d", localtime())
    strTime = strftime("%H:%M:%S", localtime())    
    strTemp3 = T.readline().decode()    
    # id=strDate+" "+strTime
    print(strTemp3)
    strTemp = strTemp3.replace("\n","")
    strTemp2 = strTemp.split()
    print(strTemp2)

    
    
    # strTemp = strTemp.replace("\n","")
    # strTemp = strTemp.split()
    # strHumi = strTemp[1]
    # strTemp = strTemp[0]

    # [온도, 습도, 온도]
    soil_moisture = strTemp2[5];
    light_brightness = strTemp2[7];
    temperature = strTemp2[3];
    humidity = strTemp2[1];
    print(soil_moisture)
    print(light_brightness)
    print(temperature)
    print(humidity)
    

    # if lastTime != strTime:
    #     lastTime = strTime
        
    db = pymysql.connect(host='localhost', user='root', passwd = 'root', db='smart_farm',port=13306)
    
        
    with db:
        cur = db.cursor()
        cur.execute("INSERT INTO weather(humidity,temperature,soil_moisture, light_brightness) VALUES (%s, %s, %s, %s)", (humidity, temperature, soil_moisture, light_brightness))
        db.commit()

