from os import system
import time
import datetime
import pygame
import keyboard

sound_file = "alarm-clock-90867.mp3"

def play_alarm():
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)            
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

def alarm():
    system('cls')
    isRunning = True
    print("Press 'q' to return to menu, or 'esc' to exit the program")
    alarm_time = input("Enter the alarm (HH:MM:SS): ")
    while isRunning:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, end='\r')
        
        if(current_time == alarm_time):
            print("WAKE UP!!!")
            play_alarm()
            isRunning = False
            
        if keyboard.is_pressed('q'):
                if pygame.mixer.init() and pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                isRunning = False
                startUpMenu()
            
        if keyboard.is_pressed('esc'):
                if pygame.mixer.init() and pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                isRunning = False
                exit()
    
    startUpMenu()


def show_time():
    system('cls')
    isRunning = True
    print("Press 'q' to return to menu, or 'esc' to exit the program")
    while isRunning:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, end='\r')
        
        if keyboard.is_pressed('q'):
            isRunning = False
            startUpMenu()
        
        if keyboard.is_pressed('esc'):
            isRunning = False
            exit()


def stopwatch():
    system('cls')
    print("Press 's' to start/stop stopwatch, 'r' to reset, 'q' to return to menu, or 'esc' to exit the program")
    isRunning = False
    start_time = time.time()
    elapsed_time = 0
    
    while True:
        if isRunning:
            elapsed_time = time.time() - start_time
        print(f"{int(elapsed_time // 3600):02}:{int((elapsed_time % 3600) // 60):02}:{int(elapsed_time % 60):02}", end='\r')
        if keyboard.is_pressed('s'):
            isRunning = not isRunning
            start_time = time.time() - elapsed_time
        if keyboard.is_pressed('r'):
            elapsed_time = 0
            start_time = time.time()
            isRunning = False
        if keyboard.is_pressed('q'): 
            isRunning = False
            startUpMenu()
        if keyboard.is_pressed('esc'):
            exit()
                      
    
def timer():
    system('cls')
    print("Press 'q' to return to menu, or 'esc' to exit the program")
    seconds = int(input("Enter the time in seconds: "))
    while seconds <= 0:
        print("Please enter a positive integer for seconds.")
        seconds = int(input("Enter the time in seconds: "))
    isRunning = True
    end_time = time.time() + seconds
    
    while isRunning:
        remaining_time = int(end_time - time.time())
        if remaining_time <= 0:
            print("Time's up!")
            play_alarm()
            isRunning = False
            startUpMenu()
        
        mins, secs = divmod(remaining_time, 60)
        hours, mins = divmod(mins, 60)
        print(f"{hours:02}:{mins:02}:{secs:02}", end='\r')
        
        if keyboard.is_pressed('q'):
            isRunning = False
            startUpMenu()
        
        if keyboard.is_pressed('esc'):
            isRunning = False
            exit()
        
def startUpMenu():
    system('cls')
    print("Welcome to Clock")
    print("What would you like to do?")
    print("1. Set an alarm")
    print("2. Show current time")
    print("3. Stopwatch")
    print("4. Timer")
    print("5. Exit")
    choice = int(input("Enter your choice (1 - 5): "))
    
    if choice == 1:
        alarm()
    elif choice == 2:
        show_time() 
    elif choice == 3:
        stopwatch()
    elif choice == 4:
        timer() 
    elif choice == 5:
        print("Exiting the program.")
        exit()

startUpMenu()