import os 
import pynput
from pynput.keyboard import Key, Listener

#Function referenced from GeeksforGeeks
def clear():
 
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

def display_text(text):
    #print("\n")
    print(text)
    print("\n")

def press_enter():
    ans = input("\nPress ENTER to continue...")
    print("\n"*15)
