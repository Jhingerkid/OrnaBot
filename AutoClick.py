from pyautogui import *
from CombatHealth import healthCheck
from CombatMana import manaCheck
import pyautogui
import time
import keyboard
import random


def initiateCombat(imageName):
    # Initiate the battle
    time.sleep(2)
    battleButton = pyautogui.locateCenterOnScreen("BattleButton.png", confidence=0.5)
    pyautogui.click(x=battleButton[0], y=battleButton[1])
    time.sleep(3)
    # Battle has started
    combatLoop(imageName)
    # Wait for continue screen to load, then click continue
    time.sleep(2)
    continueButton = pyautogui.locateCenterOnScreen("Continue.png", confidence=0.7)
    pyautogui.click(x=continueButton[0], y=continueButton[1])
    time.sleep(2)
    # If the battle resulted in a levelup, click continue again
    if pyautogui.locateOnScreen('LevelUp.png', confidence=0.5) != None:
        levelContinueButton = pyautogui.locateCenterOnScreen("Continue.png", confidence=0.7)
        pyautogui.click(x=levelContinueButton[0], y=levelContinueButton[1])
    # Go back to looking for enemies
    monsterLocater()


def combatLoop(imageName):
    # Locate enemy
    enemy = pyautogui.locateOnScreen('MonsterImages/'+imageName, grayscale=True, confidence=.8)
    # Combat loop
    while enemy != None:
        time.sleep(2)
        combatRound()
        time.sleep(4)
        if pyautogui.locateOnScreen('Victory.png', grayscale=True, confidence=.8):
            enemy = None


def heal():
    time.sleep(2)
    x, y = pyautogui.locateCenterOnScreen("ItemButton.png", confidence=.9)
    pyautogui.moveTo(x, y, .25)
    pyautogui.click(x+random.randint(-10,10),y+random.randint(-10,10))
    time.sleep(2)
    x, y = pyautogui.locateCenterOnScreen("HealthPotion.png", confidence=.95)
    pyautogui.moveTo(x, y, .25)
    pyautogui.click(x+random.randint(-10,10),y+random.randint(-10,10))


def replenishMP():
    time.sleep(2)
    x, y = pyautogui.locateCenterOnScreen("ItemButton.png", confidence=.9)
    pyautogui.moveTo(x, y, .25)
    pyautogui.click(x+random.randint(-10,10),y+random.randint(-10,10))
    time.sleep(2)
    x, y = pyautogui.locateCenterOnScreen("ManaPotion.png", confidence=.95)
    pyautogui.moveTo(x, y, .25)
    pyautogui.click(x+random.randint(-10,10),y+random.randint(-10,10))


def combatRound():
    # Heal if HP is too low
    if (healthCheck.checkHealth()):
        heal()
    # Replenish MP if it is too low
    if (manaCheck.checkMana()):
        replenishMP()
    # If healing isn't needed, attack
    else:
        x, y = pyautogui.locateCenterOnScreen("Sparkerino.png", confidence=.9)
        pyautogui.moveTo(x, y, .25)
        pyautogui.click(x+random.randint(-10,10),y+random.randint(-10,10))
        


def clickMonster(x, y, image):
    pyautogui.moveTo(x, y, .25)
    pyautogui.click()
    initiateCombat(image)


def check(monsterName):
    left = str(monsterName) + "Left.png"
    right = str(monsterName) + "Right.png"
    fight = str(monsterName) + "Fight.png"
    # This comment can be used to check recognition confidence levels
    print(left,right)
    print(f'{pyautogui.locateOnScreen("MonsterImages/"+left, grayscale=True, confidence=.8)}')
    print(f'{pyautogui.locateOnScreen("MonsterImages/"+right, grayscale=True, confidence=.8)}')
    if pyautogui.locateOnScreen('MonsterImages/'+left, confidence=.8, grayscale=True) != None:
        x, y = pyautogui.locateCenterOnScreen('MonsterImages/'+left, confidence=.8, grayscale=True)
        image = fight
        clickMonster(x, y, image)
    elif pyautogui.locateOnScreen('MonsterImages/'+right, confidence=.8, grayscale=True) != None:
        x, y = pyautogui.locateCenterOnScreen('MonsterImages/'+right, confidence=.8, grayscale=True)
        image = fight
        clickMonster(x, y, image)


def monsterLocater():
    monsterList = [
        "Goblin", "RedSlime", "Skeleton", "Wisp", "Wolfman", 
        "Demon", "Rat", "Draconian", "FeralHorse", 
        "Hawk", "Crow", "LivingArmor", "Spider", "Flame",
        "FallenWarrior","Bandit", "EvilEye", "GreaterSnake"
        ]
    while keyboard.is_pressed('q') == False:
        for monsterName in monsterList:
            check(monsterName)


monsterLocater()


# Additions - 
# When in the map screen, the bot should check status bars below the character. If outlined red, initiate and auto heal
# Whenever the character is poisoned, use an antidote