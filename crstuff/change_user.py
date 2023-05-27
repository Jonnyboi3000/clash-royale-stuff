# This is a crude prototype for changeing user.
# the coordinates for the user slots are in a dictionary and set for my screen
# the code brings up Nox using the common code
# the function select_user() given an indeax (1,2,3,4) selects that user slot
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
    # add a sleep for the resize to complete
    time.sleep(1)

else:
    print('no nox player')
    exit()

ipath='c:/Users/john/Downloads/crstuff'
ipath='.'


user_click_positions={ 1: (1818,999),2:(1818,1166),3:(1818,1363),4:(1818,1500)}

def select_user(slot_number):
    menu=pyautogui.locateOnScreen(ipath+'/menu-hamburger.png')
    pyautogui.click(menu.left+menu.width/2, menu.top+menu.height/2, 1, 1, button='left')
    time.sleep(1)

    menu_change_user=pyautogui.locateOnScreen(ipath+'/menu-change-user.png')
    pyautogui.click(menu_change_user.left+menu_change_user.width/2, menu_change_user.top+menu_change_user.height/2, 1, 1, button='left')
    time.sleep(1)
    click_position=user_click_positions[slot_number]
    print(click_position)

    pyautogui.click(click_position[0], click_position[1], 1, 1, button='left')
    time.sleep(1)
    
# time.sleep(2)

#select_user(1)




