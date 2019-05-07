import time
import os
import pyautogui
import mouse
from imagesearch import imagesearch


def network():
    pos = imagesearch("mynetwork.png")
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        pyautogui.click(pos[0], pos[1])


def linkedin():
    pos = imagesearch("linkedinbutt.png")
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        pyautogui.click(pos[0], pos[1])


def wheel():
    for y in range(0, 5):
        mouse.wheel(-1)
        time.sleep(1)


def contacts():
    pos = imagesearch("contact.png")
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        pyautogui.click(pos[0], pos[1])
        time.sleep(2)


os.startfile(r"C:\python\bluestacks_1")
time.sleep(30)
linkedin()
time.sleep(5)
pyautogui.press('f11')
time.sleep(5)
network()
wheel()
for z in range(0, 40):
    contacts()


os.system("taskkill /f /im  Bluestacks.exe")
os.system("taskkill /f /im  HD-Agent.exe")
os.system("taskkill /f /im  HD-MultiInstanceManager.exe")
os.system("taskkill /f /im  HD-Player.exe")


os.startfile(r"C:\ProgramData\BlueStacks\Client\Bluestacks.exe")
time.sleep(30)
linkedin()
time.sleep(5)
pyautogui.press('f11')
time.sleep(5)
network()
wheel()
for z in range(0, 40):
    contacts()


os.system("taskkill /f /im  Bluestacks.exe")
os.system("taskkill /f /im  HD-Agent.exe")
os.system("taskkill /f /im  HD-MultiInstanceManager.exe")
os.system("taskkill /f /im  HD-Player.exe")