import time
import datetime
import pygame

sound_file = "AlarmClock/alarm-clock-90867.mp3"

def alarm(alarm_time):
    isRunning = True
    while isRunning:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, end='\r')
        
        if(current_time == alarm_time):
            print("WAKE UP!!!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)            
            pygame.mixer.music.play()
            isRunning = False
            while pygame.mixer.music.get_busy():
                time.sleep(1)
                
        time.sleep(1)


print("Welcome to Clock")
print("What would you like to do?")
print("1. Set an alarm")
print("2. Show current time")
print("3. Stopwatch")
print("4. Timer")
print("5. Exit")
choice = int(input("Enter your choice (1 - 5): "))

if choice == 1:
    alarm_time = input("Enter the alarm (HH:MM:SS): ")
    alarm(alarm_time)
