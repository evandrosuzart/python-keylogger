from file_utils import create_bat_file
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        report_method = "file"
    else:
        report_method = sys.argv[1]
    create_bat_file(report_method)