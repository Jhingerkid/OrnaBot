from pyautogui import *
import pyautogui
import time

def checkHealth():
    hpStatus = [
        "hp1.png", "hp2.png", "hp3.png", "hp4.png", "hp5.png", "hp6.png", "hp7.png", "hp8.png",
        "hp9.png", "hp10.png", "hp11.png", "hp12.png", "hp13.png", "hp14.png", "hp15.png", "hp16.png",
        "hp17.png", "hp18.png", "hp19.png", "hp20.png"
        ]
    for hp in hpStatus:
        if pyautogui.locateOnScreen('CombatHealth/'+hp, region=(620, 550, 50, 50), confidence=.95, grayscale=True) != None:
            return 1
    return 0