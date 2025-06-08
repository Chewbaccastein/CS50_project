from time import localtime, sleep
import sys
import msvcrt
import re
import os
### menu function only works in Windows due to msvcrt module ###

class Clock:
    def __init__(self):
        self._hour = 0
        self._minute = 0
        self._second = 0
        self._last_sing_hour = -1
        self._last_display = " "
        # self._alarm_trigger = False
        
    def __str__(self):
        hour_12 = self._hour % 12
        if hour_12 == 0:
            hour_12 = 12
        return(f"{hour_12:02}:{self._minute:02}:{self._second:02} {self.am_pm()}")

    @property
    def hour(self):
        return self._hour
    @property
    def minute(self):
        return self._minute
    @property
    def second(self):
        return self._second
    
    def set_time(self, hour, minute, second):
        self._hour = hour
        self._minute = minute
        self._second = second
        self._last_sing_hour = -1
    
    def am_pm(self):
        if 0 <= self._hour < 12:
            return "AM"
        else:
            return "PM"
        
        
    def display_update(self):
    
        new_display = get_current_time()
        self.set_time(new_display.hour, new_display.minute, new_display.second)
    
        if new_display != self._last_display:
            sys.stdout.write("\r" + str(self).center(70))
            sys.stdout.flush()
            self._last_display = str(self)
        
        
    # triggers cuckoo sing at the top of hours.
    
        if new_display.minute == 0 and new_display.second == 0:
            self.cuckoo_sing()
           
    

    def cuckoo_sing(self): # cuckoo sings the number of hours, 12-hr clock based. quiet time is 8pm - 8am, (cuckoo does not sing during this period)
        if self._minute == 0 and self._second == 0 and self._last_sing_hour != self._hour:
            if 8 <= self._hour < 20:
                cuckoo_count = self._hour % 12 or 12
                for _ in range(cuckoo_count):
                    print("\nCuckoo!")
                    sleep(0.3)
            else:
                print("\n**cricket**") # Quite hour
                
            self._last_sing_hour = self._hour
        
        
        
        # self._current_time = get_current_time()
        # self._hour = self._current_time.hour % 12 or 12
        # if 8 <= self._current_time.hour < 20:
        #     for _ in range(self._hour):
        #         print("Cuckoo!")
        #         sleep(0.6)
        # else:
        #     print("**cricket**") # Quite hour
            
    # tick function to make test_mode clock function like a real clock.
    def tick(self): 
        self._second += 1
        if self._second >= 60:
            self._second = 0
            self._minute += 1
        if self._minute >= 60:
            self._minute = 0
            self._hour += 1
        if self._hour >= 24:
            self._hour = 0
    
    # zero_minute, zero_second = current_time.minute, current_time.second
    # numbers_sing = current_time.hour
    # if 8 <= numbers_sing < 13 and zero_minute == zero_second == 0:
    #     for _ in range(numbers_sing):
    #         print("Cuckoo!")
    #         sleep(0.5)
    # elif 12 < numbers_sing < 20 and zero_minute == zero_second == 0:
    #     for _ in range(24 - numbers_sing):
    #         print("Cuckoo!")
    #         sleep(0.5)
    # else:
    #     print("**cricket**") # Quiet hour





def main():
    header = """
    -----------------------------------------------------------------
    Menu: 1 = set alarm | 2 = cancel alarm | 3 = test mode | 4 = exit 
    -----------------------------------------------------------------
    """ 
    
    clock = Clock()
    redraw_screen = True  # to fix flashing when screan resets

    while True:
        if redraw_screen:
            os.system('cls')
            print(header,alarm_status()) 
            
            current_date = get_current_date()
            print(current_date.center(67))
            
            redraw_screen = False  # Reset flag

        clock.display_update()
        if alarm_cuckoo(clock):
            redraw_screen = True

        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'1':
                set_alarm()
                redraw_screen = True
            elif key == b'2':
                cancel_alarm()
                redraw_screen = True
            elif key == b'3':
                test_mode()
                redraw_screen = True
            elif key == b'4':
                print("\n>>>Exiting...")
                sys.exit()

        sleep(0.1)

    
    # clock = Clock()
    
    # while True:
    #     os.system('cls')
    #     print(header)
    #     current_date = get_current_date()
    #     print(current_date.center(67))
    #     clock.display_update()
    #     user_menu()
    #     sleep(0.1)
    
    # current_date = get_current_date()
    # print(current_date.center(67))
    # #display current time
    # while True:
    #     user_menu()
    #     clock.display_update()
    #     alarm_cuckoo(clock)
    #     sleep(0.1)
        
    
        
    #indicator = alram on/alram off
    ...
    #choices: set alarm, cancel alarm, test mode
    ...

def get_current_date():
    get_date = localtime()
    today_date = f'{get_date[1]:02}/{get_date[2]:02}/{get_date[0]:04}'
    return today_date

def get_current_time():
    local_time = Clock()
    server_time = localtime()
    local_time.set_time(server_time[3], server_time[4], server_time[5])
    return local_time



alarm_set = (-1, -1, -1) # global variable to store alarm time
alarm_trigger = False # global variable to indicate if alarm is set
def set_alarm():
    global alarm_set
    global alarm_trigger
    alarm_clock = Clock()
    
    while True:
        try:
            am_pm_input = input("Alarm mode | is it AM or PM?  >>").upper().strip()
            if am_pm_input not in ["AM", "PM"]:
                raise ValueError("Please pick AM or PM  ")
            
            time_input = input("Alarm mode | please set the alarm, format: HH:MM  >>").strip()
            
            if not re.fullmatch(r"^(1[0-2]|0?[1-9]):[0-5]?[0-9]", time_input):
                raise ValueError ("Please follow the format HH:MM")
            hour, minute = map(int, time_input.split(":"))

                    
            # Convert to 24-hour format
            if am_pm_input == "PM" and hour != 12:
                hour += 12
            elif am_pm_input == "AM" and hour == 12:
                hour = 0

            alarm_clock.set_time(hour, minute, 0)
            alarm_set = (alarm_clock.hour, alarm_clock.minute, 0)  
            break
        except ValueError: print("Please try again")
    os.system('cls')
    if alarm_set != (-1, -1, -1):
        alarm_trigger = True
        display_hour = alarm_clock.hour % 12 or 12
        print(f"Alarm set for {display_hour:02}:{minute:02} {am_pm_input}")
        sleep(2.5)
    return

def alarm_cuckoo(clock):
    global alarm_set
    global alarm_trigger
    if alarm_trigger:
        if (clock.hour, clock.minute, clock.second) == alarm_set:
            print("\nPress any key to snooze 9 minutes or hit 'X' key to cancel alarm")
            while True:
                print("\r\nCuckoo! Cuckoo! Cuckoo!  ", end="")
                sleep(0.5)
                print("\rAlarm ringing!             ", end="")
                sleep(0.5)
                print("\r\nCuckoo! Cuckoo! Cuckoo!  ", end="")
                sleep(0.5)
                print("\nPress any key to snooze 9 minutes or hit 'X' key to cancel alarm")
                sleep(0.5)
               
                # press key to snooze 9 min or stop
                if msvcrt.kbhit():
                    key = msvcrt.getch()
                    if key.upper() == b'X':
                        alarm_trigger = False
                        print("\n--Alarm canceled--")
                        return "canceled"
                    else: # 9 minutes snooze - add 9 minutes
                        snooze_clock = Clock()
                        snooze_clock.set_time(clock.hour, clock.minute, clock.second)
                        for _ in range(9 * 60):
                            snooze_clock.tick()
                        alarm_set = (snooze_clock.hour, snooze_clock.minute, snooze_clock.second)
                        print(f"\nSnoozed! new alarm set for {(snooze_clock.hour % 12 or 12):02}:{snooze_clock.minute:02} {snooze_clock.am_pm()}")
                        return "snoozed"
    return False
                    


def cancel_alarm():
    global alarm_set
    global alarm_trigger   
    os.system('cls')
    alarm_set = (-1, -1, -1)
    alarm_trigger = False
    print("Alarm canceled.")
    sleep(2.5)
    os.system('cls')
    return

def alarm_status():
    if alarm_set != (-1, -1, -1) and alarm_trigger == True:
        hour_24, minute, second = alarm_set
        hour_12 = hour_24 % 12 or 12
        if 0 <= hour_24 < 12:
            am_pm = "AM"
        else:
            am_pm = "PM"
        return f"Alarm {hour_12:02}:{minute:02} {am_pm}"
    return "No alarm set"


""" -----------------------------------------test mode related-------------------------------------------------"""
def test_mode():
    test_clock = Clock()
    
    
    while True:
        try:
            am_pm_input = input("Test mode | is it AM or PM?  >>").upper().strip()
            if am_pm_input not in ["AM", "PM"]:
                raise ValueError("Please pick AM or PM  ")
            
            time_input = input("Test mode | please set time to test, format: HH:MM:SS  >>").strip()
            
            if not re.fullmatch(r"^(1[0-2]|0?[1-9]):[0-5]?[0-9]:[0-5]?[0-9]", time_input):
                raise ValueError ("Please follow the format HH:MM:SS")
            hour, minute, second = map(int, time_input.split(":"))

                    
            # Convert to 24-hour format
            if am_pm_input == "PM" and hour != 12:
                hour += 12
            elif am_pm_input == "AM" and hour == 12:
                hour = 0
            
            test_clock.set_time(hour, minute, second)
            # # testing for cuckoo sing at the top of the hour
            # if test_clock.minute == 0 and test_clock.second == 0:
            #     test_clock._last_sing_hour = -1
            #     test_clock.cuckoo_sing()       
            break
        except ValueError: print("Please try again")
            
    os.system('cls')
    
    
    print("Test mode | Please hit any key to go back to the main menu")
    while True:
        
        if test_clock.minute == 0 and test_clock.second == 0:
            test_clock._last_sing_hour = -1
        
        print("\r" + str(test_clock), end="")
        result = alarm_cuckoo(test_clock)
        if result in ("snoozed", "canceled"):
            sleep(1)
            break
        
        if test_clock.minute == 0 and test_clock.second == 0:
            test_clock.cuckoo_sing()
            
        test_clock.tick()
        sleep(1)
        
        if msvcrt.kbhit():
            msvcrt.getch()
            break
             
    os.system('cls')
    return





"""
    # global alarm_set
    # # alarm check, if alarm is canceled or snoozed, it will exit the test mode back to main.
    # if (test_clock.hour, test_clock.minute, test_clock.second) == alarm_set and alarm_trigger == True:
    #     print("\nPress any key to snooze 9 minutes or hit 'X' key to cancel alarm")
    #     while True: 
    #         # press key to snooze 9 min or stop
    #         if msvcrt.kbhit():
    #             key = msvcrt.getch()
    #             if key.upper() == b'X':
    #                 alarm_trigger = False
    #                 print("\n--Alarm canceled--")
    #                 sleep(1)
    #                 return
    #             else: # 9 minutes snooze - add 9 minutes
    #                 snooze_clock = Clock()
    #                 snooze_clock.set_time(test_clock.hour, test_clock.minute, test_clock.second)
    #                 for _ in range(9 * 60):
    #                     snooze_clock.tick()
    #                 alarm_set = (snooze_clock.hour, snooze_clock.minute, snooze_clock.second)
    #                 print(f"\nSnoozed! new alarm set for {(snooze_clock.hour % 12 or 12):02}:{snooze_clock.minute:02} {snooze_clock.am_pm()}")
    #                 sleep(1)
    #                 return 
"""

if __name__ == "__main__":
    main()


