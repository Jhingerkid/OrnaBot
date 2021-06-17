from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def initiateCombat(imageName):
    time.sleep(2)
    battleButton = pyautogui.locateCenterOnScreen("BattleButton.png", confidence=0.7)
    pyautogui.click(x=battleButton[0], y=battleButton[1])
    time.sleep(3)
    enemy = pyautogui.locateOnScreen(imageName, confidence=.6)
    x, y = pyautogui.locateCenterOnScreen("Sparkerino.png", confidence=.9)
    pyautogui.moveTo(x, y, .25)
    while enemy != None:
        time.sleep(2)
        pyautogui.click(x+random.randint(1,10),y+random.randint(1,10))
        enemy = pyautogui.locateOnScreen(imageName, confidence=.6)
    time.sleep(3)
    continueButton = pyautogui.locateCenterOnScreen("Continue.png", confidence=0.7)
    pyautogui.click(x=continueButton[0], y=continueButton[1])
    if pyautogui.locateOnScreen('LevelUp.png', confidence=0.5) != None:
        levelContinueButton = pyautogui.locateCenterOnScreen("Continue.png", confidence=0.7)
        pyautogui.click(x=levelContinueButton[0], y=levelContinueButton[1])


def clickMonster(x, y, image):
    pyautogui.moveTo(x, y, .25)
    pyautogui.click()
    initiateCombat(image)

def monsterLocater():
    while keyboard.is_pressed('q') == False:
        if pyautogui.locateOnScreen('RedSlimeLeft.png', confidence=.9) != None:
            x, y = pyautogui.locateCenterOnScreen("RedSlimeLeft.png", confidence=.9)
            image = "RedSlimeFight.png"
            clickMonster(x, y, image)
        elif pyautogui.locateOnScreen('RedSlimeRight.png', confidence=.9) != None:
            x, y = pyautogui.locateCenterOnScreen("RedSlimeRight.png", confidence=.9)
            image = "RedSlimeFight.png"
            clickMonster(x, y, image)
        elif pyautogui.locateOnScreen('SkeletonLeft.png', confidence=.9) != None:
            x, y = pyautogui.locateCenterOnScreen("SkeletonLeft.png", confidence=.9)
            image = "SkeletonFight.png"
            clickMonster(x, y, image)
            return
        elif pyautogui.locateOnScreen('SkeletonRight.png', confidence=.9) != None:
            x, y = pyautogui.locateCenterOnScreen("SkeletonRight.png", confidence=.9)
            image = "SkeletonFight.png"
            clickMonster(x, y, image)
            return
        elif pyautogui.locateOnScreen('WispRight.png', confidence=.8) != None:
            x, y = pyautogui.locateCenterOnScreen("WispRight.png", confidence=.8)
            image = "WispFight.png"
            clickMonster(x, y, image)
            return
        elif pyautogui.locateOnScreen('WispLeft.png', confidence=.8) != None:
            x, y = pyautogui.locateCenterOnScreen("WispLeft.png", confidence=.8)
            image = "WispFight.png"
            clickMonster(x, y, image)
            return

# def test(imageName):
#     enemy = pyautogui.locateOnScreen(imageName, confidence=.7)
#     print(enemy)

# test("WispLeft.png")

monsterLocater()


# print(f'{pyautogui.locateCenterOnScreen("SkeletonRight.png", confidence=0.5)}')
# while keyboard.is_pressed('t') == False:
#     if pyautogui.locateOnScreen('SkeletonRight.png', confidence=0.9) != None:
#         x, y = pyautogui.locateCenterOnScreen("SkeletonRight.png", confidence=.9)
#         pyautogui.moveTo(x, y, .25)