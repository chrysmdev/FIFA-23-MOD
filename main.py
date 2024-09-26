# IMPORTS 
import os
import time
import pyautogui

# OPEN BOTH PROGRAMS
Program_Path_MM = "D:\JOGOS_COMPLEMENTOS\mods_fifa\FIFA_Mod_Manager_v1.1.8\FIFA_Mod_Manager.exe.exe"
Program_Path_FE = "D:\JOGOS_COMPLEMENTOS\mods_fifa\FIFA.23.LE.v23.1.3.6\Launcher.exe"

os.startfile(Program_Path_MM)
os.startfile(Program_Path_FE)

# PASSING THROUGH THE ADMIN QUESTION
time.sleep(2)
pyautogui.press('left')
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')