from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def initiateCombat(coords):
    location = coords
    x= location[0]
    y= location[1]
    print(x)
    print(y)
    pyautogui.click(x=x,y=y)


def monsterLocater(x):
    while x == 1:
        if pyautogui.locateOnScreen('RedSlimeLeft.png', confidence=0.5) != None:
            print(f'Left {pyautogui.locateCenterOnScreen("RedSlimeLeft.png", confidence=0.5)}')
            initiateCombat(pyautogui.locateCenterOnScreen("RedSlimeLeft.png", confidence=0.5))
            time.sleep(0.5)
        elif pyautogui.locateOnScreen('RedSlimeRight.png', confidence=0.5) != None:
            print(f'Right {pyautogui.locateCenterOnScreen("RedSlimeRight.png", confidence=0.5)}')
            initiateCombat(pyautogui.locateCenterOnScreen("RedSlimeRight.png", confidence=0.5))
            time.sleep(0.5)

monsterLocater(1)