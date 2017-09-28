t=int(input("what is the time now?"))
w=int(input("number of hours to wait"))
alarmtime=(w%24)+t
alarmtime=alarmtime%24
print(alarmtime)
