from pygetwindow import getWindowsWithTitle,getActiveWindow
from pyautogui import hotkey
from time import sleep
chrome_black_list=['哔哩哔哩','知乎','灌水区']
game_black_list=['Steam']
def get_web_page():
    window=getWindowsWithTitle('Chrome')
    if window:
        return window[0]
    return None
def check_chrome():
    page=get_web_page()
    if page:
        title=page.title
        for black in chrome_black_list:
            if black in title:
                page.activate()
                sleep(0.1)
                hotkey('alt','left')
                sleep(0.2)
                now=get_web_page()
                if now and now.title==title:
                    now.activate()
                    hotkey('ctrl','w')
                return
def check_game():
    window=getActiveWindow()
    if window:
        for black in game_black_list:
            if window.title==black:
                hotkey('alt','f4')
                return
while 1:
    check_chrome()
    check_game()
    sleep(0.5)
