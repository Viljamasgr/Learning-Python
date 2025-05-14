# Python date & time

import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today()

time = datetime.time(12, 30, 0)
now = datetime.datetime.now()

now =  now.strftime("%H:%M:%S %m-%d-%Y")

target_datetime = datetime.datetime(2030, 1, 3, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has not passed")