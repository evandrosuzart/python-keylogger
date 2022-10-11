# Python Keylogger

## This is a study project, and the author is not responsible for the misuse of this content.

As the name of the repository says, it is a simple but parameterizable keylogger, where we can define the interval in which the application collects the content typed by the monitored user.
In addition, it is also possible to send screenshots and logs via email defined by the person who configures the application.

The first step is to configure the environment variables.

The env_vars.json file contains the environment variables here 

ENCODE -> charset files
EMAIL_ADDRESS -> destination email address in base64
EMAIL_PASSWORD -> email password converted to base64
SEND_REPORT_EVERY -> interval between each application inspection cycle
SCREENSHOT_INTERVAL -> screenshot interval
SCREENSHOT_PATH -> directory where screenshots are stored
LOG_PATH -> directory where log files are stored

The startup_bat_generator.py file receives as an argument the type of report you want:
* file
* email

The file_utils.py file is responsible for all file manipulation, whether creating the log directory, log file or saving the screenshot.

The env_utils.py file is responsible for receiving the contents of the env_vars.json file and saving the environment variables in the application execution context.

If you want to generate the .bat file, just run the startup_bat_generator.py file, and on the next windows restart, the system starts and the application starts up in the background.
* python startup_bat_generator.py report_method
where the report_method variable should be filled by email or file

If you want to run the application immediately, run the following command inside the root directory of the application:
* python main.py report_method
where the report_method variable should be filled by email or file



