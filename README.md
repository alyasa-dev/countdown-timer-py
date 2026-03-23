# ⏱️ Countdown Timer
A simple command-line countdown timer built in Python.
## How it works
The program asks you to enter how many seconds you want to count down from. It then ticks down one second at a time, printing each second to the screen until it hits zero and prints "Time's Up!". After each countdown it asks if you want to start another one — type Y to go again or N to quit. If you type a word instead of a number or enter a negative number the program will catch it and ask you to try again instead of crashing.
## Usage
```bash
python main.py
```
## Example
```
How many seconds should the countdown start from: abc
Please enter a valid number!
How many seconds should the countdown start from: -5
Please enter a positive number!
How many seconds should the countdown start from: 5
5
4
3
2
1
Time's Up!
Do you want another countdown? Y/N: y
How many seconds should the countdown start from: 3
3
2
1
Time's Up!
Do you want another countdown? Y/N: n
```
## Built with
- Python 3
- time module (built-in)
