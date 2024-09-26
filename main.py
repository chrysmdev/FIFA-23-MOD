# IMPORTS 
from os import startfile
from time import sleep
import pyautogui

# OPEN FILE EDITOR
Program_Path_FE = "D:\JOGOS_COMPLEMENTOS\mods_fifa\FIFA.23.LE.v23.1.3.6\Launcher.exe"
startfile(Program_Path_FE)

# PASSING THROUGH THE USER ACCOUNT CONTROL
sleep(1)
pyautogui.press('enter')
