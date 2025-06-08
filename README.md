### **Cuckoo clock with alarm function**
Final project for CS50 Python:

#### Video Demo:  https://youtu.be/-EQgTvnFGRQ


#### Description:

-Cuckoo clock sings every hour, matching the hour on the clock (e.g., 1:00 PM = 1 cuckoo, 5:00 PM = 5 cuckoos).

-Uses a 12-hour clock format (AM/PM).

-Quiet hours are from 8:00 PM to 8:00 AM — no cuckoo sounds during this time.

-When an alarm is set, clock will sing until you either Snooze or Stop it.

-If you snooze, clock will sing again after 9 minutes.

### **Usage**
- Live mode: current time based on server-synced time
- Test mode: let's user chage current time in order to test the Cuckoo alarm/hourly sings

### Limitations
Currently, it only works on Windows, as the msvcrt module is used to detect keyboard inputs while the program is running.

