import psutil
import time
import os
import re
import pyttsx3
from nvidia_smi import nvmlInit, NVMLError, nvmlDeviceGetHandleByIndex, nvmlDeviceGetTemperature, NVML_TEMPERATURE_GPU

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[16].id)

def play_audio(temperature):
    engine.say('Get out, it is gonna blow. Temperature is ' + temperature + " °Celsius")
    engine.runAndWait()

def sendmessage(message):
    os.system('notify-send "{}" "{}"'.format("Temperature Warning", message))

def connect_gpu():
    try:
        nvmlInit()
        return 1
    except:
        return None

def get_gpu_temp():
    try:
        nvmlInit()
        gpu = nvmlDeviceGetHandleByIndex(0)
        gpu_temp = nvmlDeviceGetTemperature(gpu, NVML_TEMPERATURE_GPU)
        return gpu_temp
    except NVMLError:
        return None

def temp_check():
    hot = 0
    data = psutil.sensors_temperatures()
    temperatures = re.findall("current=[0-9]{0,3}\.[0-9]", str(data['coretemp']))
    for i, t in enumerate(temperatures):
        temperatures[i] = float(t[8:])
        hot = max(temperatures[i], hot)
    gpu_temp = get_gpu_temp()
    if gpu_temp:
        hot = max(hot, gpu_temp)
        temperatures.append("gpu: "  + str(gpu_temp))
    if hot > 80 and hot < 98:
        sendmessage("Be carefull one of the cpu cores is " + str(hot))
    elif hot >= 98: 
        sendmessage("Turn it off, or it is gonna blow, " + str(hot))
        play_audio()
    print(temperatures)

try:
    while(True):
        temp_check()
        time.sleep(60)
except KeyboardInterrupt:
    print("Lets stop it boys")
