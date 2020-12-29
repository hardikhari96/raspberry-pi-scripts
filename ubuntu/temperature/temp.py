import os
import time

log = ""
f = open("templog.txt","a+")
def measure_temp():
    temp = int(os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline())
    log = "temp = "+str((temp/1000))+" °C"
    f.write(str(temp/1000) +"\r\n")
    return log
while True:
    print(measure_temp())
    time.sleep(3)
f.close()
