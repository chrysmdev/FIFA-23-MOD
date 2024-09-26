# IMPORTS 
from os import startfile
from time import sleep
import pyautogui

# OPEN FILE EDITOR
Program_Path_FE = "D:\JOGOS_COMPLEMENTOS\mods_fifa\FIFA.23.LE.v23.1.3.6\Launcher.exe"
startfile(Program_Path_FE)

# PASSING THROUGH DISCLAIMER
sleep(1)
pyautogui.press('enter')

# OPEN MOD MANAGER
Program_Path_MM = "D:\JOGOS_COMPLEMENTOS\mods_fifa\FIFA_Mod_Manager_v1.1.8\FIFA_Mod_Manager.exe.exe"
startfile(Program_Path_MM)

# LAUNCH FIFA 23 THROUGH MOD MANAGER
sleep(3)
pyautogui.doubleClick(780, 300)