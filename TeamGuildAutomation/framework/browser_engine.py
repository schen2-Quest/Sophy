from selenium import webdriver
import configparser
import os.path

class BrowserEngine(object):

    def __init__(self, dirver):
        self.driver = dirver

    def open_browser(self):
        config = configparser.ConfigParser()
        file_path = os.path.join(os.path.dirname(__file__) , '..', 'config', 'config.ini')
        config.read(file_path)
        browser = config.get("browserType", "browserName")
        url = config.get("testServer", "URL")

        if browser == "Firefox":
            # driver = webdriver.Firefox()
            desired_cap = {
                    'platform': "Windows 10",
                    'browserName': "firefox",
                    'version': "56",
                    'screenResolution': "1680x1050"
                }
        elif browser == "Chrome":
            desired_cap = {
                    'platform': "Windows 10",
                    'browserName': "chrome",
                    'version': "65",
                    'screenResolution': "1680x1050"
                }
        elif browser == "IE":
            desired_cap = {
                    'platform': "Windows 10",
                    'browserName': "iexplore",
                    'version': "11",
                    'screenResolution': "1680x1050"
                }

        driver = webdriver.Remote(
            command_executor='http://sso-quest-Skila.Zheng:657d31c5-9368-4b89-9ef0-17dc52f694e0@ondemand.saucelabs.com:80/wd/hub/',
            desired_capabilities=desired_cap)

        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(60)
        driver.set_script_timeout(60)

        return driver

    def quit_browser(self):
        self.driver.quit()