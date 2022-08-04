from unittest import result
from flask import Flask, jsonify, request
from sqlalchemy import create_engine, text

app = Flask(__name__)


database = create_engine("mysql+mysqlconnector://root:root@localhost:13306/smart_farm?charset=utf8", encoding = 'utf-8')
app.database = database

@app.route('/FARM/MONITORING/HUMIDITY', methods = ['GET'])
def humidity():
    result=""
    humidity = app.database.execute("SELECT humidity FROM weather order by id desc LIMIT 1")
    for row in humidity:
        print("humidity:", row['humidity'])
        result=row['humidity']
    return result

@app.route('/FARM/MONITORING/TEMPERATURE', methods = ['GET'])
def temperature():
    result=""
    temperature = app.database.execute("SELECT temperature FROM weather order by id desc LIMIT 1")
    for row in temperature:
        print("temperature:", row['temperature'])
        result=row['temperature']
    return result

@app.route('/FARM/MONITORING/LIGHT_BRIGHTNESS', methods = ['GET'])
def light_brightness():
    result=""
    light_brightness = app.database.execute("SELECT light_brightness FROM weather order by id desc LIMIT 1")
    for row in light_brightness:
        print("light_brightness:", row['light_brightness'])
        result=row['light_brightness']
    return result

@app.route('/FARM/MONITORING/SOIL_MOISTURE', methods = ['GET'])
def soil_moisture():    
    result=""
    soil_moisture = app.database.execute("SELECT soil_moisture FROM weather order by id desc LIMIT 1")
    for row in soil_moisture:
        print("soil_moisture:", row['soil_moisture'])
        result=row['soil_moisture']
    return result

@app.route('/FARM/CONTROL/WIND', methods = ['GET'])
def wind():
    return "wind"

@app.route('/FARM/CONTROL/WATER', methods = ['GET'])
def water():
    return "water"

@app.route('/FARM/CONTROL/LIGHT', methods = ['GET'])
def light():
    return "light"

@app.route('/FARM/LOGIN', methods = ['GET'])
def login():
    return "login"

app.run(host="192.168.0.124", port=5000, debug=True)
