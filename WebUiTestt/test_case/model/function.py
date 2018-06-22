from selenium import webdriver
import os
from test_case.model.driver import cur_file_dir


def insert_img(driver, file_name):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        base_dir = str(base_dir)
        base_dir = base_dir.replace('/', '\\')
        base = base_dir.split('test_case')[0]
        file_path = base + "report\\image\\" + file_name
        print(file_path)
        driver.get_screenshot_as_file(file_path)


if __name__ == '__main__':
        current_path = cur_file_dir()
        base = current_path.split('test_case')[0]
        driver_path = base + "\\webdriver\\geckodriver.exe"
        print(driver_path)
        driver = webdriver.Firefox(executable_path=driver_path)
        driver.get("http://10.154.10.38")
        insert_img(driver, 'login.png')
        driver.quit()

