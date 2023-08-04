from datetime import datetime

from playsound import playsound

alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print(alarm_period)
print(f"Setting up alarm..at{alarm_hour}hr, {alarm_minute}min, {alarm_seconds}sec")
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    # print(current_hour)
    if alarm_period == current_period:
        # print('insdie if')
        if alarm_hour == current_hour:
            # print(current_hour)
            if alarm_minute == current_minute:
                if alarm_seconds == current_seconds:
                    print("Wake Up!")
                    playsound('alarm.mp3')
                    break

# input format -  12:50:00 PM
