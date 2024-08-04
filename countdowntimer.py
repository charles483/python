# Type: Python Source Code
# Description: Count down timer
# Code Snippet:
# This code snippet is a simple count down timer written in Python. It takes the time in seconds as input and counts down to zero. The timer is displayed in the format HH:MM:SS.
#********************************code*****************************************
import time

def count_down(t):
    while t:
        hours, rem = divmod(t, 3600)
        mins, sec = divmod(rem, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, sec)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
        
    print('Timer completed')

t = input('Enter the time in seconds: ')
count_down(int(t))
