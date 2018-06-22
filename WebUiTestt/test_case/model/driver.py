from selenium import webdriver
import os
import sys
import time


def browser():
    current_path = cur_file_dir()
    base = current_path.split('test_case')[0]
    driver_path = base + "\\webdriver\\geckodriver.exe"
    print(driver_path)
    driver = webdriver.Firefox(executable_path=driver_path)
    return driver


def cur_file_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)


def log_info(text):
    print("<font color>='#696969'\t- %s: %s</font>" % (time.strftime('%X', time.localtime(time.time())), text))


if __name__ == '__main__':
        dr = browser()
        dr.get("http://10.154.10.38")
        log_info("use")
        dr.quit()
