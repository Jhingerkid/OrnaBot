from pyautogui import *
import pyautogui
import time

def checkMana():
    mpStatus = [
        "mp1.png", "mp2.png", "mp3.png", "mp4.png", "mp5.png", "mp6.png", "mp7.png", "mp8.png",
        "mp9.png", "mp10.png", "mp11.png", "mp12.png", "mp13.png", "mp14.png", "mp15.png", "mp16.png",
        "mp17.png", "mp18.png", "mp19.png"
        ]
    for mp in mpStatus:
        if pyautogui.locateOnScreen('CombatMana/'+mp, region=(620, 580, 50, 50), confidence=.95, grayscale=True) != None:
            return 1
    return 0