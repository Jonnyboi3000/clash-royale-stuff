import pyautogui
import time
import win32gui
import win32con
def callback_enum_windows(hwnd,window_dict):
    if win32gui.IsWindowVisible(hwnd):
        this_window_dict={}
        this_window_dict['title']=win32gui.GetWindowText(hwnd)
        window_dict[hwnd]=this_window_dict
    
def get_window_list_dict():
    window_dict={}
    win32gui.EnumWindows(callback_enum_windows,window_dict)
    return(window_dict)
wd=get_window_list_dict()
nox_list=[(x,wd[x]['title']) for x in wd if 'NoxPlayer' in wd[x]['title']]

print(nox_list)
if len(nox_list)==1:
    print('found one')
    win32gui.ShowWindow(nox_list[0][0],win32con.SW_MINIMIZE)
    time.sleep(.01)
    win32gui.ShowWindow(nox_list[0][0],win32con.SW_MAXIMIZE)

time.sleep(3)
pyautogui.leftClick(100,100)
time.sleep(2)

#found_picture=pyautogui.locateOnScreen('C:/Users/john/Downloads/crstuff/cardrequest.PNG')

bfp=pyautogui.locateOnScreen('C:/Users/john/Downloads/crstuff/bf.PNG')

#pyautogui.click(found_picture.left+40, found_picture.top+10, 1, 1, button='left')

pyautogui.click(bfp.left+40, bfp.top+10, 1, 1, button='left')

battlepic=pyautogui.locateOnScreen('C:/Users/john/Downloads/crstuff/battle.PNG')

pyautogui.click(battlepic.left+40, battlepic.top+10, 1, 1, button='left')

print(found_picture)