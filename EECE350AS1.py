import socket
from time import ctime

def converttime(timeinstring):
    #converts time from hh:mm:ss to hours, minutes, seconds
    hourstemp = int(timeinstring[:2])
    minutestemp = int(timeinstring[3:5])
    secondstemp = int(timeinstring[6:9])
    return (hourstemp,minutestemp,secondstemp)

def deducttime(hour1,hour2,minute1,minute2,second1,second2):
    totalseconds1 = hour1*3600 + minute1*60 + second1
    totalseconds2 = hour2*3600 + minute2*60 + second2
    difference = abs(totalseconds1-totalseconds2)
    hours = difference//3600
    minutes = (difference - hours*3600)//60
    seconds = (difference - hours*3600 - minutes*60)
    print("There is a {} hours, {} minutes, and {} seconds difference between time1 and time2.".format(hours,minutes,seconds))

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("time-c.nist.gov",13))

while True:
    data = mysock.recv(10000)
    if data:
        time = data.decode()
    else:
        break
mysock.close()

timelist = time.split()
currenttime=timelist[2]
currenttimetup = converttime(currenttime)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("time-c.nist.gov",13))

while True:
    data = mysock.recv(10000)
    if data:
        time2 = data.decode()
    else:
        break
mysock.close()

timelist2 = time2.split()
currenttime2=timelist2[2]
currenttime2tup = converttime(currenttime2)
print(currenttimetup,currenttime2tup)
