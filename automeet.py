##Google meet automation using the "AutoMeet library".
from lib.AutoMeet import AutoMeet
import time
import datetime

getTime = str(datetime.datetime.today().time())
currentTime = getTime[:2] + getTime[3:5]
getDay = int(datetime.datetime.today().weekday())


times = [[1000, 1100], [1110, 1210], [1220, 1320]]
ack = [False,False,False]

usrname = "ur email Id"
passwrd = "ur pass"
LEC1 = "google meet link" #lecture1
LEC2 = "google meet link" #lecture2
LEC3 = "google meet link" #lecture3
LEC4 = "google meet link" #lecture4
LEC5 = "google meet link" #lecture5
#Add according to the number of lectures
monday = [LEC1, LEC2, LEC3]
tuesday = [LEC2, LEC1, LEC3]
wednersday = [LEC1, LEC2, LEC3]
thursday = [LEC3, LEC1, LEC2]
friday = [LEC2, LEC3, LEC1]

days = [monday, tuesday, wednersday, thursday, friday,saturday]




while True:
    getTime = str(datetime.datetime.today().time())
    currentTime = int(getTime[:2] + getTime[3:5])

    day = days[getDay]
    # print(day)
    for i in range(len(times)):
        if times[i][0] <= currentTime < times[i][1]:
            print(day[i])
            if not ack[i]:
                auto = AutoMeet(usrname,passwrd,"{}".format(day[i]))
                auto.automeetX()
                ack[i] = True

    print("HOLD")
    time.sleep(30)

