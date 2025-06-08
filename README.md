# Cuckoo Clock Alarm App (Windows Console)

#### Video Demo:  <https://youtu.be/-EQgTvnFGRQ>

#### Description: 

A playful and functional Windows console-based clock app with an old-fashioned charm. This project simulates a cuckoo clock that sings on the hour—except during quiet hours—and includes alarm features with snooze support and a test mode for time simulation.

## Features

- **Live Clock Display** (12-hour AM/PM format)
- **Cuckoo Sing** at the top of each hour (between 8AM and 8PM)
- **Cricket Sound** during quiet hours (8PM–8AM)
- **Set & Cancel Alarms**
- **Snooze** alarms for 9 minutes with any key
- **Test Mode** for simulating a specific time
- 🖥**Menu Interface** using Windows `msvcrt` module
Menu interface
-----------------------------------------------------------------
Menu: 1 = set alarm | 2 = cancel alarm | 3 = test mode | 4 = exit 
-----------------------------------------------------------------

## Requirements

- Python 3.6+
- **Windows OS only** (uses `msvcrt` for keyboard interaction)
- No third-party libraries required

---

## How to Run

Clone the repo and run the script from your terminal:

```bash
python cuckoo_clock.py


