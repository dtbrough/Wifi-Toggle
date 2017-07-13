#! python3
# Author: D.Brough
# Created: 13th July 2017

''' Tool to toggle wifi on/off. '''

import pyautogui, time

pyautogui.keyDown('fn')
pyautogui.keyDown('winleft')
pyautogui.press('x')
pyautogui.keyUp('fn')
pyautogui.keyUp('winleft')

pyautogui.press('t')

pyautogui.keyDown('alt')
pyautogui.press('f4')
pyautogui.keyUp('alt')

# print('Wifi toggled')
